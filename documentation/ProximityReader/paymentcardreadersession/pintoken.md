# PaymentCardReaderSession.PINToken

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

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

- [Adding support for Tap to Pay on iPhone to your app](../adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Overview

When the payment card issuer requests the PIN during a transaction, your participating payment service provider must provide this token as part of the response.

## Topics

### Creating a token
- [init(rawValue: String)](./pintoken/init%28rawvalue%29.md)
  Creates a token with the string your payment service provider gave you.
### Getting the token value
- [let rawValue: String](./pintoken/rawvalue.md)
  The raw token string from your payment service provider.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting the PIN
- [func capturePIN(using: PaymentCardReaderSession.PINToken, cardReaderTransactionID: String) async throws -> PaymentCardReadResult](./capturepin%28using,cardreadertransactionid%29.md)
  Presents a sheet to capture the PIN when required by the payment card issuer, and returns the previously encrypted card data including newly captured PIN data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/pintoken)*