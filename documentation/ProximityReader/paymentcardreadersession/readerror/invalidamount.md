# PaymentCardReaderSession.ReadError.invalidAmount

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

The request contained an invalid amount.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case invalidAmount
```

## Discussion

This error occurs when you specify a negative amount. All amounts must be positive and contain less than 10 digits.

## See Also

### Getting the error
- [PaymentCardReaderSession.ReadError.cardReadFailed](./cardreadfailed.md)
  An error occurred when reading the card.
- [PaymentCardReaderSession.ReadError.invalidCurrencyCode](./invalidcurrencycode.md)
  The request included an invalid currency code.
- [PaymentCardReaderSession.ReadError.invalidPreferredAID](./invalidpreferredaid.md)
  The preferred AID specified in the transaction request is invalid.
- [PaymentCardReaderSession.ReadError.invalidVASMerchants(_:)](./invalidvasmerchants%28_%29.md)
  The specified list of VAS merchants list is invalid.
- [PaymentCardReaderSession.ReadError.invalidVASRequestParameters(_:)](./invalidvasrequestparameters%28_%29.md)
  The specified VAS parameters are invalid.
- [PaymentCardReaderSession.ReadError.nfcDisabled](./nfcdisabled.md)
  NFC is disabled on the device.
- [PaymentCardReaderSession.ReadError.noReaderSession](./noreadersession.md)
  No reader session available or the session isn’t ready.
- [PaymentCardReaderSession.ReadError.passcodeDisabled](./passcodedisabled.md)
  Read operations aren’t allowed when the device’s passcode is disabled.
- [PaymentCardReaderSession.ReadError.paymentCardDeclined](./paymentcarddeclined.md)
  The payment card declined the transaction.
- [PaymentCardReaderSession.ReadError.paymentReadFailed](./paymentreadfailed.md)
  An internal failure prevented the read operation.
- [PaymentCardReaderSession.ReadError.pinCancelled](./pincancelled.md)
  The current PIN capture was cancelled, also cancelling any ongoing read operation.
- [PaymentCardReaderSession.ReadError.pinNotAllowed](./pinnotallowed.md)
  The time window allowed for a PIN capture after a card read has expired or requesting the PIN is simply not supported by your current configuration.
- [PaymentCardReaderSession.ReadError.pinEntryFailed](./pinentryfailed.md)
  An error occurred when capturing the PIN.
- [PaymentCardReaderSession.ReadError.pinEntryTimeout](./pinentrytimeout.md)
  The current PIN capture was not completed in allowed time.
- [PaymentCardReaderSession.ReadError.pinTokenInvalid](./pintokeninvalid.md)
  An error that indicates an invalid PIN token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readerror/invalidamount)*