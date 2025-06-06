# CMError

**Framework**: Core Motion  
**Kind**: struct

Defines motion errors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMError
```

## Topics

### Errors
- [var CMErrorDeviceRequiresMovement: CMError](cmerrordevicerequiresmovement.md)
  The device must move for a sampling of motion data to occur.
- [var CMErrorInvalidAction: CMError](cmerrorinvalidaction.md)
  The specified action is invalid.
- [var CMErrorInvalidParameter: CMError](cmerrorinvalidparameter.md)
  The specified parameter is invalid.
- [var CMErrorMotionActivityNotAuthorized: CMError](cmerrormotionactivitynotauthorized.md)
  The app isn’t currently authorized to use motion activity support.
- [var CMErrorMotionActivityNotAvailable: CMError](cmerrormotionactivitynotavailable.md)
  Motion activity support isn’t available on the current device.
- [var CMErrorMotionActivityNotEntitled: CMError](cmerrormotionactivitynotentitled.md)
  The app is missing an entitlement for the requested activity.
- [var CMErrorNilData: CMError](cmerrornildata.md)
  Core Motion didn’t return any data.
- [var CMErrorNULL: CMError](cmerrornull.md)
  No error occurred.
- [var CMErrorNotAuthorized: CMError](cmerrornotauthorized.md)
  The app isn’t authorized to use the Core Motion framework.
- [var CMErrorNotAvailable: CMError](cmerrornotavailable.md)
  The requested service isn’t available on this device.
- [var CMErrorNotEntitled: CMError](cmerrornotentitled.md)
  The app is missing a required entitlement.
- [var CMErrorSize: CMError](cmerrorsize.md)
  The data is the incorrect size.
- [var CMErrorTrueNorthNotAvailable: CMError](cmerrortruenorthnotavailable.md)
  True north isn’t available on this device.
- [var CMErrorUnknown: CMError](cmerrorunknown.md)
  An unknown error occurred.
### Initializers
- [init(UInt32)](cmerror/init(_:).md)
- [init(rawValue: UInt32)](cmerror/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](cmerror/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let CMErrorDomain: String](cmerrordomain.md)
  The error domain for Core Motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmerror)*