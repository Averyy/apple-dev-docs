# makeNotification(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Converts a posted asynchronous message into a notification for any observers.

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
static func makeNotification(_ message: Self) -> Notification
```

## Return Value

The converted [`Notification`](../../notification.md).

## Discussion

To implement this method in your own `AsyncMessage` conformance, use the properties defined by the message to populate the [`Notification`](../../notification.md)’s [`userInfo`](../../notification/userinfo.md).

## Parameters

- `message`: The posted `AsyncMessage`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage/makenotification(_:)-3760t)*