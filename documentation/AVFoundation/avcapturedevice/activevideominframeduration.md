# activeVideoMinFrameDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The currently active minimum frame duration.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var activeVideoMinFrameDuration: CMTime { get set }
```

```objc
@property (nonatomic) CMTime activeVideoMinFrameDuration;
```

## Discussion

A device’s minimum frame duration is the reciprocal of its maximum frame rate. You can set the value of this property to limit the maximum frame rate during a capture session. The capture device automatically chooses a default minimum frame duration based on its active format. After changing the value of this property, you can return to the default minimum frame duration by setting this property’s value to [`invalid`](../../CoreMedia/cmtime/invalid.md). Choosing a new preset for the capture session also resets this property to its default value.

Attempting to set this property to a value not found in the active format’s [`videoSupportedFrameRateRanges`](./format/videosupportedframerateranges.md) array raises an exception ([`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md)).

> ❗ **Important**:  Before changing the value of this property, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock.

This property value is key-value observable.

## See Also

### Configuring frame durations
- [var activeVideoMaxFrameDuration: CMTime](./activevideomaxframeduration.md)
  The currently active maximum frame duration.
- [var activeDepthDataMinFrameDuration: CMTime](./activedepthdataminframeduration.md)
  The minimum frame duration of depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activevideominframeduration)*