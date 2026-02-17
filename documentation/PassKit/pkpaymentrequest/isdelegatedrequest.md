# isDelegatedRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether this payment request is being made by a delegated entity on behalf of a merchant.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
var isDelegatedRequest: Bool { get set }
```

#### Discussion

Set this property to YES when your app is acting as an Apple Pay delegate and presenting the payment sheet on behalf of another merchant. The default value is NO.

> **Note**: This property requires your app to be registered as an Apple Pay delegate and to have the com.apple.developer.in-app-payments-delegate entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/isdelegatedrequest)*