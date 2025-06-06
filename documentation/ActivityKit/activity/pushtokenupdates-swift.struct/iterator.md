# Activity.PushTokenUpdates.Iterator

**Framework**: ActivityKit  
**Kind**: struct

An iterator for accessing individual data entries from the series.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> Activity<Attributes>.PushTokenUpdates.Element?](activity/pushtokenupdates-swift.struct/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [Activity.PushTokenUpdates.Iterator.Element](activity/pushtokenupdates-swift.struct/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](activity/pushtokenupdates-swift.struct/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> Activity<Attributes>.PushTokenUpdates.Iterator](activity/pushtokenupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.PushTokenUpdates.Element](activity/pushtokenupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.struct/iterator)*