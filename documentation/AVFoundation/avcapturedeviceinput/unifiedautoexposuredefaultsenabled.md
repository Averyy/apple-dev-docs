# unifiedAutoExposureDefaultsEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the input enables unified auto-exposure defaults.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var unifiedAutoExposureDefaultsEnabled: Bool { get set }
```

#### Discussion

You may set the value of a capture device’s [`activeFormat`](avcapturedevice/activeformat.md) in two ways:

1. Set it directly using one of the formats in the device’s [`formats`](avcapturedevice/formats.md) property.
2. The capture session sets it on your behalf when you set its [`sessionPreset`](avcapturesession/sessionpreset.md) property.

Depending on the device and format, you may configure the default auto exposure behavior differently when you use one method or the other, resulting in non-uniform auto exposure behavior. Auto exposure defaults include [`minFrameRate`](avframeraterange/minframerate.md), [`maxFrameRate`](avframeraterange/maxframerate.md), and [`maxExposureDuration`](avcapturedevice/format/maxexposureduration.md). You can set this property to [`true`](https://developer.apple.com/documentation/swift/true) to ensure that the system applies consistent default behaviors to the device regardless of the way you set the active format.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  Manually setting the device’s [`minFrameRate`](avframeraterange/minframerate.md), [`maxFrameRate`](avframeraterange/maxframerate.md), or [`maxExposureDuration`](avcapturedevice/format/maxexposureduration.md) overrides the device defaults, even if you set this property to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var videoMinFrameDurationOverride: CMTime](avcapturedeviceinput/videominframedurationoverride.md)
  A time value that acts as a modifier to a capture device’s active video minimum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/unifiedautoexposuredefaultsenabled)*