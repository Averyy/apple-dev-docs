# Analyzing media

**Framework**: Professional-Video-Applications  
**Role**: Article

Use the FxPlug analysis API to analyze frames of source media before rendering them.

## Overview

Frame-by-frame analysis of video clips is commonly required for rendering tasks that occur in an FxPlug plug-in. For example, tracking of objects and stabilization of video both require a pre-render analysis of video frames before rendering.

FxPlug 4.1 introduces [`FxAnalysisAPI`](../professional_video_applications/fxanalysisapi.md), which FxPlug plug-ins can use to analyze video frames from source media in Final Cut Pro X or Motion. `FxAnalysisAPI` uses the host app’s built-in analysis infrastructure so that your plug-in’s analysis can be performed in the background, and you can view the progress UI in the same location as the host’s own analysis processes. This provides a consistent user experience for both native effects and FxPlug plug-ins that require analysis.

The example plug-in `FxBrightnessAnalysis` demonstrates how to implement the analysis APIs for a filter that analyzes all frames and then adjusts the brightness of the frames to a consistent level.

### Set the desired analysis time range

Your plug-in can tell Motion and Final Cut Pro what time range to analyze. In the following example, using [`desiredAnalysisTimeRange(_:forInputWith:)`](../professional_video_applications/fxanalyzer/desiredanalysistimerange%28_,forinputwith%29.md), the `desiredRange` is set to whatever the host provides in `inputTimeRange`.

**Swift**:

```swift
func desiredAnalysisTimeRange(_ desiredRange: inout CMTimeRange?, forInputWith inputTimeRange: CMTimeRange) throws {
    // Whatever the host app has, we want to analyze
    desiredRange = inputTimeRange
}
```

**Objective-C**:

```objc
- (BOOL)desiredAnalysisTimeRange:(CMTimeRange *)desiredRange
           forInputWithTimeRange:(CMTimeRange)inputTimeRange
                           error:(NSError **)error
{
    // Whatever the host app has, we want to analyze
    *desiredRange = inputTimeRange;
    return YES;
}
```

### Set up your plug-in for analysis

Set up data arrays or variables that will be used later for analysis in the [`setupAnalysis(for:frameDuration:)`](../professional_video_applications/fxanalyzer/setupanalysis%28for,frameduration%29.md) method for [`FxAnalyzer`](../professional_video_applications/fxanalyzer.md). You can also use other FxPlug APIs like [`FxParameterSettingAPI_v5`](../professional_video_applications/fxparametersettingapi_v5.md) within this method to set parameter states during analysis, as in the example below.

**Swift**:

```swift
    @objc func setupAnalysis(for analysisRange: CMTimeRange, frameDuration: CMTime) throws {
        analysisLock.lock()
        do {
            startFrameTime = analysisRange.start
            analysisFrameDuration = frameDuration
            
            if analyzedData != nil {
            free(_: analyzedData)
                analyzedData = nil
            }
            
            let numFrames = round(CMTimeGetSeconds(analysisRange.duration) / CMTimeGetSeconds(frameDuration))
            analyzedData = UnsafeMutablePointer.allocate(capacity: MemoryLayout<BrightnessAnalysis>.stride * size_t(numFrames))
            let initedVal = BrightnessAnalysis(frameTime: CMTime.zero, averageLuminance: 0.0)
            analyzedData?.initialize(to: initedVal)
            nextAnalyzedFrameNum = 0
        }
        analysisLock.unlock() 
    }
```

**Objective-C**:

```objc
- (BOOL)setupAnalysisForTimeRange:(CMTimeRange)analysisRange
                    frameDuration:(CMTime)frameDuration
                            error:(NSError**)error
{
    BOOL result = YES;
    [analysisLock lock];
    {
        startFrameTime = analysisRange.start;
        analysisFrameDuration = frameDuration;
        
        if (analyzedData != NULL)
        {
            free(analyzedData);
            analyzedData = NULL;
        }
        
        double numFrames = ceil(CMTimeGetSeconds(analysisRange.duration) / CMTimeGetSeconds(frameDuration));
        totalFramesToAnalyze = ceil(numFrames);
        analyzedData = malloc(sizeof(*analyzedData) * (size_t)numFrames);
#if BACKWARDS_ANALYSIS
        nextAnalyzedFrameNum = numFrames - 1;
#else
        nextAnalyzedFrameNum = 0;
#endif // BACKWARDS_ANALYSIS
    }
    [analysisLock unlock];
    
    return result;
}
```

