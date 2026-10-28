# VASReadResult

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

The result of a request to read loyalty card information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct VASReadResult
```

## Mentions

- [Accepting loyalty passes from Wallet](./accepting-loyalty-passes-from-wallet.md)

## Overview

A `VASReadResult` object contains the encrypted loyalty card information from the customer. Typically, you receive this object only after calling the [`readVAS(_:)`](./paymentcardreadersession/readvas%28_%29.md) or [`readPaymentCard(_:vasRequest:stopOnVASResult:)`](./paymentcardreadersession/readpaymentcard%28_,vasrequest,stoponvasresult%29.md) method of [`PaymentCardReaderSession`](./paymentcardreadersession.md).

## Topics

### Creating a read result structure
- [init(id: String, entries: [VASReadResult.ReadEntry])](./vasreadresult/init%28id,entries%29.md)
  Creates a new result object with the specified identifier and customer entries.
### Getting the entry details
- [let entries: [VASReadResult.ReadEntry]](./vasreadresult/entries.md)
  The list of loyalty reward card entries received from the customer.
- [VASReadResult.ReadEntry](./vasreadresult/readentry.md)
  An object containing encrypted data associated with a customer’s loyalty or reward pass.
### Getting the result ID
- [let id: String](./vasreadresult/id.md)
  A unique identifier string for the requested read operation.

## Relationships

### Conforms To
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Loyalty card requests
- [Accepting loyalty passes from Wallet](./accepting-loyalty-passes-from-wallet.md)
  Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- [class VASRequest](./vasrequest.md)
  A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasreadresult)*