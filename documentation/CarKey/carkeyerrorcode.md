# CarKeyErrorCode

**Framework**: CarKey  
**Kind**: enum

The errors that can occur when you perform remote-keyless entry operations on a vehicle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
enum CarKeyErrorCode
```

## Topics

### Getting the Error Code
- [CarKeyErrorCode.AnotherRequestInProgress](carkeyerrorcode/anotherrequestinprogress.md)
  An error that indicates a previous request is still in progress.
- [CarKeyErrorCode.ClientInBackground](carkeyerrorcode/clientinbackground.md)
  An error that indicates the operation occurred when the app was in the background.
- [CarKeyErrorCode.EnduringRequestUsingEventMethod](carkeyerrorcode/enduringrequestusingeventmethod.md)
  An error that indicates a mismatch between the initial request type and the results.
- [CarKeyErrorCode.FeatureNotSupported](carkeyerrorcode/featurenotsupported.md)
  An error that indicates the specified feature isn’t supported in the current environment.
- [CarKeyErrorCode.FunctionUnknown](carkeyerrorcode/functionunknown.md)
  An error that indicates the vehicle didn’t recognize the specified function identifier.
- [CarKeyErrorCode.Internal](carkeyerrorcode/internal.md)
  An error that indicates an unknown error occurred.
- [CarKeyErrorCode.MessageTooLong](carkeyerrorcode/messagetoolong.md)
  An error that indicates the command you sent was too long.
- [CarKeyErrorCode.RequestNotInProgress](carkeyerrorcode/requestnotinprogress.md)
  An error that indicates an enduring operation wasn’t running.
- [CarKeyErrorCode.RequestTimedOut](carkeyerrorcode/requesttimedout.md)
  An error that indicates the request didn’t complete in time.
- [CarKeyErrorCode.SecurityViolation](carkeyerrorcode/securityviolation.md)
  An error that indicates your app doesn’t have the required entitlements.
- [CarKeyErrorCode.SessionNotActive](carkeyerrorcode/sessionnotactive.md)
  An error that indicates an active session is currently inactive.
- [CarKeyErrorCode.VehicleNotConnected](carkeyerrorcode/vehiclenotconnected.md)
  An error that indicates the vehicle isn’t available to respond to the request.
- [CarKeyErrorCode.VehicleNotFound](carkeyerrorcode/vehiclenotfound.md)
  An error that indicates a vehicle with the specified ID wasn’t found.
### Getting a Description of the Error
- [var localizedDescription: String](carkeyerrorcode/localizeddescription.md)
  Retrieve the localized description for this error.
### Operators
- [static func == (CarKeyErrorCode, CarKeyErrorCode) -> Bool](carkeyerrorcode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](carkeyerrorcode/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](carkeyerrorcode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](carkeyerrorcode/equatable-implementations.md)
- [Error Implementations](carkeyerrorcode/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyerrorcode)*