### Store data to persist between application launches

Your plug-in needs to store the analysis data in a parameter so that it can persist between application launches. You typically do this with a custom parameter added in [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md). You also supply the user with a button to start the analysis in [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md). When implementing custom parameters, implement the [`class(forCustomParameterID:)`](../professional_video_applications/fxtileableeffect/class%28forcustomparameterid%29.md) method so your custom parameters can be serialized and deserialized properly.

**Swift**:

```swift
   func addParameters() throws {
        let paramAPI = _apiManager.api(for: FxParameterCreationAPI_v5.self) as! FxParameterCreationAPI_v5

// ...
        paramAPI.addCustomParameter(withName: "Analysis Data", parameterID: kParam.analysisData.rawValue, defaultValue: [AnyHashable : Any]() as NSCopying & NSSecureCoding & NSObjectProtocol, parameterFlags: FxParameterFlags( kFxParameterFlag_HIDDEN | kFxParameterFlag_NOT_ANIMATABLE))
    }
```

**Objective-C**:

```objc
- (BOOL)addParametersWithError:(NSError * _Nullable * _Nullable)error {
    id<FxParameterCreationAPI_v5>   paramAPI    = [_apiManager apiForProtocol:@protocol(FxParameterCreationAPI_v5)];
    if (paramAPI == nil)
    {
        return NO;
    }
// ...

    [paramAPI addCustomParameterWithName:@"Analysis Data"
                             parameterID:kParam_AnalysisData
                            defaultValue:[NSDictionary dictionary]
                          parameterFlags:kFxParameterFlag_HIDDEN | kFxParameterFlag_NOT_ANIMATABLE];    
    return YES;
}
```

**Swift**:

```swift
    func `class`(forCustomParameterID parameterID: UInt32) -> AnyClass {
        if parameterID == kParam.analysisData.rawValue {
            return NSDictionary.self
        }
        return NSNull.self
    }
```

**Objective-C**:

```objc
- (Class)classForCustomParameterID:(UInt32)parameterID
{
    if (parameterID == kParam_AnalysisData)
    {
        return [NSDictionary class];
    }
    
    return nil;
}
```

### Start the analysis

In the `FxBrightnessAnalysis` example plug-in, when the user clicks the Start Analysis push button parameter, the host app calls the plug-in’s `-startAnalysis:` function, which then initializes the [`FxAnalysisAPI`](../professional_video_applications/fxanalysisapi.md) and requests that the host start a forward analysis.

![A screen shot of the FxBrightnessAnalysis example’s parameter inspector.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3676024@2x.png)

> ❗ **Important**:  Each plug-in instance is limited to only one analysis job at a time. If you attempt to start another analysis while an analysis is already in progress, the analysis API returns an error. As in the example code below, first check that the [`analysisStateForEffect()`](../professional_video_applications/fxanalysisapi/analysisstateforeffect%28%29.md) isn’t [`kFxAnalysisState_AnalysisStarted`](../professional_video_applications/kfxanalysisstate_analysisstarted.md) or [`kFxAnalysisState_AnalysisRequested`](../professional_video_applications/kfxanalysisstate_analysisrequested.md) before attempting to start an analysis.

**Swift**:

```swift
    @objc func startAnalysis(_ sender: Any?) {
        let analysisAPI = _apiManager.api(for: FxAnalysisAPI.self) as! FxAnalysisAPI?
        let colorGamutAPI = _apiManager.api(for: FxColorGamutAPI_v2.self) as! FxColorGamutAPI_v2?
        if (analysisAPI == nil) || (colorGamutAPI == nil) {
            print("Unable to retrieve analysis API or color gamut API. Stopping analysis.")
            return
        }
        
        let rgbToYCbCr = colorGamutAPI?.colorMatrixFromDesiredRGBToYCbCr()!
        let matrixData : UnsafeMutablePointer<Matrix44Data> = (rgbToYCbCr?.matrix())!
        luminanceRed = matrixData.pointee.0.0
        luminanceGreen = matrixData.pointee.0.1
        luminanceBlue = matrixData.pointee.0.2
        
        // If analysis isn't already happening, start it. If it is already happening, just
        // continue on.
        let currentState : FxAnalysisState = (analysisAPI?.analysisStateForEffect())!
        if currentState != kFxAnalysisState_AnalysisStarted && currentState != kFxAnalysisState_AnalysisRequested {
            do {
                if BACKWARDS_ANALYSIS {
                    try analysisAPI?.startBackwardAnalysis(kFxAnalysisLocation_CPU)
                }
                else {
                    try analysisAPI?.startForwardAnalysis(kFxAnalysisLocation_CPU)
                }
            } catch {
                print("Unable to start analysis due to error \(error)")
            }
        }
    }

```

