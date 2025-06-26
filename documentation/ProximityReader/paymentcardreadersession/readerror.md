# PaymentCardReaderSession.ReadError

**Framework**: ProximityReader  
**Kind**: enum

Errors that can occur during a card read.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ReadError
```

## Mentions

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)
- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

## Topics

### Getting the error
- [PaymentCardReaderSession.ReadError.cardReadFailed](paymentcardreadersession/readerror/cardreadfailed.md)
  An error occurred when reading the card.
- [PaymentCardReaderSession.ReadError.invalidAmount](paymentcardreadersession/readerror/invalidamount.md)
  The request contained an invalid amount.
- [PaymentCardReaderSession.ReadError.invalidCurrencyCode](paymentcardreadersession/readerror/invalidcurrencycode.md)
  The request included an invalid currency code.
- [PaymentCardReaderSession.ReadError.invalidPreferredAID](paymentcardreadersession/readerror/invalidpreferredaid.md)
  The preferred AID specified in the transaction request is invalid.
- [PaymentCardReaderSession.ReadError.invalidVASMerchants(_:)](paymentcardreadersession/readerror/invalidvasmerchants(_:).md)
  The specified list of VAS merchants list is invalid.
- [PaymentCardReaderSession.ReadError.invalidVASRequestParameters(_:)](paymentcardreadersession/readerror/invalidvasrequestparameters(_:).md)
  The specified VAS parameters are invalid.
- [PaymentCardReaderSession.ReadError.nfcDisabled](paymentcardreadersession/readerror/nfcdisabled.md)
  NFC is disabled on the device.
- [PaymentCardReaderSession.ReadError.noReaderSession](paymentcardreadersession/readerror/noreadersession.md)
  No reader session available or the session isn’t ready.
- [PaymentCardReaderSession.ReadError.passcodeDisabled](paymentcardreadersession/readerror/passcodedisabled.md)
  Read operations aren’t allowed when the device’s passcode is disabled.
- [PaymentCardReaderSession.ReadError.paymentCardDeclined](paymentcardreadersession/readerror/paymentcarddeclined.md)
  The payment card declined the transaction.
- [PaymentCardReaderSession.ReadError.paymentReadFailed](paymentcardreadersession/readerror/paymentreadfailed.md)
  An internal failure prevented the read operation.
- [PaymentCardReaderSession.ReadError.pinCancelled](paymentcardreadersession/readerror/pincancelled.md)
  The current PIN capture was cancelled, also cancelling any ongoing read operation.
- [PaymentCardReaderSession.ReadError.pinNotAllowed](paymentcardreadersession/readerror/pinnotallowed.md)
  The time window allowed for a PIN capture after a card read has expired or requesting the PIN is simply not supported by your current configuration.
- [PaymentCardReaderSession.ReadError.pinEntryFailed](paymentcardreadersession/readerror/pinentryfailed.md)
  An error occurred when capturing the PIN.
- [PaymentCardReaderSession.ReadError.pinEntryTimeout](paymentcardreadersession/readerror/pinentrytimeout.md)
  The current PIN capture was not completed in allowed time.
- [PaymentCardReaderSession.ReadError.pinTokenInvalid](paymentcardreadersession/readerror/pintokeninvalid.md)
  An error that indicates an invalid PIN token.
- [PaymentCardReaderSession.ReadError.readCancelled](paymentcardreadersession/readerror/readcancelled.md)
  The current read operation was cancelled.
- [PaymentCardReaderSession.ReadError.readFromBackgroundError](paymentcardreadersession/readerror/readfrombackgrounderror.md)
  Read operations aren’t allowed when an app is in the background state.
- [PaymentCardReaderSession.ReadError.readNotAllowed](paymentcardreadersession/readerror/readnotallowed.md)
  The read operation isn’t allowed at this time.
- [PaymentCardReaderSession.ReadError.readNotAllowedDuringCall](paymentcardreadersession/readerror/readnotallowedduringcall.md)
  Read operations aren’t allowed during a phone call.
- [PaymentCardReaderSession.ReadError.readerServiceConnectionError](paymentcardreadersession/readerror/readerserviceconnectionerror.md)
  The session wasn’t able to connect the system UI or other services.
- [PaymentCardReaderSession.ReadError.readerServiceError](paymentcardreadersession/readerror/readerserviceerror.md)
  A general reader service internal state issue occurred.
- [PaymentCardReaderSession.ReadError.readerSessionAuthenticationError](paymentcardreadersession/readerror/readersessionauthenticationerror.md)
  An authentication error occurred while refreshing the reader session.
- [PaymentCardReaderSession.ReadError.readerSessionBusy](paymentcardreadersession/readerror/readersessionbusy.md)
  The reader is busy with another session.
- [PaymentCardReaderSession.ReadError.readerSessionExpired](paymentcardreadersession/readerror/readersessionexpired.md)
  The reader session expired and couldn’t refresh due to other state changes.
- [PaymentCardReaderSession.ReadError.readerSessionNetworkError](paymentcardreadersession/readerror/readersessionnetworkerror.md)
  A network error occurred that prevented a reader session refresh.
- [PaymentCardReaderSession.ReadError.readerTokenExpired](paymentcardreadersession/readerror/readertokenexpired.md)
  The configuration token for the reader session expired.
- [PaymentCardReaderSession.ReadError.vasReadFail](paymentcardreadersession/readerror/vasreadfail.md)
  An error occurred when reading a loyalty pass.
### Describing the error
- [var errorDescription: String](paymentcardreadersession/readerror/errordescription.md)
  A description of the error in plain text.
- [var errorName: String](paymentcardreadersession/readerror/errorname.md)
### Enumeration Cases
- [PaymentCardReaderSession.ReadError.storeAndForwardDeclineFailed](paymentcardreadersession/readerror/storeandforwarddeclinefailed.md)
  Decline request was made after the allowance time window.
- [PaymentCardReaderSession.ReadError.storeAndForwardResultNotFound](paymentcardreadersession/readerror/storeandforwardresultnotfound.md)
  Decline request failed because the framework can’t find the read result.
- [PaymentCardReaderSession.ReadError.unknown(code:)](paymentcardreadersession/readerror/unknown(code:).md)
  An unexpected error happened, try again.
### Default Implementations
- [Error Implementations](paymentcardreadersession/readerror/error-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readerror)*