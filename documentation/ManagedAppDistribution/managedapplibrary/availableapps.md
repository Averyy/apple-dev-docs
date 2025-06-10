# availableApps

**Framework**: ManagedAppDistribution  
**Kind**: property

The current managed apps available to this device.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
final var availableApps: ManagedAppLibrary.ManagedApps { get }
```

#### Discussion

The current managed apps are of type `Result<[ManagedApp], ManagedAppDistributionError>`. Use an asynchronous `for` loop to update your views when the current managed apps change. If the device can’t retrieve the metadata for the apps, fetching the list of managed apps fails with `ManagedAppDistributionError.networkError`. An example of this failure is if the device is offline.

> **Note**: The async sequence returns an error and the sequence ends when running as an iOS app on macOS.

## See Also

- [ManagedAppLibrary.ManagedApps](managedapplibrary/managedapps.md)
  An array of managed apps that updates as apps become available or unavailable.
- [static let currentDistributor: ManagedAppLibrary](managedapplibrary/currentdistributor.md)
  The library provider for managed apps on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/availableapps)*