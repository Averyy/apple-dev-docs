# ManagedAppLibrary

**Framework**: ManagedAppDistribution  
**Kind**: class

A representation of a library of managed apps.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
final class ManagedAppLibrary
```

## Mentions

- [Fetching and displaying managed apps](fetching-and-displaying-managed-apps.md)

## Topics

### Obtaining library information
- [var availableApps: ManagedAppLibrary.ManagedApps](managedapplibrary/availableapps.md)
  The current managed apps available to this device.
- [ManagedAppLibrary.ManagedApps](managedapplibrary/managedapps.md)
  An array of managed apps that updates as apps become available or unavailable.
- [static let currentDistributor: ManagedAppLibrary](managedapplibrary/currentdistributor.md)
  The library provider for managed apps on this device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Fetching and displaying managed apps](fetching-and-displaying-managed-apps.md)
  Provide a consistent app presentation when displaying managed apps.
- [struct ManagedApp](managedapp.md)
  A representation of a managed app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary)*