# PaymentCardReader.UpdateEvent

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

An event you receive during the configuration of the payment system.

**Availability**:
- iOS 15.4+ - Deprecated in 16.0
- iPadOS 15.4+ - Deprecated in 16.0
- Mac Catalyst 17.0+ - Deprecated in 17.0

> **Deprecated**: Use PaymentCardReader.Event

## Declaration

```swift
enum UpdateEvent
```

#### Overview

If the [`prepare(using:updateHandler:)`](./prepare%28using,updatehandler%29.md) must update the device’s configuration, it delivers events to the update handler you provided. Use those events to monitor the status of the update.

## Topics

### Enumeration Cases
- [PaymentCardReader.UpdateEvent.notReady](./updateevent/notready.md)
  A reader that is not ready to perform transactions.
- [PaymentCardReader.UpdateEvent.progress(_:)](./updateevent/progress%28_%29.md)
  The current update progress, specified as an integer value from 1 to 100.
### Instance Properties
- [var name: String](./updateevent/name.md)
  The name of the event.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [let id: String](./id.md)
  A unique identifier for this object.
- [func prepare(using: PaymentCardReader.Token, updateHandler: ((PaymentCardReader.UpdateEvent) -> Void)?) async throws -> PaymentCardReaderSession](./prepare%28using,updatehandler%29.md)
  Configures the pipeline for reading payment or loyalty cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/updateevent)*