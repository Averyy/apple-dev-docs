# ManagedPackageLibrary

**Framework**: ManagedAppDistribution  
**Kind**: class

A representation of a library of managed packages.

**Availability**:
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
final class ManagedPackageLibrary
```

## Topics

### Structures
- [ManagedPackageLibrary.ManagedPackages](managedpackagelibrary/managedpackages.md)
  An array of managed apps that updates as apps become available or unavailable.
### Instance Properties
- [var availablePackages: ManagedPackageLibrary.ManagedPackages](managedpackagelibrary/availablepackages.md)
  The current managed apps available to this device.
### Type Properties
- [static let currentDistributor: ManagedPackageLibrary](managedpackagelibrary/currentdistributor.md)
  The library provider for managed apps on this device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary)*