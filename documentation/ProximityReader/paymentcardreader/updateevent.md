# PaymentCardReader.UpdateEvent

**Framework**: ProximityReader  
**Kind**: enum

An event you receive during the configuration of the payment system.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum UpdateEvent
```

#### Overview

If the [`prepare(using:updateHandler:)`](paymentcardreader/prepare(using:updatehandler:).md) must update the device’s configuration, it delivers events to the update handler you provided. Use those events to monitor the status of the update.

## Topics

### Enumeration Cases
- [PaymentCardReader.UpdateEvent.notReady](paymentcardreader/updateevent/notready.md)
  A reader that is not ready to perform transactions.
- [PaymentCardReader.UpdateEvent.progress(_:)](paymentcardreader/updateevent/progress(_:).md)
  The current update progress, specified as an integer value from 1 to 100.
### Instance Properties
- [var name: String](paymentcardreader/updateevent/name.md)
  The name of the event.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let id: String](paymentcardreader/id.md)
  A unique identifier for this object.
- [func prepare(using: PaymentCardReader.Token, updateHandler: ((PaymentCardReader.UpdateEvent) -> Void)?) async throws -> PaymentCardReaderSession](paymentcardreader/prepare(using:updatehandler:).md)
  Configures the pipeline for reading payment or loyalty cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/updateevent)*