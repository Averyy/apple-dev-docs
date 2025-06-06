# ManagedAppLibrary.ManagedApps.AsyncIterator

**Framework**: ManagedAppDistribution  
**Kind**: struct

The iterator for managed apps.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Iterating
- [ManagedAppLibrary.ManagedApps.AsyncIterator.Element](managedapplibrary/managedapps/asynciterator/element.md)
  The type of element this asynchronous sequence produces.
- [func next() async throws -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](managedapplibrary/managedapps/asynciterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Instance Methods
- [func next(isolation: isolated (any Actor)?) async throws(ManagedAppLibrary.ManagedApps.AsyncIterator.Failure) -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](managedapplibrary/managedapps/asynciterator/next(isolation:).md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [ManagedAppLibrary.ManagedApps.AsyncIterator.Failure](managedapplibrary/managedapps/asynciterator/failure.md)
  The type of failure produced by iteration.
### Default Implementations
- [AsyncIteratorProtocol Implementations](managedapplibrary/managedapps/asynciterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [ManagedAppLibrary.ManagedApps.Element](managedapplibrary/managedapps/element.md)
  The type of element this asynchronous sequence produces.
- [func makeAsyncIterator() -> ManagedAppLibrary.ManagedApps.AsyncIterator](managedapplibrary/managedapps/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator)*