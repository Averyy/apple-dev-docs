# activeDepthDataMinFrameDuration

**Framework**: AVFoundation  
**Kind**: property

The minimum frame duration of depth data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var activeDepthDataMinFrameDuration: CMTime { get set }
```

#### Discussion

Use this property to set an upper limit to the frame rate at which the system produces depth data. Lowering the depth data frame rate typically lowers power consumption which increases the time the camera can run before it reaches an elevated system pressure state. Setting a value outside the active depth data format’s supported frame rate range produces an exception.

Setting this property to [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) resets it to the active depth data format’s default minimum frame duration. Setting this property to [`positiveInfinity`](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity) results in a depth data frame rate of `0`.

This value gets reset whenever either the active video format or the active depth data format changes.

> ❗ **Important**:  Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock.

 Before changing the value of this property, you must call [`lockForConfiguration()`](avcapturedevice/lockforconfiguration().md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](avcapturedevice/unlockforconfiguration().md) to release the lock.

## See Also

- [var activeVideoMinFrameDuration: CMTime](avcapturedevice/activevideominframeduration.md)
  The currently active minimum frame duration.
- [var activeVideoMaxFrameDuration: CMTime](avcapturedevice/activevideomaxframeduration.md)
  The currently active maximum frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activedepthdataminframeduration)*