# Activity.ContentStateUpdates.Iterator

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
- [func next() async -> Activity<Attributes>.ContentStateUpdates.Element?](activity/contentstateupdates-swift.struct/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [Activity.ContentStateUpdates.Iterator.Element](activity/contentstateupdates-swift.struct/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](activity/contentstateupdates-swift.struct/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> Activity<Attributes>.ContentStateUpdates.Iterator](activity/contentstateupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Activity.ContentStateUpdates.Element](activity/contentstateupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct/iterator)*