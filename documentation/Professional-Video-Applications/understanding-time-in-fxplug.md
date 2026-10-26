# Understanding time in FxPlug

**Framework**: Professional-Video-Applications  
**Role**: Article

Learn about time handling in host apps and plug-ins.

#### Overview

FxPlug 4 uses rational time of [`CMTime`](../CoreMedia/cmtime.md) type to handle all timing in the host apps and plug-ins. Time can be in the form of a specific time or duration in an effect, object, or timeline (project). When FxPlug methods use `time` or `renderTime`, that time generally refers to the current time that the host is providing or requesting. [`FxTimingAPI_v4`](../professional_video_applications/fxtimingapi_v4.md) provides methods to access other time values available in the host app. For FxPlug methods that don’t provide time, you can use [`FxCustomParameterActionAPI_v4`](../professional_video_applications/fxcustomparameteractionapi_v4.md)’s  [`currentTime()`](../professional_video_applications/fxcustomparameteractionapi_v4/currenttime%28%29.md) to determine current playhead time in the project.

##### Time in Motion

In Motion projects, timelines always start at zero, regardless of the custom timecode the user may set in the project’s properties. Input time is also always relative to the timeline start time. Other times of significance are indicated in the following figure.

![Screenshot of a Motion timeline showing a variety of times, ranging from Zero Timeline time on the left to Maximum Timline Time on the right.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3695370@2x.png)

##### Time in Final Cut Pro

In Final Cut Pro, projects can start at any timecode set by the user, and their timeline time will be continuous from that start time. Timeline time is independent of Input Time in Final Cut Pro, so [`FxTimingAPI_v4`](../professional_video_applications/fxtimingapi_v4.md) provides two convenience methods to convert between them: [`timelineTime(_:fromInputTime:)`](../professional_video_applications/fxtimingapi_v4/timelinetime%28_,frominputtime%29.md) and [`inputTime(_:fromTimelineTime:)`](../professional_video_applications/fxtimingapi_v4/inputtime%28_,fromtimelinetime%29.md). The following figure shows various times in the FxTiming API.

![Screenshot showing the Final Cut Pro timeline with a variety of times labeled, from Timeline Start Set by User on the left to Current Input Time on the right.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3695369@2x.png)

> **Note**:  Although the timeline’s start time is set by the user, the timecode of the timeline will not necessarily correspond to the rational time your plug-in uses. This difference may be due to drop-frame timecode, or because the timecode resets to `00:00:00:00`. For example, if the user sets the project start timecode to `23:59:50:00`, the rational start time of the timeline when converted to seconds may be `86476.39` seconds, but will NOT reset to `0` seconds when the timeline’s timecode reaches `00:00:00:00`.

##### Motion effect templates

You must [apply FxPlug plug-ins to a Motion template](https://support.apple.com/guide/motion/intro-to-final-cut-pro-templates-motn17691fe6/mac) to use it in a Final Cut Pro project. You may notice significant differences in how [`startTime(forEffect:)`](../professional_video_applications/fxtimingapi_v4/starttime%28foreffect%29.md), [`durationTime(forEffect:)`](../professional_video_applications/fxtimingapi_v4/durationtime%28foreffect%29.md), and [`startTimeOfInput(toFilter:)`](../professional_video_applications/fxtimingapi_v4/starttimeofinput%28tofilter%29.md) return time values. To understand these differences, imagine that an effect template added to a clip in Final Cut Pro is equivalent to a complete timeline in Motion. For example, in Motion, [`startTime(forEffect:)`](../professional_video_applications/fxtimingapi_v4/starttime%28foreffect%29.md) will return the plug-in effect’s start time relative to the Motion timeline. In Final Cut Pro, the same method will return the start time of the plug-in effect, relative to the native start time of the clip to which the user applies the template, regardless of the how much of the clip’s head has been trimmed by the user.

##### Retiming and frame duration

Effect templates that you apply to clips or other objects in Final Cut Pro may stretch to match the duration of the clip. When clips with effect templates are retimed by the user in Final Cut Pro, the effect template will adjust proportionally.

Unlike in Motion, [`frameDuration(_:)`](../professional_video_applications/fxtimingapi_v4/frameduration%28_%29.md) and [`sampleDuration(_:)`](../professional_video_applications/fxtimingapi_v4/sampleduration%28_%29.md) always return the native frame or sample durations of the clip, regardless of how fast or slow you retime it. If your plug-in attempts to determine the frame duration or frames per second of the timeline, then use [`timelineFpsNumerator(for:)`](../professional_video_applications/fxtimingapi_v4/timelinefpsnumerator%28for%29.md) and [`timelineFpsDenominator(for:)`](../professional_video_applications/fxtimingapi_v4/timelinefpsdenominator%28for%29.md) to make that calculation, as shown in the example below.

**Swift**:

```swift
let timingAPI = _apiManager!.api(for: FxTimingAPI_v4.self) as! FxTimingAPI_v4
var timelineFrameDuration = CMTimeMake(value: Int64(timingAPI.timelineFpsDenominator(for: self)),
                                           timescale: Int32(timingAPI.timelineFpsNumerator(for: self)))
```

**Objective-C**:

```objc
id<FxTimingAPI_v4> timingAPI = [_apiManager apiForProtocol:@protocol(FxTimingAPI_v4)];
CMTime timelineFrameDuration = kCMTimeZero;
timelineFrameDuration = CMTimeMake( [timingAPI timelineFpsDenominatorForEffect:self],
                                    (int)[timingAPI timelineFpsNumeratorForEffect:self] );
```

## See Also

### Time and analysis
- [Scheduling media in plug-ins](./scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug)*