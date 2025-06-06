# ManagedAppLibrary.ManagedApps

**Framework**: ManagedAppDistribution  
**Kind**: struct

An array of managed apps that updates as apps become available or unavailable.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
struct ManagedApps
```

## Topics

### Obtaining managed apps
- [ManagedAppLibrary.ManagedApps.AsyncIterator](managedapplibrary/managedapps/asynciterator.md)
  The iterator for managed apps.
- [ManagedAppLibrary.ManagedApps.Element](managedapplibrary/managedapps/element.md)
  The type of element this asynchronous sequence produces.
- [func makeAsyncIterator() -> ManagedAppLibrary.ManagedApps.AsyncIterator](managedapplibrary/managedapps/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](managedapplibrary/managedapps/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var availableApps: ManagedAppLibrary.ManagedApps](managedapplibrary/availableapps.md)
  The current managed apps available to this device.
- [static let currentDistributor: ManagedAppLibrary](managedapplibrary/currentdistributor.md)
  The library provider for managed apps on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps)*