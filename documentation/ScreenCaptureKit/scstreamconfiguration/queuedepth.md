# queueDepth

**Framework**: ScreenCaptureKit  
**Kind**: property

The maximum number of frames for the queue to store.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var queueDepth: Int { get set }
```

#### Discussion

By default, the system sets the queue depth to its minimum value of three frames. Specifying more frames uses more memory, but may allow you to process frame data without stalling the display stream.

> ❗ **Important**:  Don’t exceed a queue depth of eight frames.

 Don’t exceed a queue depth of eight frames.

## See Also

- [var minimumFrameInterval: CMTime](scstreamconfiguration/minimumframeinterval.md)
  The desired minimum time between frame updates, in seconds.
- [var captureResolution: SCCaptureResolutionType](scstreamconfiguration/captureresolution.md)
  The resolution at which to capture source content.
- [enum SCCaptureResolutionType](sccaptureresolutiontype.md)
  Available resolutions for content capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/queuedepth)*