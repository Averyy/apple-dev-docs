# PaymentCardReader

**Framework**: ProximityReader  
**Kind**: class

An object you use to configure Tap to Pay on iPhone on the current device.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
class PaymentCardReader
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Overview

A `PaymentCardReader` object coordinates the reading of payment and loyalty cards using existing iPhone hardware. Use it to read cards that might otherwise require specialized hardware. For example, use it to collect contactless payment information from another iPhone or from NFC-enabled hardware, such as NFC-enabled plastic cards.

After you create the `PaymentCardReader` object, call [`prepare(using:)`](paymentcardreader/prepare(using:).md) to validate the payment pipeline and receive a new [`PaymentCardReaderSession`](paymentcardreadersession.md). Use the session object to read card information related to payments and refunds, or to verify card information.

## Topics

### Creating a payment reader
- [init(options: PaymentCardReader.Options)](paymentcardreader/init(options:).md)
  Creates a payment card reader with the specified options.
- [PaymentCardReader.Options](paymentcardreader/options-swift.struct.md)
  Additional information you use to configure a payment card reader.
### Getting the feature availability
- [static let isSupported: Bool](paymentcardreader/issupported.md)
  A Boolean value that indicates whether this device model supports Tap to Pay on iPhone.
### Configuring Tap to Pay on iPhone
- [func prepare(using: PaymentCardReader.Token) async throws -> PaymentCardReaderSession](paymentcardreader/prepare(using:).md)
  Configures the pipeline for reading payment or loyalty cards.
### Displaying the Tap to Pay on iPhone’s terms and conditions
- [func isAccountLinked(using: PaymentCardReader.Token) async throws -> Bool](paymentcardreader/isaccountlinked(using:).md)
  A Boolean value that indicates whether the account is already linked.
- [func linkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/linkaccount(using:).md)
  Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.
- [func relinkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/relinkaccount(using:).md)
  Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.
- [PaymentCardReader.Token](paymentcardreader/token.md)
  A secure token that you receive from your participating payment service provider.
### Observing reader events
- [let events: AsyncStream<PaymentCardReader.Event>](paymentcardreader/events.md)
  A stream of events you receive indicating the activities of the payment card reader.
- [PaymentCardReader.Event](paymentcardreader/event.md)
  An event you receive indicating the state or activity of the payment card reader.
### Getting the configuration details
- [var readerIdentifier: String](paymentcardreader/readeridentifier.md)
  The unique identifier for this card reader.
- [let options: PaymentCardReader.Options](paymentcardreader/options-swift.property.md)
  The defined configuration settings when the reader was created.
### Deprecated
- [let id: String](paymentcardreader/id.md)
  A unique identifier for this object.
- [func prepare(using: PaymentCardReader.Token, updateHandler: ((PaymentCardReader.UpdateEvent) -> Void)?) async throws -> PaymentCardReaderSession](paymentcardreader/prepare(using:updatehandler:).md)
  Configures the pipeline for reading payment or loyalty cards.
- [PaymentCardReader.UpdateEvent](paymentcardreader/updateevent.md)
  An event you receive during the configuration of the payment system.
### Instance Methods
- [func fetchPaymentCardReaderStore() throws -> PaymentCardReaderStore](paymentcardreader/fetchpaymentcardreaderstore.md)
  Returns a store containing the read results the framework obtained using a Store and Forward session.
- [func prepareStoreAndForward() async throws -> StoreAndForwardPaymentCardReaderSession](paymentcardreader/preparestoreandforward.md)
  Configures the pipeline for reading payment or loyalty cards in Store and Forward mode.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Setting up Tap to Pay on iPhone](setting-up-the-entitlement-for-tap-to-pay-on-iphone.md)
  Request and configure the required entitlement to support Tap to Pay on iPhone.
- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
  Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- [class PaymentCardReaderSession](paymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader)*