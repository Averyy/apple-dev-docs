# isLowLightBoostSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLowLightBoostSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLowLightBoostSupported) BOOL lowLightBoostSupported;
```

#### Discussion

You can set the capture device’s [`automaticallyEnablesLowLightBoostWhenAvailable`](./automaticallyenableslowlightboostwhenavailable.md) property only if this property is [`true`](../../Swift/true.md).

This property is key-value observable.

## See Also

### Configuring low light settings
- [var isLowLightBoostEnabled: Bool](./islowlightboostenabled.md)
  A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.
- [var automaticallyEnablesLowLightBoostWhenAvailable: Bool](./automaticallyenableslowlightboostwhenavailable.md)
  A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islowlightboostsupported)*