# availablePackages

**Framework**: ManagedAppDistribution  
**Kind**: property

The current managed apps available to this device.

**Availability**:
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
final var availablePackages: ManagedPackageLibrary.ManagedPackages { get }
```

#### Discussion

The current managed packages are of type `Result<[ManagedPackage], ManagedAppDistributionError>`. Use an asynchronous `for` loop to update your views when the current managed packages change. If the device can’t retrieve the metadata for the packages, fetching the list of managed packages fails with `ManagedAppDistributionError.networkError`. An example of this failure is if the device is offline.

> **Note**: The async sequence returns an error and the sequence ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary/availablepackages)*