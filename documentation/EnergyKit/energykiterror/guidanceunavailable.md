# EnergyKitError.guidanceUnavailable

**Framework**: EnergyKit  
**Kind**: case

The system failed to retrieve guidance for the requested location.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case guidanceUnavailable
```

#### Discussion

This error can occur when:

- A network failure occurs; ask the person to check their network connection.
- [`ElectricityGuidance`](electricityguidance.md) isn’t available in the requested location.

## See Also

- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  A request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  The load event payload is invalid.
- [EnergyKitError.permissionDenied](energykiterror/permissiondenied.md)
  The client doesn’t have permission to access the requested API.
- [EnergyKitError.serviceUnavailable](energykiterror/serviceunavailable.md)
  The requested service failed to start.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  The requested energy venue doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/guidanceunavailable)*