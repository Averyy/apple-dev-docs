# apiMisuse

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Type Property

The API use is incorrect.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
static var apiMisuse: ENError.Code { get }
```

## See Also

### Error Codes
- [static var badFormat: ENError.Code](./badformat.md)
  A file is formated incorrectly.
- [static var badParameter: ENError.Code](./badparameter.md)
  The parameter is missing or incorrect.
- [static var bluetoothOff: ENError.Code](./bluetoothoff.md)
  Bluetooth is turned off.
- [static var insufficientMemory: ENError.Code](./insufficientmemory.md)
  The memory is insufficient to perform the operation.
- [static var insufficientStorage: ENError.Code](./insufficientstorage.md)
  The storage is insufficient to enable notifications.
- [static var `internal`: ENError.Code](./internal.md)
  A bug in the internal notification framework.
- [static var invalidated: ENError.Code](./invalidated.md)
  A call to invalidate before the operation completes normally.
- [static var notAuthorized: ENError.Code](./notauthorized.md)
  The user has denied access to the notification framework.
- [static var notEnabled: ENError.Code](./notenabled.md)
  Notification is not enabled.
- [static var notEntitled: ENError.Code](./notentitled.md)
  Process of calling is not entitled.
- [static var rateLimited: ENError.Code](./ratelimited.md)
  API calls are too frequent.
- [static var restricted: ENError.Code](./restricted.md)
  Exposure notification is disabled due to system policies.
- [static var unknown: ENError.Code](./unknown.md)
  Failure has an unknown cause.
- [static var unsupported: ENError.Code](./unsupported.md)
  Operation is not supported.
- [static var dataInaccessible: ENError.Code](./datainaccessible.md)
  The user must unlock the device before it can access data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerror/apimisuse)*