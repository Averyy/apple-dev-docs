# GroupSessionMessenger.Messages

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence of messages sent to the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Messages<Message> where Message : Decodable, Message : Encodable
```

#### Overview

When you use a [`GroupSessionMessenger`](groupsessionmessenger.md) to communicate across devices, the `Messages` structure provides the sequence of messages the other devices send. Iterate over the contents of this structure asynchronously to retrieve each message and update your app.

Don’t create this structure directly. Instead, use the [`messages(of:)`](groupsessionmessenger/messages(of:)-626qo.md) or [`messages(of:)`](groupsessionmessenger/messages(of:)-jvoz.md) method to retrieve the messages for a given session.

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> GroupSessionMessenger.Messages<Message>.Iterator](groupsessionmessenger/messages/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSessionMessenger.Messages.Iterator](groupsessionmessenger/messages/iterator.md)
- [GroupSessionMessenger.Messages.Element](groupsessionmessenger/messages/element.md)
  The type of element produced by this asynchronous sequence.
### Finding elements
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](groupsessionmessenger/messages/contains(where:).md)
  Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](groupsessionmessenger/messages/allsatisfy(_:).md)
  Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsessionmessenger/messages/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsessionmessenger/messages/min(by:).md)
  Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](groupsessionmessenger/messages/max(by:).md)
  Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
### Selecting elements
- [func prefix(Int) -> AsyncPrefixSequence<Self>](groupsessionmessenger/messages/prefix(_:).md)
  Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](groupsessionmessenger/messages/prefix(while:).md)
  Returns an asynchronous sequence, containing the initial, consecutive elements of the base sequence that satisfy the given predicate.
### Excluding elements
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](groupsessionmessenger/messages/dropfirst(_:).md)
  Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](groupsessionmessenger/messages/drop(while:).md)
  Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](groupsessionmessenger/messages/filter(_:).md)
  Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
### Transforming a sequence
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](groupsessionmessenger/messages/reduce(_:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](groupsessionmessenger/messages/reduce(into:_:).md)
  Returns the result of combining the elements of the asynchronous sequence using the given closure, given a mutable initial value.
### Type Aliases
- [GroupSessionMessenger.Messages.AsyncIterator](groupsessionmessenger/messages/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](groupsessionmessenger/messages/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](groupsessionmessenger/messages(of:)-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](groupsessionmessenger/messages(of:)-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.MessageContext](groupsessionmessenger/messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages)*