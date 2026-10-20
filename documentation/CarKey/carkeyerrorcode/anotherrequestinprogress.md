# CarKeyErrorCode.AnotherRequestInProgress

**Framework**: CarKey  
**Kind**: case  
**Role**: Case

An error that indicates a previous request is still in progress.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
case AnotherRequestInProgress
```

#### Discussion

Wait for the previous request to finish or update your UI to indicate a request is in progress.

## See Also

### Getting the Error Code
- [CarKeyErrorCode.ClientInBackground](./clientinbackground.md)
  An error that indicates the operation occurred when the app was in the background.
- [CarKeyErrorCode.EnduringRequestUsingEventMethod](./enduringrequestusingeventmethod.md)
  An error that indicates a mismatch between the initial request type and the results.
- [CarKeyErrorCode.FeatureNotSupported](./featurenotsupported.md)
  An error that indicates the specified feature isn’t supported in the current environment.
- [CarKeyErrorCode.FunctionUnknown](./functionunknown.md)
  An error that indicates the vehicle didn’t recognize the specified function identifier.
- [CarKeyErrorCode.Internal](./internal.md)
  An error that indicates an unknown error occurred.
- [CarKeyErrorCode.MessageTooLong](./messagetoolong.md)
  An error that indicates the command you sent was too long.
- [CarKeyErrorCode.RequestNotInProgress](./requestnotinprogress.md)
  An error that indicates an enduring operation wasn’t running.
- [CarKeyErrorCode.RequestTimedOut](./requesttimedout.md)
  An error that indicates the request didn’t complete in time.
- [CarKeyErrorCode.SecurityViolation](./securityviolation.md)
  An error that indicates your app doesn’t have the required entitlements.
- [CarKeyErrorCode.SessionNotActive](./sessionnotactive.md)
  An error that indicates an active session is currently inactive.
- [CarKeyErrorCode.VehicleNotConnected](./vehiclenotconnected.md)
  An error that indicates the vehicle isn’t available to respond to the request.
- [CarKeyErrorCode.VehicleNotFound](./vehiclenotfound.md)
  An error that indicates a vehicle with the specified ID wasn’t found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyerrorcode/anotherrequestinprogress)*