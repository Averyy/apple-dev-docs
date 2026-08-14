# NotificationCenter.Notifications.Iterator

**Framework**: Foundation  
**Kind**: struct

The asynchronous iterator created by this asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Iterating over Elements
- [func next() async -> Notification?](notificationcenter/notifications/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Supporting Types
- [NotificationCenter.Notifications.Element](notificationcenter/notifications/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../swift/asynciteratorprotocol.md)

## See Also

- [func makeAsyncIterator() -> NotificationCenter.Notifications.Iterator](notificationcenter/notifications/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/notifications/iterator)*