**Objective-C**:

```objc
- (void)startAnalysis:(id)sender
{
    id<FxAnalysisAPI>   analysisAPI = [_apiManager apiForProtocol:@protocol(FxAnalysisAPI)];
    id<FxColorGamutAPI_v2>  colorGamutAPI   = [_apiManager apiForProtocol:@protocol(FxColorGamutAPI_v2)];
    if ((analysisAPI == nil) || (colorGamutAPI == nil))
    {
        NSLog (@"Unable to retrieve analysis API or color gamut API. Stopping analysis.");
        return;
    }
    
    FxMatrix44* rgbToYCbCr  = [colorGamutAPI colorMatrixFromDesiredRGBToYCbCr];
    Matrix44Data*   matrixData  = [rgbToYCbCr matrix];
    luminanceRed = (*matrixData)[0][0];
    luminanceGreen = (*matrixData)[0][1];
    luminanceBlue = (*matrixData)[0][2];
    
    // If analysis isn't already happening, start it. If it is already happening, just
    // continue on.
    FxAnalysisState currentState = [analysisAPI analysisStateForEffect];
    if ((currentState != kFxAnalysisState_AnalysisStarted) && (currentState != kFxAnalysisState_AnalysisRequested))
    {
        NSError* err = nil;
#if BACKWARDS_ANALYSIS
        if (![analysisAPI startBackwardAnalysis:kFxAnalysisLocation_CPU
                                          error:&err])
#else
        if (![analysisAPI startForwardAnalysis:kFxAnalysisLocation_CPU
                                         error:&err])
#endif // BACKWARDS_ANALYSIS
        {
            NSLog (@"Analysis failed to start due to error: %@", err);
        }
    }
}
```

### Analyze the frames and store the results

Use the [`analyzeFrame(_:at:)`](../professional_video_applications/fxanalyzer/analyzeframe%28_,at%29.md) method allows you to analyze each frame and store results. In the following example the plug-in samples all the pixels to determine the average luminance of each frame, and then stores the `averageLuminance` value for each frame (`frameTime`) in the `analyzedData` array.

> **Note**:  The FxAnalysis API always analyzes all pixels in the frame, instead of just tiles.

**Swift**:

```swift
    @objc func analyzeFrame(_ frame: FxImageTile!, at frameTime: CMTime) throws {

        if frame?.ioSurface.pixelFormat == kCVPixelFormatType_128RGBAFloat {
        
        // Calculate the average brightness of the next frames
        var averageLuminance : Double = 0
        let width : Int = (frame?.ioSurface.width)!
        let height : Int = (frame?.ioSurface.height)!
        
        frame?.ioSurface.lock(options: IOSurfaceLockOptions(rawValue: 0x00000001), seed: nil) //kIOSurfaceLockReadOnly
        let rowBytes : Int = (frame?.ioSurface.bytesPerRow)!

        let baseAddr = frame?.ioSurface.baseAddress
        for row in 0..<height {
            let rawPixels = baseAddr?.advanced(by: row * rowBytes)
            let pixels = rawPixels?.bindMemory(to: Float32.self, capacity: width * 4)
            var nextPixel = UnsafePointer<Float>(pixels)//Float = Float((pixels!) + (row * rowBytes))
            for _ in 0..<width {
                let red = Double(nextPixel!.pointee)
                nextPixel = nextPixel?.advanced(by: 1)
                let green = Double(nextPixel!.pointee)
                nextPixel = nextPixel?.advanced(by: 1)
                let blue = Double(nextPixel!.pointee)
                nextPixel = nextPixel?.advanced(by: 2) // 2 because we want to skip alpha
                
                luminanceRed *= red
                luminanceGreen *= green
                luminanceBlue *= blue
                let luminance = luminanceRed + luminanceGreen + luminanceBlue
                averageLuminance += luminance
            }
        }

        frame?.ioSurface.unlock(options: IOSurfaceLockOptions(rawValue: 0x00000001), seed: nil) //kIOSurfaceLockReadOnly
        
        
        averageLuminance /= Double(width) * Double(height)
        
        analysisLock.lock()

        // Add our analysis data to the array
        print("Average luminance for frame at time \(CMTimeGetSeconds(frameTime)) = \(averageLuminance)")
            analyzedData?[nextAnalyzedFrameNum].frameTime = frameTime
            analyzedData?[nextAnalyzedFrameNum].averageLuminance = averageLuminance

            nextAnalyzedFrameNum += 1
        
        // Attempt to save partial data. If it fails, don't worry because we'll save it all at the end
        // Also, don't save on every frame, as it slows down the analysis too much. Save every 10th
        // frame instead.
        if (nextAnalyzedFrameNum % 10) == 0 {
            do {
                try saveAnalyzedData()
            }
            catch {
                print("Unable to save partial analysis data")
            }
        }
        
        analysisLock.unlock()
        }
    }

```

