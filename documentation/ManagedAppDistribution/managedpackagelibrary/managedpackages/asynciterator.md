# ManagedPackageLibrary.ManagedPackages.AsyncIterator

**Framework**: ManagedAppDistribution  
**Kind**: struct

The iterator for managed apps.

**Availability**:
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Instance Methods
- [func next() async throws -> ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element?](managedpackagelibrary/managedpackages/asynciterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
- [func next(isolation: isolated (any Actor)?) async throws(ManagedPackageLibrary.ManagedPackages.AsyncIterator.Failure) -> ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element?](managedpackagelibrary/managedpackages/asynciterator/next(isolation:).md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [ManagedPackageLibrary.ManagedPackages.AsyncIterator.Element](managedpackagelibrary/managedpackages/asynciterator/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary/managedpackages/asynciterator)*