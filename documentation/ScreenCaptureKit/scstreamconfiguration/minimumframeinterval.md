# minimumFrameInterval

**Framework**: ScreenCaptureKit  
**Kind**: property

The desired minimum time between frame updates, in seconds.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var minimumFrameInterval: CMTime { get set }
```

#### Discussion

Use this value to throttle the rate at which you receive updates. The default value is `0`, which indicates that the system uses the maximum supported frame rate.

You specify the minimum frame interval as the reciprocal of the maximum frame rate. For example, to configure the stream to capture at 60 fps, specify a minimum frame interval equal to `1/60`.

```swift
let config = SCStreamConfiguration()
config.minimumFrameInterval = CMTime(value: 1, timescale: CMTimeScale(60))
```

## See Also

- [var queueDepth: Int](scstreamconfiguration/queuedepth.md)
  The maximum number of frames for the queue to store.
- [var captureResolution: SCCaptureResolutionType](scstreamconfiguration/captureresolution.md)
  The resolution at which to capture source content.
- [enum SCCaptureResolutionType](sccaptureresolutiontype.md)
  Available resolutions for content capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/minimumframeinterval)*