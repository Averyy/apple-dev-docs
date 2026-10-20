# cancelVideoZoomRamp()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Smoothly ends a zoom transition in progress.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func cancelVideoZoomRamp()
```

```objc
- (void) cancelVideoZoomRamp;
```

#### Discussion

Calling this method is equivalent to calling [`ramp(toVideoZoomFactor:withRate:)`](./ramp%28tovideozoomfactor,withrate%29.md) with a rate of zero. If a zoom transition is in progress, the transition slows to a stop (instead of stopping abruptly).

Before calling this method, you must call [`lockForConfiguration()`](./lockforconfiguration%28%29.md) to acquire exclusive access to the device’s configuration properties. If you don’t, calling this method raises an exception. When you finish configuring the device, call [`unlockForConfiguration()`](./unlockforconfiguration%28%29.md) to release the lock and allow other devices to configure the settings.

## See Also

### Adjusting zoom
- [var videoZoomFactor: CGFloat](./videozoomfactor.md)
  A value that controls the cropping and enlargement of images captured by the device.
- [func ramp(toVideoZoomFactor: CGFloat, withRate: Float)](./ramp%28tovideozoomfactor,withrate%29.md)
  Begins a smooth transition from the current zoom factor to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/cancelvideozoomramp())*