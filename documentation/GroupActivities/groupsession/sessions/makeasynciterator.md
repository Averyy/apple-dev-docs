# makeAsyncIterator()

**Framework**: Group Activities  
**Kind**: method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func makeAsyncIterator() -> GroupSession<ActivityType>.Sessions.Iterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [GroupSession.Sessions.Iterator](groupsession/sessions/iterator.md)
- [GroupSession.Sessions.Element](groupsession/sessions/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/sessions/makeasynciterator())*