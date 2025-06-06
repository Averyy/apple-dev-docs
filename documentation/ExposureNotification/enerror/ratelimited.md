# rateLimited

**Framework**: Exposure Notification  
**Kind**: property

API calls are too frequent.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
static var rateLimited: ENError.Code { get }
```

## See Also

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
- [static var restricted: ENError.Code](enerror/restricted.md)
  Exposure notification is disabled due to system policies.
- [static var unknown: ENError.Code](enerror/unknown.md)
  Failure has an unknown cause.
- [static var unsupported: ENError.Code](enerror/unsupported.md)
  Operation is not supported.
- [static var dataInaccessible: ENError.Code](enerror/datainaccessible.md)
  The user must unlock the device before it can access data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerror/ratelimited)*