**Objective-C**:

```objc
- (BOOL)analyzeFrame:(FxImageTile *)frame
              atTime:(CMTime)frameTime
               error:(NSError **)error
{
    if (frame.ioSurface.pixelFormat != kCVPixelFormatType_128RGBAFloat)
    {
        if (error != nil)
        {
            *error = [NSError errorWithDomain:FxPlugErrorDomain
                                         code:kFxError_AnalysisError
                                     userInfo:@{ NSLocalizedDescriptionKey : @"Invalid bit depth for analysis data" }];
        }
        return NO;
    }
    
    // Calculate the average brightness of the next frames
    double averageLuminance = 0;
    NSInteger   width   = frame.ioSurface.width;
    NSInteger   height  = frame.ioSurface.height;
    
    [frame.ioSurface lockWithOptions:kIOSurfaceLockReadOnly
                                seed:nil];
    
    NSUInteger  rowBytes= frame.ioSurface.bytesPerRow;
    float*      pixels  = frame.ioSurface.baseAddress;
    for (NSInteger row = 0; row < height; row++)
    {
        float*  nextPixel = (float*)((UInt8*)pixels + (row * rowBytes));
        for (NSInteger col = 0; col < width; col++)
        {
            double  red = *nextPixel;
            nextPixel++;
            double  green = *nextPixel;
            nextPixel++;
            double  blue = *nextPixel;
            nextPixel++;
            nextPixel++; // skip alpha
            
            double luminance = luminanceRed * red + luminanceGreen * green + luminanceBlue * blue;
            averageLuminance += luminance;
        }
    }
    
    [frame.ioSurface unlockWithOptions:kIOSurfaceLockReadOnly
                                  seed:nil];
    
    
    averageLuminance /= (double)width * (double)height;
    
    [analysisLock lock];

    // Add our analysis data to the array
    NSLog (@"Average luminance for frame at time %f = %f", CMTimeGetSeconds(frameTime), averageLuminance);
    analyzedData [ nextAnalyzedFrameNum ].frameTime = frameTime;
    analyzedData [ nextAnalyzedFrameNum ].averageLuminance = averageLuminance;
#if BACKWARDS_ANALYSIS
    nextAnalyzedFrameNum--;
#else
    nextAnalyzedFrameNum++;
#endif // BACKWARDS_ANALYSIS
    
    // Attempt to save partial data. If it fails, don't worry because we'll save it all at the end
    // Also, don't save on every frame, as it slows down the analysis too much. Save every 10th
    // frame instead
    if ((nextAnalyzedFrameNum % 10) == 0)
    {
        if (![self saveAnalyzedData:nil])
        {
            NSLog (@"Unable to save partial analysis data");
        }
    }
    
    [analysisLock unlock];
    
    return YES;
}

```

The example above calls the `-saveAnalyzedData:` function shown below every 10 frames. The function then saves the results into a custom parameter using the [`setCustomParameterValue(_:toParameter:at:)`](../professional_video_applications/fxparametersettingapi_v5/setcustomparametervalue%28_,toparameter,at%29.md) method of [`FxParameterSettingAPI_v5`](../professional_video_applications/fxparametersettingapi_v5.md).

