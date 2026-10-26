# Communicating with the plug-in state

**Framework**: Professional-Video-Applications  
**Role**: Article

Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.

#### Overview

One of the biggest changes between FxPlug 3 and 4 is that now there is no FxPlug API access at render time. Rendering occurs out-of-process, reducing the amount of back and forth between the host app and the plug-in, which is essential for performance. Thus, if you call [`FxParameterRetrievalAPI_v6`](../professional_video_applications/fxparameterretrievalapi_v6.md) at render time, it will return *nil*.

This means that your plug-in must prepare what it needs to know to render before render time. Then, at render time, this information is provided to your plug-in. This information is called the *Plug-in State*. It’s represented by a byte-buffer of [`NSData`](../Foundation/nsdata.md) of your own creation that can be passed to the rendering method at render time. The content of the `NSData` object is up to you, but it typically contains parameter values from the host application’s UI, or values calculated from those parameter values.

##### Prepare the plug-in state

Here, your plug-in can query parameter values, and store the required information in an NSData object as you see fit. In the `FxBrightness` example, a struct of values is filled in with plug-in parameter values and ultimately combined into an `NSData` object like this:

**Swift**:

```swift
func pluginState(_ pluginState: AutoreleasingUnsafeMutablePointer<NSData>?, at renderTime: CMTime, quality qualityLevel: UInt) throws {
    let paramAPI = _apiManager!.api(for: FxParameterRetrievalAPI_v6.self) as! FxParameterRetrievalAPI_v6
        
    var brightness = 1.0
    paramAPI.getFloatValue(UnsafeMutablePointer<Double>(&brightness), fromParameter: 1, at: renderTime)
        
    pluginState?.pointee = NSData.init(bytes: &brightness, length: MemoryLayout.size(ofValue: brightness))
}
```

**Objective-C**:

```objc
- (BOOL)pluginState:(NSData**)pluginState
             atTime:(CMTime)renderTime
            quality:(FxQuality)qualityLevel
              error:(NSError**)error
{
    BOOL    succeeded = NO;
    id<FxParameterRetrievalAPI_v6>  paramGetAPI = [_apiManager apiForProtocol:@protocol(FxParameterRetrievalAPI_v6)];
    if (paramGetAPI != nil)
    {
        double  brightness  = 1.0;
        [paramGetAPI getFloatValue:&brightness
                     fromParameter:1
                            atTime:renderTime];
        
        *pluginState = [NSData dataWithBytes:&brightness
                                      length:sizeof(brightness)];
        
        if (*pluginState != nil)
        {
            succeeded = YES;
        }
    }
    else
    {
        *error = [NSError errorWithDomain:FxPlugErrorDomain
                                     code:kFxError_ThirdPartyDeveloperStart + 20
                                 userInfo:@{
                                            NSLocalizedDescriptionKey :
                                                @"Unable to retrieve FxParameterRetrievalAPI_v6 in \
                                                [-TileableRemoteBrightness pluginStateAtTime:]" }];
    }
    
    return succeeded;
}
```

When it’s time to render, your `NSData` is handed back to you, at which point you can unpack the data, like this:

**Swift**:

```swift
let brightness  = pluginState!.withUnsafeBytes { (ptr: UnsafePointer<Double>) -> Double in
        return ptr.pointee
}
```

**Objective-C**:

```objc
double  brightness = 0.0;
[pluginState getBytes:&brightness
               length:sizeof(brightness)];
```

## See Also

### Rendering
- [Rendering in FxPlug](./rendering-in-fxplug.md)
  Use Metal or other frameworks to render images with your FxPlug plug-in.
- [Working with tiled images](./working-with-tiled-images.md)
  Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.
- [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md)
  Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.
- [protocol FxTileableEffect](../professional_video_applications/fxtileableeffect.md)
  The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/communicating-with-the-plug-in-state)*