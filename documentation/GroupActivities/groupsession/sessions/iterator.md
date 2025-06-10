# GroupSession.Sessions.Iterator

**Framework**: Group Activities  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> GroupSession<ActivityType>?](groupsession/sessions/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [GroupSession.Sessions.Iterator.Element](groupsession/sessions/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](groupsession/sessions/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func makeAsyncIterator() -> GroupSession<ActivityType>.Sessions.Iterator](groupsession/sessions/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSession.Sessions.Element](groupsession/sessions/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/sessions/iterator)*