**Swift**:

```swift
    func saveAnalyzedData() throws {
        //let analysisData = Data(bytes: &analyzedData, count: nextAnalyzedFrameNum * MemoryLayout<BrightnessAnalysis>.stride)
        let analysisData = NSData(bytes: analyzedData, length: nextAnalyzedFrameNum * MemoryLayout<BrightnessAnalysis>.stride)
        var paramData: [AnyHashable : Any]? = nil
        if let dictionary = CMTimeCopyAsDictionary(analysisFrameDuration, allocator: kCFAllocatorDefault) as? [AnyHashable : Any] {
            paramData = [
                kKey_FrameDuration : dictionary,
                kKey_AnalysisData : analysisData,
                kKey_NumAnalyzedFrames : NSNumber(value: nextAnalyzedFrameNum - 1)
            ]
        }

        let paramAPI = _apiManager.api(for: FxParameterSettingAPI_v5.self) as! FxParameterSettingAPI_v5?
        
           paramAPI?.setCustomParameterValue(paramData as (NSCopying & NSSecureCoding & NSObjectProtocol)?, toParameter: kParam.analysisData.rawValue, at: CMTime.zero)
    }
```

**Objective-C**:

```objc
- (BOOL)saveAnalyzedData:(NSError**)error
{
    BOOL result = NO;
    NSData* analysisData    = [NSData dataWithBytes:analyzedData
                                             length:totalFramesToAnalyze * sizeof (*analyzedData)];
    NSDictionary*   paramData   = [NSDictionary dictionaryWithObjectsAndKeys:
                                   (NSDictionary*)CMTimeCopyAsDictionary(analysisFrameDuration, kCFAllocatorDefault), kKey_FrameDuration,
                                   analysisData, kKey_AnalysisData,
                                   [NSNumber numberWithInteger:nextAnalyzedFrameNum - 1], kKey_NumAnalyzedFrames,
                                   nil];
    
    result = YES;
    id<FxParameterSettingAPI_v5>    paramAPI    = [_apiManager apiForProtocol:@protocol(FxParameterSettingAPI_v5)];
    if (paramAPI != nil)
    {
        [paramAPI setCustomParameterValue:paramData
                              toParameter:kParam_AnalysisData
                                   atTime:kCMTimeZero];

        result = YES;
    }
    else
    {
        if (error != nil)
        {
            *error = [NSError errorWithDomain:FxPlugErrorDomain
                                         code:kFxError_APIUnavailable
                                     userInfo:@{ NSLocalizedDescriptionKey : @"Unable to retrieve the FxParameterSettingAPI_v5 in -cleanupAnalysis:" }];
        }
    }
    
    return result;
}
```

> 💡 **Tip**:  To cancel analysis, return `NO` and set the error in the [`analyzeFrame(_:at:)`](../professional_video_applications/fxanalyzer/analyzeframe%28_,at%29.md) method.

### Clean up after analysis

Use the [`cleanupAnalysis()`](../professional_video_applications/fxanalyzer/cleanupanalysis%28%29.md) method to do any necessary cleanup after the analysis is complete. The following example is from the `FxBrightnessAnalysis` plug-in.

**Swift**:

```swift
    @objc func cleanupAnalysis() throws {
        // Update our parameters
        analysisLock.lock()
        do {
            try saveAnalyzedData()
            free(analyzedData)
            analyzedData = nil
        }
        analysisLock.unlock()
    }

```

**Objective-C**:

```objc
- (BOOL)cleanupAnalysis:(NSError **)error
{
    // Update our parameters
    BOOL    result  = NO;
    [analysisLock lock];
    {
        [self saveAnalyzedData:error];
        free(analyzedData);
        analyzedData = NULL;
        result = YES;
    }
    [analysisLock unlock];
    
    return result;
}
```

### Determine the Current Analysis State

The `-analysisStateForEffect:` method returns the current analysis state as one of the following keys:

