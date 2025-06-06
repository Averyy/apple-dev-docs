# PaymentCardReaderSession.PINToken

**Framework**: ProximityReader  
**Kind**: struct

A secure PIN token that you receive from your participating payment service provider.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct PINToken
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Overview

When the payment card issuer requests the PIN during a transaction, your participating payment service provider must provide this token as part of the response.

## Topics

### Creating a token
- [init(rawValue: String)](paymentcardreadersession/pintoken/init(rawvalue:).md)
  Creates a token with the string your payment service provider gave you.
### Getting the token value
- [let rawValue: String](paymentcardreadersession/pintoken/rawvalue-swift.property.md)
  The raw token string from your payment service provider.
### Type Aliases
- [PaymentCardReaderSession.PINToken.RawValue](paymentcardreadersession/pintoken/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](paymentcardreadersession/pintoken/equatable-implementations.md)
- [RawRepresentable Implementations](paymentcardreadersession/pintoken/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func capturePIN(using: PaymentCardReaderSession.PINToken, cardReaderTransactionID: String) async throws -> PaymentCardReadResult](paymentcardreadersession/capturepin(using:cardreadertransactionid:).md)
  Presents a sheet to capture the PIN when required by the payment card issuer, and returns the previously encrypted card data including newly captured PIN data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/pintoken)*