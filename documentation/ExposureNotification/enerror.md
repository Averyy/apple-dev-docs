# ENError

**Framework**: Exposure Notification  
**Kind**: struct

Errors that the exposure notification framework issues.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
struct ENError
```

#### Overview

> ❗ **Important**:  This structure is available in iOS 12.5, and in iOS 13.5 and later.

 This structure is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Error Codes
- [static var apiMisuse: ENError.Code](enerror/apimisuse.md)
  The API use is incorrect.
- [static var badFormat: ENError.Code](enerror/badformat.md)
  A file is formated incorrectly.
- [static var badParameter: ENError.Code](enerror/badparameter.md)
  The parameter is missing or incorrect.
- [static var bluetoothOff: ENError.Code](enerror/bluetoothoff.md)
  Bluetooth is turned off.
- [static var insufficientMemory: ENError.Code](enerror/insufficientmemory.md)
  The memory is insufficient to perform the operation.
- [static var insufficientStorage: ENError.Code](enerror/insufficientstorage.md)
  The storage is insufficient to enable notifications.
- [static var `internal`: ENError.Code](enerror/internal.md)
  A bug in the internal notification framework.
- [static var invalidated: ENError.Code](enerror/invalidated.md)
  A call to invalidate before the operation completes normally.
- [static var notAuthorized: ENError.Code](enerror/notauthorized.md)
  The user has denied access to the notification framework.
- [static var notEnabled: ENError.Code](enerror/notenabled.md)
  Notification is not enabled.
- [static var notEntitled: ENError.Code](enerror/notentitled.md)
  Process of calling is not entitled.
- [static var rateLimited: ENError.Code](enerror/ratelimited.md)
  API calls are too frequent.
- [static var restricted: ENError.Code](enerror/restricted.md)
  Exposure notification is disabled due to system policies.
- [static var unknown: ENError.Code](enerror/unknown.md)
  Failure has an unknown cause.
- [static var unsupported: ENError.Code](enerror/unsupported.md)
  Operation is not supported.
- [static var dataInaccessible: ENError.Code](enerror/datainaccessible.md)
  The user must unlock the device before it can access data.
- [static var travelStatusNotAvailable: ENError.Code](enerror/travelstatusnotavailable.md)
  The system can’t determine whether the user is traveling.
- [ENError.Code](enerror/code.md)
  Error codes that the exposure notification framework issues.
### Type Properties
- [static var errorDomain: String](enerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ENError.Code](enerror/code.md)
  Error codes that the exposure notification framework issues.
- [let ENErrorDomain: String](enerrordomain.md)
  The domain for an error.
- [typealias ENErrorHandler](enerrorhandler.md)
  The handler for error conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerror)*