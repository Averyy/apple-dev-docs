# events

**Framework**: ProximityReader  
**Kind**: property

A stream of events you receive indicating the activities of the payment card reader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
final let events: AsyncStream<PaymentCardReader.Event>
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Discussion

When calling [`prepare(using:)`](paymentcardreader/prepare(using:).md), the [`PaymentCardReader.Event.updateProgress(_:)`](paymentcardreader/event/updateprogress(_:).md) event will indicate the completion percentage of the configuration. When reading cards with [`PaymentCardReaderSession`](paymentcardreadersession.md), the raised events will indicate the current state of the card-reading process.

## See Also

- [PaymentCardReader.Event](paymentcardreader/event.md)
  An event you receive indicating the state or activity of the payment card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/events)*