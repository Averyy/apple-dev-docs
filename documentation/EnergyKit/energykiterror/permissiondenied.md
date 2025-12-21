# EnergyKitError.permissionDenied

**Framework**: EnergyKit  
**Kind**: case

An error that indicates the client doesn’t have permission to access a requested API.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
case permissionDenied
```

#### Discussion

This failure happens when a person declines the EnergyKit approval prompt. A person can adjust the relevant setting in:

- Settings > Apps > (your app)
- Settings > Privacy & Security > Home

## See Also

- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  An error that indicates the framework fails to provide guidance for a location.
- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  An error that indicates a request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  An error that indicates an invalid load event.
- [EnergyKitError.serviceUnavailable](energykiterror/serviceunavailable.md)
  An error that indicates when a requested service fails to start.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  An error that indicates a referenced venue is invalid, nonexistent, or restricted by the person.
- [EnergyKitError.locationServicesDenied](energykiterror/locationservicesdenied.md)
  An error that indicates that Location Services is off in the home’s settings.
- [EnergyKitError.rateLimitExceeded](energykiterror/ratelimitexceeded.md)
  An error that indicates the app exceeds the rate limit for using the framework.
- [EnergyKitError.unsupportedRegion](energykiterror/unsupportedregion.md)
  An error that indicates the device resides in an unsupported region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/permissiondenied)*