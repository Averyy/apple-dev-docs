# EnergyKitError

**Framework**: EnergyKit  
**Kind**: enum

A specialized error that provides localized messages describing the error and why it occurred.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum EnergyKitError
```

## Topics

### Viewing error reasons
- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  An error that indicates the framework fails to provide guidance for a location.
- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  An error that indicates a request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  An error that indicates an invalid load event.
- [EnergyKitError.permissionDenied](energykiterror/permissiondenied.md)
  An error that indicates the client doesn’t have permission to access a requested API.
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
### Reading error messages
- [var errorDescription: String?](energykiterror/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](energykiterror/failurereason.md)
  A localized message providing text if the person requests help.
- [var helpAnchor: String?](energykiterror/helpanchor.md)
  A localized message providing text if the user requests help
- [var recoverySuggestion: String?](energykiterror/recoverysuggestion.md)
  A localized message describing how to recover from the failure.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror)*