- **[`kFxAnalysisState_NotAnalyzing`](../professional_video_applications/kfxanalysisstate_notanalyzing.md)**: Not analyzing.
- **[`kFxAnalysisState_AnalysisRequested`](../professional_video_applications/kfxanalysisstate_analysisrequested.md)**: Analysis has been requested, but it hasn’t started yet.
- **[`kFxAnalysisState_AnalysisStarted`](../professional_video_applications/kfxanalysisstate_analysisstarted.md)**: Analysis has started.
- **[`kFxAnalysisState_AnalysisCompleted`](../professional_video_applications/kfxanalysisstate_analysiscompleted.md)**: Analysis has completed.
- **[`kFxAnalysisState_AnalysisInterrupted`](../professional_video_applications/kfxanalysisstate_analysisinterrupted.md)**: The analysis was interrupted.

Although not necessary, you can use these states to provide UI feedback, and to determine when the analysis is complete or whether it was interrupted.

### Retrieve analysis data for use in rendering

During rendering, retrieve the analyzed data for each frame from the custom parameter in your [`pluginState(_:at:quality:)`](../professional_video_applications/fxtileableeffect/pluginstate%28_,at,quality%29.md) method. Use [`getCustomParameterValue(_:fromParameter:at:)`](../professional_video_applications/fxparameterretrievalapi_v6/getcustomparametervalue%28_,fromparameter,at%29.md) to get the frame’s value, process a result that your renderer will need, then pack it into the plug-in state for that frame. This example shows how to retrieve the analysis data for use in rendering. The steps that follow take you through the example in more detail.

**Swift**:

```swift
    func pluginState(_ pluginState: AutoreleasingUnsafeMutablePointer<NSData>?, at renderTime: CMTime, quality qualityLevel: UInt) throws {
        let paramAPI = _apiManager!.api(for: FxParameterRetrievalAPI_v6.self) as! FxParameterRetrievalAPI_v6

        var p: (NSCopying & NSSecureCoding & NSObjectProtocol)? = nil
        var brightnessData = BrightnessEqualization(analysisCompleted: false, desiredBrightness: 0.0, actualBrightness: 0.0, frameDuration: CMTime.zero,
                                                    rgbToYCbCr:matrixData(toFlatArray: FxMatrix44().matrix()), YCbCrToRGB:matrixData(toFlatArray: FxMatrix44().matrix()))
        if (p != nil) &&
            (paramAPI.getCustomParameterValue(AutoreleasingUnsafeMutablePointer<(NSCopying & NSSecureCoding & NSObjectProtocol)?>(&p),
                                              fromParameter: kParam.analysisData.rawValue,
                                              at: renderTime)) {
            let analysisData = p as! NSDictionary
        
            let completedAnalysis : Bool = analysisData.allKeys.count > 0
            
            var frameDuration : CMTime = .invalid

            if completedAnalysis {
                let durationDict = ((analysisData.object(forKey: kKey_FrameDuration) ?? 0) as! NSDictionary)
                frameDuration = CMTimeMakeFromDictionary(durationDict)
            }
            
            let numFramesAnalyzed : Int = (analysisData[kKey_NumAnalyzedFrames] as? NSNumber)?.intValue ?? 0
            
            let analyzedParamData = analysisData[kKey_AnalysisData] as? NSData //UnsafeRawBufferPointer
        
            let brightnessAnalysisPtr = analyzedParamData?.bytes
            let brightnessAnalysis = brightnessAnalysisPtr?.bindMemory(to: BrightnessAnalysis.self, capacity: numFramesAnalyzed)
            
            var actualBrightness = 1.0
            
            if completedAnalysis {
                actualBrightness = brightness(at: renderTime, frameDuration: frameDuration, numFrames: numFramesAnalyzed, fromData: brightnessAnalysis)
            }
            
            var desiredBrightness = 1.0
            paramAPI.getFloatValue(&desiredBrightness, fromParameter: kParam.brightness.rawValue, at: renderTime)
            
            let colorAPI = _apiManager!.api(for: FxColorGamutAPI_v2.self) as! FxColorGamutAPI_v2
            
            let rgbToYCbCr = colorAPI.colorMatrixFromDesiredRGBToYCbCr()
            let YCbCrToRGB = colorAPI.colorMatrixFromYCbCrToDesiredRGB()
            
            let rgbToYCbCrData = rgbToYCbCr!.matrix()
            let YCbCrToRGBData = YCbCrToRGB!.matrix()
            brightnessData = BrightnessEqualization (analysisCompleted: completedAnalysis, desiredBrightness: desiredBrightness, actualBrightness: actualBrightness, frameDuration: frameDuration, rgbToYCbCr: matrixData(toFlatArray: rgbToYCbCrData), YCbCrToRGB: matrixData(toFlatArray: YCbCrToRGBData))
        }
        let renderData = NSData(bytes: &brightnessData, length: MemoryLayout<BrightnessEqualization>.stride)
        
        pluginState!.pointee = renderData
    }
```

