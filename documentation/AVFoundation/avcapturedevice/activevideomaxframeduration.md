# activeVideoMaxFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The currently active maximum frame duration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var activeVideoMaxFrameDuration: CMTime { get set }
```

#### Discussion

A device’s maximum frame duration is the reciprocal of its minimum frame rate. You can set the value of this property to limit the minimum frame rate during a capture session. The capture device automatically chooses a default maximum frame duration based on its active format. After changing the value of this property, you can return to the default maximum frame duration by setting this property’s value to [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid). Choosing a new preset for the capture session also resets this property to its default value.

Attempting to set this property to a value not found in the active format’s [`videoSupportedFrameRateRanges`](avcapturedevice/format/videosupportedframerateranges.md) array raises an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)).

> ❗ **Important**:  Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock.

This property value is key-value observable.

## See Also

- [var activeVideoMinFrameDuration: CMTime](avcapturedevice/activevideominframeduration.md)
  The currently active minimum frame duration.
- [var activeDepthDataMinFrameDuration: CMTime](avcapturedevice/activedepthdataminframeduration.md)
  The minimum frame duration of depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activevideomaxframeduration)*