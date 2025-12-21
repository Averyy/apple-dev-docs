# VASReadResult

**Framework**: ProximityReader  
**Kind**: struct

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

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Overview

A `VASReadResult` object contains the encrypted loyalty card information from the customer. Typically, you receive this object only after calling the [`readVAS(_:)`](paymentcardreadersession/readvas(_:).md) or [`readPaymentCard(_:vasRequest:stopOnVASResult:)`](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md) method of [`PaymentCardReaderSession`](paymentcardreadersession.md).

## Topics

### Creating a read result structure
- [init(id: String, entries: [VASReadResult.ReadEntry])](vasreadresult/init(id:entries:).md)
  Creates a new result object with the specified identifier and customer entries.
### Getting the entry details
- [let entries: [VASReadResult.ReadEntry]](vasreadresult/entries.md)
  The list of loyalty reward card entries received from the customer.
- [VASReadResult.ReadEntry](vasreadresult/readentry.md)
  An object containing encrypted data associated with a customer’s loyalty or reward pass.
### Getting the result ID
- [let id: String](vasreadresult/id.md)
  A unique identifier string for the requested read operation.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)
  Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- [class VASRequest](vasrequest.md)
  A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasreadresult)*