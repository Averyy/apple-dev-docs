# messages

**Framework**: StoreKit  
**Kind**: property

The asynchronous sequence that sends a message when the App Store creates it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
static var messages: Message.Messages { get }
```

## Mentions

- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)

#### Discussion

If your app doesn’t implement this message listener, StoreKit retrieves any messages from the App Store each time your app launches, and presents them by default.

For more information about listening for and displaying messages, see [`Message`](message.md).

## See Also

- [let reason: Message.Reason](message/reason-swift.property.md)
  The reason that the App Store sends the message.
- [Message.Messages](message/messages-swift.struct.md)
  An asynchronous sequence of messages from the App Store.
- [Message.Reason](message/reason-swift.struct.md)
  Reasons for the App Store messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/message/messages-swift.type.property)*