# makeMessage(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method  
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

To implement this method in your own `AsyncMessage` conformance, retrieve values from the [`Notification`](../../notification.md)’s [`userInfo`](../../notification/userinfo.md) and set them as properties on the message.

## Parameters

- `notification`: The posted [`Notification`](../../notification.md).

## Default Implementations

### NotificationCenter.AsyncMessage Implementations
- [static func makeMessage(Notification) -> Self?](./makemessage%28_%29-2l2y5.md)
  Converts a posted notification into this asynchronous message type for any observers.

## See Also

### Converting between messages and notifications
- [static func makeNotification(Self) -> Notification](./makenotification%28_%29.md)
  Converts a posted asynchronous message into a notification for any observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage/makemessage(_:))*