**Objective-C**:

```objc
- (BOOL)pluginState:(NSData * _Nonnull * _Nullable)pluginState
             atTime:(CMTime)renderTime
            quality:(FxQuality)qualityLevel
              error:(NSError * _Nullable * _Nullable)error {
    id<FxParameterRetrievalAPI_v6>  paramAPI    = [_apiManager apiForProtocol:@protocol(FxParameterRetrievalAPI_v6)];
    if (paramAPI == nil)
    {
        return NO;
    }
    
    NSDictionary* analysisData    = nil;
    [paramAPI getCustomParameterValue:&analysisData
                        fromParameter:kParam_AnalysisData
                               atTime:renderTime];
    BOOL    completedAnalysis = [[analysisData allKeys] count] > 0;
    
    CMTime frameDuration = kCMTimeInvalid;
    if (completedAnalysis)
    {
        frameDuration = CMTimeMakeFromDictionary((CFDictionaryRef)[analysisData objectForKey:kKey_FrameDuration]);
    }
    
    NSInteger   numFramesAnalyzed   = [[analysisData objectForKey:kKey_NumAnalyzedFrames] integerValue];
    
    NSData* analyzedParamData = [analysisData objectForKey:kKey_AnalysisData];
    BrightnessAnalysis* brightnessAnalysis  = (BrightnessAnalysis*)[analyzedParamData bytes];
    double actualBrightness = 1.0;
    if (completedAnalysis)
    {
        actualBrightness = [self brightnessAtTime:renderTime
                                    frameDuration:frameDuration
                                        numFrames:numFramesAnalyzed
                                         fromData:brightnessAnalysis];
    }
    
    double desiredBrightness    = 1.0;
    [paramAPI getFloatValue:&desiredBrightness
              fromParameter:kParam_Brightness
                     atTime:renderTime];

    id<FxColorGamutAPI_v2>  colorAPI    = [_apiManager apiForProtocol:@protocol(FxColorGamutAPI_v2)];
    FxMatrix44* rgbToYCbCr  = [colorAPI colorMatrixFromDesiredRGBToYCbCr];
    FxMatrix44* YCbCrToRGB  = [colorAPI colorMatrixFromYCbCrToDesiredRGB];
    
    Matrix44Data    *rgbToYCbCrData = [rgbToYCbCr matrix];
    Matrix44Data    *YCbCrToRGBData = [YCbCrToRGB matrix];
    struct BrightnessEqualization brightnessData = {
        completedAnalysis,
        desiredBrightness,
        actualBrightness,
        frameDuration,
        [self matrixDataToFlatArray:rgbToYCbCrData],
        [self matrixDataToFlatArray:YCbCrToRGBData]
    };
    
    NSMutableData*  renderData = [NSMutableData dataWithBytes:&brightnessData
                                                       length:sizeof(brightnessData)];
    
    *pluginState = renderData;
    return YES;
}

```

In the above example from the `FxBrightnessAnalysis` plug-in:

1. The `analysisData` for the current frame is retrieved from the custom parameter using [`getCustomParameterValue(_:fromParameter:at:)`](../professional_video_applications/fxparameterretrievalapi_v6/getcustomparametervalue%28_,fromparameter,at%29.md).
2. A pointer to the data is then passed to a function called `brightnessAtTime::::` to determine the analyzed brightness value of the current frame.
3. The `desiredBrightness` value that was set in the `kParam_Brightness` float slider parameter by the user is retrieved.
4. The `actualBrightness` and `desiredBrightness` values are packed into the `brightnessData` struct and returned as `renderData`.

See [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md) for more information on working with `pluginState`.

## See Also

### Time and analysis
- [Understanding time in FxPlug](./understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](./scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxTimingAPI_v4](../professional_video_applications/fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [protocol FxKeyframeAPI_v3](../professional_video_applications/fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [protocol FxAnalysisAPI](../professional_video_applications/fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](../professional_video_applications/fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](../professional_video_applications/fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)*