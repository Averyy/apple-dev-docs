# SCCaptureResolutionType

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

Available resolutions for content capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
enum SCCaptureResolutionType
```

```c
enum SCCaptureResolutionType : NSInteger;
```

## Overview

Higher-resolution values produce better and more accurate-looking content to the source, at the expense of bandwidth.

## Topics

### Resolutions
- [SCCaptureResolutionType.automatic](./sccaptureresolutiontype/automatic.md)
  Allow ScreenCaptureKit to automatically select the quality of content depending on factors such as network connection.
- [SCCaptureResolutionType.best](./sccaptureresolutiontype/best.md)
  Capture streaming content at the best available resolution.
- [SCCaptureResolutionType.nominal](./sccaptureresolutiontype/nominal.md)
  Capture streaming content with a one point to one pixel conversion factor.
### Initializers
- [init?(rawValue: Int)](./sccaptureresolutiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring captured frames
- [var queueDepth: Int](./scstreamconfiguration/queuedepth.md)
  The maximum number of frames for the queue to store.
- [var minimumFrameInterval: CMTime](./scstreamconfiguration/minimumframeinterval.md)
  The desired minimum time between frame updates, in seconds.
- [var captureResolution: SCCaptureResolutionType](./scstreamconfiguration/captureresolution.md)
  The resolution at which to capture source content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccaptureresolutiontype)*