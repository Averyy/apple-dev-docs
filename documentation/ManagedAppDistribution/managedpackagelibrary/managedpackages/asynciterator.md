# ManagedPackageLibrary.ManagedPackages.AsyncIterator

**Framework**: ManagedAppDistribution  
**Kind**: struct  
**Role**: Structure

The iterator for managed apps.

**Availability**:
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Instance Methods
- [func next() async throws -> ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
- [func next(isolation: isolated (any Actor)?) async throws(ManagedPackageLibrary.ManagedPackages.AsyncIterator.Failure) -> ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element?](./asynciterator/next%28isolation%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element](./asynciterator/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary/managedpackages/asynciterator)*