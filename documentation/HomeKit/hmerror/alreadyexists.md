# alreadyExists

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An error indicating the container already contains the object you are trying to add.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var alreadyExists: HMError.Code { get }
```

## See Also

### Detecting general errors
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
- [static var unexpectedError: HMError.Code](./unexpectederror.md)
  An unexpected error.
- [static var missingEntitlement: HMError.Code](./missingentitlement.md)
  An error indicating a required entitlement is not available.
- [static var referToUserManual: HMError.Code](./refertousermanual.md)
  An error described in the device’s user manual.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/alreadyexists)*