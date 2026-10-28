# isPortraitEffectActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Portrait video effect is active on a device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var isPortraitEffectActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPortraitEffectActive) BOOL portraitEffectActive;
```

## Discussion

When active, the device blurs the background, simulating a shallow depth of field effect. The device also limits the values of its [`activeVideoMinFrameDuration`](./activevideominframeduration.md) and [`activeVideoMaxFrameDuration`](./activevideomaxframeduration.md) to the value that the device format’s [`videoFrameRateRangeForPortraitEffect`](./format/videoframeraterangeforportraiteffect.md) specifies.

When a capture device’s [`isPortraitEffectEnabled`](./isportraiteffectenabled.md) property value is [`true`](../../Swift/true.md), it may also return [`true`](../../Swift/true.md) for this property, depending on whether it supports the feature in its current configuration.

This property is key-value observable.

## See Also

### Inspecting the Portrait Effect settings
- [class var isPortraitEffectEnabled: Bool](./isportraiteffectenabled.md)
  A Boolean value that indicates whether the user enabled the Portrait video effect in Control Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isportraiteffectactive)*