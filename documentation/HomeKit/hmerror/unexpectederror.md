# unexpectedError

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An unexpected error.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
static var unexpectedError: HMError.Code { get }
```

## See Also

### Detecting general errors
- [static var alreadyExists: HMError.Code](./alreadyexists.md)
  An error indicating the container already contains the object you are trying to add.
- [static var genericError: HMError.Code](./genericerror.md)
  An error that does not have a more specific error code.
- [static var incompatibleHomeHub: HMError.Code](./incompatiblehomehub.md)
  No compatible home hub found.
- [static var invalidClass: HMError.Code](./invalidclass.md)
  An attempt to use an abstract base class in an operation instead of a concrete subclass.
- [static var notFound: HMError.Code](./notfound.md)
  An error indicating the object was not found in the container.
- [static var notificationAlreadyEnabled: HMError.Code](./notificationalreadyenabled.md)
  An error indicating the notification is already enabled.
- [static var notificationNotSupported: HMError.Code](./notificationnotsupported.md)
  An attempt to register for notifications from an accessory that does not support notifications.
- [static var operationNotSupported: HMError.Code](./operationnotsupported.md)
  An attempt to use an unsupported operation.
- [static var missingEntitlement: HMError.Code](./missingentitlement.md)
  An error indicating a required entitlement is not available.
- [static var referToUserManual: HMError.Code](./refertousermanual.md)
  An error described in the device’s user manual.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/unexpectederror)*