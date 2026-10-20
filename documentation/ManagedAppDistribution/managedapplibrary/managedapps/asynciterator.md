# ManagedAppLibrary.ManagedApps.AsyncIterator

**Framework**: ManagedAppDistribution  
**Kind**: struct  
**Role**: Structure

The iterator for managed apps.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Iterating
- [ManagedAppLibrary.ManagedApps.AsyncIterator.Element](./asynciterator/element.md)
  The type of element this asynchronous sequence produces.
- [func next() async throws -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Instance Methods
- [func next(isolation: isolated (any Actor)?) async throws(ManagedAppLibrary.ManagedApps.AsyncIterator.Failure) -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](./asynciterator/next%28isolation%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Obtaining managed apps
- [ManagedAppLibrary.ManagedApps.Element](./element.md)
  The type of element this asynchronous sequence produces.
- [func makeAsyncIterator() -> ManagedAppLibrary.ManagedApps.AsyncIterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator)*