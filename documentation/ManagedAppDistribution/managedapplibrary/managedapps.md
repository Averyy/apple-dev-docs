# ManagedAppLibrary.ManagedApps

**Framework**: ManagedAppDistribution  
**Kind**: struct  
**Role**: Structure

An array of managed apps that updates as apps become available or unavailable.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
struct ManagedApps
```

## Topics

### Obtaining managed apps
- [ManagedAppLibrary.ManagedApps.AsyncIterator](./managedapps/asynciterator.md)
  The iterator for managed apps.
- [ManagedAppLibrary.ManagedApps.Element](./managedapps/element.md)
  The type of element this asynchronous sequence produces.
- [func makeAsyncIterator() -> ManagedAppLibrary.ManagedApps.AsyncIterator](./managedapps/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Obtaining library information
- [var availableApps: ManagedAppLibrary.ManagedApps](./availableapps.md)
  The current managed apps available to this device.
- [static let currentDistributor: ManagedAppLibrary](./currentdistributor.md)
  The library provider for managed apps on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps)*