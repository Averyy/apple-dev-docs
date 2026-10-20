# ManagedAppLibrary.ManagedApps.AsyncIterator.Element

**Framework**: ManagedAppDistribution  
**Kind**: typealias  
**Role**: Type Alias

The type of element this asynchronous sequence produces.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
typealias Element = Result<[ManagedApp], ManagedAppDistributionError>
```

## See Also

### Iterating
- [func next() async throws -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](./next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator/element)*