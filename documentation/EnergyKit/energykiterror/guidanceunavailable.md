# EnergyKitError.guidanceUnavailable

**Framework**: EnergyKit  
**Kind**: case  
**Role**: Case

An error that indicates the framework fails to provide guidance for a location.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
case guidanceUnavailable
```

## Discussion

This error can occur:

- During a network failure; ask the person to check their network connection.
- When [`ElectricityGuidance`](../electricityguidance.md) isn’t available in the requested location.

## See Also

### Viewing error reasons
- [EnergyKitError.inProgress](./inprogress.md)
  An error that indicates a request is already in progress.
- [EnergyKitError.invalidLoadEvent](./invalidloadevent.md)
  An error that indicates an invalid load event.
- [EnergyKitError.permissionDenied](./permissiondenied.md)
  An error that indicates the client doesn’t have permission to access a requested API.
- [EnergyKitError.serviceUnavailable](./serviceunavailable.md)
  An error that indicates when a requested service fails to start.
- [EnergyKitError.venueUnavailable](./venueunavailable.md)
  An error that indicates a referenced venue is invalid, nonexistent, or restricted by the person.
- [EnergyKitError.locationServicesDenied](./locationservicesdenied.md)
  An error that indicates that Location Services is off in the home’s settings.
- [EnergyKitError.rateLimitExceeded](./ratelimitexceeded.md)
  An error that indicates the app exceeds the rate limit for using the framework.
- [EnergyKitError.unsupportedRegion](./unsupportedregion.md)
  An error that indicates the device resides in an unsupported region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/guidanceunavailable)*