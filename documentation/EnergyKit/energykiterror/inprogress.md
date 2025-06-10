# EnergyKitError.inProgress

**Framework**: EnergyKit  
**Kind**: case

A request is already in progress.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case inProgress
```

#### Discussion

Only one request can be active at a time. Wait until the prior request completes before trying again.

## See Also

- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  The system failed to retrieve guidance for the requested location.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  The load event payload is invalid.
- [EnergyKitError.permissionDenied](energykiterror/permissiondenied.md)
  The client doesn’t have permission to access the requested API.
- [EnergyKitError.serviceUnavailable](energykiterror/serviceunavailable.md)
  The requested service failed to start.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  The requested energy venue doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/inprogress)*