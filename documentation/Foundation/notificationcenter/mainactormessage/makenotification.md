# makeNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Converts a posted main actor message into a notification for any observers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
static func makeNotification(_ message: Self) -> Notification
```

#### Return Value

The converted [`Notification`](notification.md).

#### Discussion

To implement this method in your own `MainActorMessage` conformance, use the properties defined by the message to populate the [`Notification`](notification.md)’s [`userInfo`](notification/userinfo.md).

## Parameters

- `message`: The posted  .

## See Also

- [static func makeMessage(Notification) -> Self?](notificationcenter/mainactormessage/makemessage(_:).md)
  Converts a posted notification into this main actor message type for any observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:))*