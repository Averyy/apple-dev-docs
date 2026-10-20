# NotificationCenter.Notifications.Iterator

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [func next() async -> Notification?](./iterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Supporting Types
- [NotificationCenter.Notifications.Element](./element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an Iterator
- [func makeAsyncIterator() -> NotificationCenter.Notifications.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/notifications/iterator)*