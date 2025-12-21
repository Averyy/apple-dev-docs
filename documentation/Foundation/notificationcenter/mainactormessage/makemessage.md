# makeMessage(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Converts a posted notification into this main actor message type for any observers.

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
static func makeMessage(_ notification: Notification) -> Self?
```

#### Return Value

The converted `MainActorMessage` or `nil` if conversion is not possible.

#### Discussion

To implement this method in your own `MainActorMessage` conformance, retrieve values from the [`Notification`](notification.md)’s [`userInfo`](notification/userinfo.md) and set them as properties on the message.

## Parameters

- `notification`: The posted  .

## See Also

- [static func makeNotification(Self) -> Notification](notificationcenter/mainactormessage/makenotification(_:).md)
  Converts a posted main actor message into a notification for any observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage/makemessage(_:))*