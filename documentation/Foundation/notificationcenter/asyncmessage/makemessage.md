# makeMessage(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Converts a posted notification into this asynchronous message type for any observers.

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
static func makeMessage(_ notification: Notification) -> Self?
```

#### Return Value

The converted `AsyncMessage`, or `nil` if conversion is not possible.

#### Discussion

To implement this method in your own `AsyncMessage` conformance, retrieve values from the [`Notification`](notification.md)’s [`userInfo`](notification/userinfo.md) and set them as properties on the message.

## Parameters

- `notification`: The posted  .

## See Also

- [static func makeNotification(Self) -> Notification](notificationcenter/asyncmessage/makenotification(_:).md)
  Converts a posted asynchronous message into a notification for any observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage/makemessage(_:))*