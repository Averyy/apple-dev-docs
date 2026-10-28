# currentDistributor

**Framework**: ManagedAppDistribution  
**Kind**: property  
**Role**: Type Property

The library provider for managed apps on this device.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

## Declaration

```swift
static let currentDistributor: ManagedAppLibrary
```

## Discussion

This is a singleton object.

## See Also

### Obtaining library information
- [var availableApps: ManagedAppLibrary.ManagedApps](./availableapps.md)
  The current managed apps available to this device.
- [ManagedAppLibrary.ManagedApps](./managedapps.md)
  An array of managed apps that updates as apps become available or unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/currentdistributor)*