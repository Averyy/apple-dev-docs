# incompatibleHomeHub

**Framework**: HomeKit  
**Kind**: property

No compatible home hub found.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var incompatibleHomeHub: HMError.Code { get }
```

## See Also

- [static var alreadyExists: HMError.Code](hmerror/alreadyexists.md)
  An error indicating the container already contains the object you are trying to add.
- [static var genericError: HMError.Code](hmerror/genericerror.md)
  An error that does not have a more specific error code.
- [static var invalidClass: HMError.Code](hmerror/invalidclass.md)
  An attempt to use an abstract base class in an operation instead of a concrete subclass.
- [static var notFound: HMError.Code](hmerror/notfound.md)
  An error indicating the object was not found in the container.
- [static var notificationAlreadyEnabled: HMError.Code](hmerror/notificationalreadyenabled.md)
  An error indicating the notification is already enabled.
- [static var notificationNotSupported: HMError.Code](hmerror/notificationnotsupported.md)
  An attempt to register for notifications from an accessory that does not support notifications.
- [static var operationNotSupported: HMError.Code](hmerror/operationnotsupported.md)
  An attempt to use an unsupported operation.
- [static var unexpectedError: HMError.Code](hmerror/unexpectederror.md)
  An unexpected error.
- [static var missingEntitlement: HMError.Code](hmerror/missingentitlement.md)
  An error indicating a required entitlement is not available.
- [static var referToUserManual: HMError.Code](hmerror/refertousermanual.md)
  An error described in the device’s user manual.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/incompatiblehomehub)*