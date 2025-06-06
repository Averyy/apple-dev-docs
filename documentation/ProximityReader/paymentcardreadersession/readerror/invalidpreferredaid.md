# PaymentCardReaderSession.ReadError.invalidPreferredAID

**Framework**: ProximityReader  
**Kind**: case

The preferred AID specified in the transaction request is invalid.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case invalidPreferredAID
```

#### Discussion

This error occurs when you specify preferred AIDs or RIDs that aren’t between the range of 5 to 16 bytes, or the list has too many entries.

## See Also

- [PaymentCardReaderSession.ReadError.cardReadFailed](paymentcardreadersession/readerror/cardreadfailed.md)
  An error occurred when reading the card.
- [PaymentCardReaderSession.ReadError.invalidAmount](paymentcardreadersession/readerror/invalidamount.md)
  The request contained an invalid amount.
- [PaymentCardReaderSession.ReadError.invalidCurrencyCode](paymentcardreadersession/readerror/invalidcurrencycode.md)
  The request included an invalid currency code.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readerror/invalidpreferredaid)*