# PaymentCardReaderSession

**Framework**: ProximityReader  
**Kind**: class

The object you use to start reading a contactless payment or loyalty card.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
class PaymentCardReaderSession
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Overview

Use a `PaymentCardReaderSession` object to read payment and loyalty cards from a properly configured device. You don’t create this object directly. Instead, you obtain one by calling the [`prepare(using:)`](paymentcardreader/prepare(using:).md) method of your [`PaymentCardReader`](paymentcardreader.md) object, which returns a session after the successful configuration of the device.

Maintain a strong reference to a session object for the duration of the card-reading process. You may use the same session object to perform multiple read operations, but you may perform only one read operation at a time from the device.

## Topics

### Reading a payment card
- [func readPaymentCard(PaymentCardTransactionRequest) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:)-8jol5.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardVerificationRequest) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:)-hr97.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
### Reading a loyalty card
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool) async throws -> (PaymentCardReadResult?, VASReadResult?)](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest) async throws -> VASReadResult](paymentcardreadersession/readvas(_:).md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
### Requesting the PIN
- [func capturePIN(using: PaymentCardReaderSession.PINToken, cardReaderTransactionID: String) async throws -> PaymentCardReadResult](paymentcardreadersession/capturepin(using:cardreadertransactionid:).md)
  Presents a sheet to capture the PIN when required by the payment card issuer, and returns the previously encrypted card data including newly captured PIN data.
- [PaymentCardReaderSession.PINToken](paymentcardreadersession/pintoken.md)
  A secure PIN token that you receive from your participating payment service provider.
### Canceling the reading process
- [func cancelRead() async throws -> Bool](paymentcardreadersession/cancelread.md)
  Dismiss the sheet that prompts someone to present their card for reading.
### Getting error information
- [PaymentCardReaderSession.ReadError](paymentcardreadersession/readerror.md)
  Errors that can occur during a card read.
### Deprecated
- [func readPaymentCard(PaymentCardTransactionRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-2zgwn.md)
  Presents a sheet to read a contactless payment card for a purchase or a refund, and returns the encrypted card data.
- [func readPaymentCard(PaymentCardVerificationRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> PaymentCardReadResult](paymentcardreadersession/readpaymentcard(_:eventhandler:)-20e1w.md)
  Presents a sheet to verify a contactless payment card, and returns the card data.
- [func readPaymentCard(PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> (PaymentCardReadResult?, VASReadResult?)](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:eventhandler:).md)
  Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.
- [func readVAS(VASRequest, eventHandler: ((PaymentCardReaderSession.Event) -> Void)?) async throws -> VASReadResult](paymentcardreadersession/readvas(_:eventhandler:).md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.
- [let id: String](paymentcardreadersession/id.md)
  A unique identifier for this object.
- [PaymentCardReaderSession.Event](paymentcardreadersession/event.md)
  Optional events you can observe during the card-reading process.
### Instance Properties
- [let currentOSVersionDeprecationDate: Date?](paymentcardreadersession/currentosversiondeprecationdate.md)
  The date when current OS version will be deprecated.

## Relationships

### Inherited By
- [StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Setting up Tap to Pay on iPhone](setting-up-the-entitlement-for-tap-to-pay-on-iphone.md)
  Request and configure the required entitlement to support Tap to Pay on iPhone.
- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
  Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- [class PaymentCardReader](paymentcardreader.md)
  An object you use to configure Tap to Pay on iPhone on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession)*