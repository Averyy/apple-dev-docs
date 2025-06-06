# ManagedAppLibrary.ManagedApps.AsyncIterator.Element

**Framework**: ManagedAppDistribution  
**Kind**: typealias

The type of element this asynchronous sequence produces.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
typealias Element = Result<[ManagedApp], ManagedAppDistributionError>
```

## See Also

- [func next() async throws -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?](managedapplibrary/managedapps/asynciterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator/element)*