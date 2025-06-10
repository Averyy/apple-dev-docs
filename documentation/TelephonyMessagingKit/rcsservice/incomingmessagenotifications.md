# incomingMessageNotifications

**Framework**: TelephonyMessagingKit  
**Kind**: property

An asynchronous sequence of incoming message notifications produced by this service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never> { get throws }
```

#### Discussion

Iterate over this sequence with a `for`-`await`-`in` loop to receive [`RCSService.IncomingMessageNotification`](rcsservice/incomingmessagenotification.md) instances that indicate the arrival of incoming messages, like this:

```swift
let service = TelephonyMessagingSession.shared.rcsService

let incomingMessageNotifications = try service.incomingMessageNotifications
Task {
    for await notification in incomingMessageNotifications {
        let receivedMessage = notification.message
        switch receivedMessage.content {
            case .text(let text): // ...
            case .fileTransfer(let fileTransfer): // ...
            case .geolocationPush(let geolocationPush): // ...
            case .dispositionNotification(let dispositionNotification): // ...
            case .composingIndicator(let composingIndicator): // ...
        }
    }
```

For each message type, the matched `case` contains an instance of the relevant [`RCSMessage.Content`](rcsmessage/content-swift.enum.md) type as its associated value. In this example, `text` would contain string content in its [`body`](rcsmessage/text/body.md) property, and `geolocationPush` would have geolocation values in its [`latitude`](rcsmessage/geolocationpush/latitude.md) and [`longitude`](rcsmessage/geolocationpush/longitude.md) properties.

## See Also

- [RCSService.IncomingMessageNotification](rcsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming RCS message.
- [struct RCSMessage](rcsmessage.md)
  A structure that contains an RCS message’s content and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/incomingmessagenotifications)*