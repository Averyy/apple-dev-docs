# isSupported

**Framework**: ProximityReader  
**Kind**: property

A Boolean value that indicates whether this device model supports Tap to Pay on iPhone.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
static let isSupported: Bool
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Discussion

For this property to be `true`, the device model must be iPhone XS or newer. This property doesn’t check the OS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/issupported)*