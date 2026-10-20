# makeNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method  
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

The converted [`Notification`](../../notification.md).

#### Discussion

To implement this method in your own `MainActorMessage` conformance, use the properties defined by the message to populate the [`Notification`](../../notification.md)’s [`userInfo`](../../notification/userinfo.md).

## Parameters

- `message`: The posted `MainActorMessage`.

## Default Implementations

### NotificationCenter.MainActorMessage Implementations
- [static func makeNotification(Self) -> Notification](./makenotification%28_%29-4xbaj.md)
  Converts a posted main actor message into a notification for any observers.

## See Also

### Converting between messages and notifications
- [static func makeMessage(Notification) -> Self?](./makemessage%28_%29.md)
  Converts a posted notification into this main actor message type for any observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makenotification(_:))*