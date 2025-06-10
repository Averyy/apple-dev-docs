# EnergyKitError.serviceUnavailable

**Framework**: EnergyKit  
**Kind**: case

The requested service failed to start.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case serviceUnavailable
```

#### Discussion

The failure might be due to the service connection failing.

## See Also

- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  The system failed to retrieve guidance for the requested location.
- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  A request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  The load event payload is invalid.
- [EnergyKitError.permissionDenied](energykiterror/permissiondenied.md)
  The client doesn’t have permission to access the requested API.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  The requested energy venue doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/serviceunavailable)*