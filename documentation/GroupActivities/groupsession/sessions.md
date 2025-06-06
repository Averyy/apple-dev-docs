# GroupSession.Sessions

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence of sessions you use to manage a specific activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Sessions
```

#### Overview

When a participant engages one of your app’s activities, a `Sessions` structure provides the session you use to handle synchronization. Iterate over the contents of this structure asynchronously to retrieve each new session the system delivers to your app. The system delivers only one [`GroupSession`](groupsession.md) for each activity. To monitor changes to that session, configure subscribers to its published properties.

Don’t create this structure directly. Instead, use the [`sessions()`](groupactivity/sessions().md) method to retrieve the sessions.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> GroupSession<ActivityType>.Sessions.Iterator](groupsession/sessions/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSession.Sessions.Iterator](groupsession/sessions/iterator.md)
- [GroupSession.Sessions.Element](groupsession/sessions/element.md)
  The type of element produced by this asynchronous sequence.
### Finding elements
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](groupsession/sessions/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](groupsession/sessions/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsession/sessions/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsession/sessions/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsession/sessions/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
### Selecting elements
- [func prefix(Int) -> AsyncPrefixSequence<Self>](groupsession/sessions/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](groupsession/sessions/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
### Excluding elements
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](groupsession/sessions/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](groupsession/sessions/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](groupsession/sessions/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
### Transforming a sequence
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](groupsession/sessions/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](groupsession/sessions/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Type Aliases
- [GroupSession.Sessions.AsyncIterator](groupsession/sessions/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](groupsession/sessions/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/sessions)*