# Scheduling media in plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Use the scheduling APIs in FxPlug to retrieve frames from different times.

#### Overview

The FxPlug SDK provides several timing and scheduling methods that give plug-ins a way to get the current time and to schedule media.

##### Get the current time

When an onscreen control or an event in a custom parameter view requires the current time, use the [`currentTime()`](../professional_video_applications/fxcustomparameteractionapi_v4/currenttime%28%29.md) method in the `FxCustomParameterAPI` protocol to get the rational time.

> ❗ **Important**:  All FxPlug 4 APIs represent time using [`CMTime`](../CoreMedia/cmtime.md). If you’re familiar with previous versions of FxPlug, note the move away from `FxTime`. For more information, see [`CMTime`](../CoreMedia/cmtime.md).

##### Schedule media

The scheduling API lets the host applications schedule the media contained in image wells. Consider this method, new to FxPlug 4:

**Swift**:

```swift
optional func scheduleInputs(_ inputImageRequests: AutoreleasingUnsafeMutablePointer<NSArray?>?, withPluginState pluginState: Data?, at renderTime: CMTime) throws
```

**Objective-C**:

```objc
- (BOOL)scheduleInputs:(NSArray<FxImageTileRequest*>* _Nullable *_Nullable)inputImageRequests
       withPluginState:(NSData* _Nullable)pluginState
                atTime:(CMTime)renderTime
                 error:(NSError**)error;
```

This method tells the host application how many frames from the given input sources your plug-in will require in order to render at the given render time. See `PictureInPicturePlugIn.m` in the `FxPictureInPicture` project for an example of how [`scheduleInputs(_:withPluginState:at:)`](../professional_video_applications/fxtileableeffect/scheduleinputs%28_,withpluginstate,at%29.md) can be used with an image well.

## See Also

### Time and analysis
- [Understanding time in FxPlug](./understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [protocol FxTimingAPI_v4](../professional_video_applications/fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [protocol FxKeyframeAPI_v3](../professional_video_applications/fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [Analyzing media](./analyzing-media.md)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI](../professional_video_applications/fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](../professional_video_applications/fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](../professional_video_applications/fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/scheduling-media-in-plug-ins)*