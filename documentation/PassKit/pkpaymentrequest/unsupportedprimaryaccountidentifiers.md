# unsupportedPrimaryAccountIdentifiers

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An array of Apple Pay cards to exclude from payment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var unsupportedPrimaryAccountIdentifiers: [String] { get set }
```

#### Discussion

Use this property to exclude Apple Pay cards you’ve issued from being used as a payment option by adding the [`primaryAccountIdentifier`](pksecureelementpass/primaryaccountidentifier.md) of the cards you want disallowed. For example, if a person is topping up a stored value card, you can exclude the Apple Pay card being topped up from the payment options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/unsupportedprimaryaccountidentifiers)*