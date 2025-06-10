# EnergyKitError.permissionDenied

**Framework**: EnergyKit  
**Kind**: case

The client doesn’t have permission to access the requested API.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
case permissionDenied
```

#### Discussion

The failure in this error might be due to insufficient app permissions. Check app permissions and try again.

## See Also

- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  The system failed to retrieve guidance for the requested location.
- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  A request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  The load event payload is invalid.
- [EnergyKitError.serviceUnavailable](energykiterror/serviceunavailable.md)
  The requested service failed to start.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  The requested energy venue doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror/permissiondenied)*