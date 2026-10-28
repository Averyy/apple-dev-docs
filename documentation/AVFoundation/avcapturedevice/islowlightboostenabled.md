# isLowLightBoostEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLowLightBoostEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLowLightBoostEnabled) BOOL lowLightBoostEnabled;
```

## Discussion

The value of this property indicates whether the capture device currently enhancing images to improve quality due to low light conditions. When this property is [`true`](../../Swift/true.md), the capture device has switched into a special mode in which it perceives more light in images.

This property is key-value observable.

## See Also

### Configuring low light settings
- [var isLowLightBoostSupported: Bool](./islowlightboostsupported.md)
  A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.
- [var automaticallyEnablesLowLightBoostWhenAvailable: Bool](./automaticallyenableslowlightboostwhenavailable.md)
  A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/islowlightboostenabled)*