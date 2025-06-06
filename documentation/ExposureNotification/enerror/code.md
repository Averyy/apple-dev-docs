# ENError.Code

**Framework**: Exposure Notification  
**Kind**: enum

Error codes that the exposure notification framework issues.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
enum Code
```

#### Overview

> ❗ **Important**:  This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

 This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Error Codes
- [ENError.Code.apiMisuse](enerror/code/apimisuse.md)
  The API use is incorrect.
- [ENError.Code.badFormat](enerror/code/badformat.md)
  A file is formated incorrectly.
- [ENError.Code.badParameter](enerror/code/badparameter.md)
  The parameter is missing or incorrect.
- [ENError.Code.restricted](enerror/code/restricted.md)
  Exposure notification is disabled due to system policies.
- [ENError.Code.bluetoothOff](enerror/code/bluetoothoff.md)
  Bluetooth is turned off.
- [ENError.Code.insufficientMemory](enerror/code/insufficientmemory.md)
  The memory is insufficient to perform the operation.
- [ENError.Code.insufficientStorage](enerror/code/insufficientstorage.md)
  The storage is insufficient to enable notifications.
- [ENError.Code.internal](enerror/code/internal.md)
  A bug in the internal notification framework.
- [ENError.Code.invalidated](enerror/code/invalidated.md)
  A call to invalidate before the operation completes normally.
- [ENError.Code.notAuthorized](enerror/code/notauthorized.md)
  The user has denied access to the notification framework.
- [ENError.Code.notEnabled](enerror/code/notenabled.md)
  Notification is not enabled.
- [ENError.Code.notEntitled](enerror/code/notentitled.md)
  Process of calling is not entitled.
- [ENError.Code.rateLimited](enerror/code/ratelimited.md)
  API calls are too frequent.
- [ENError.Code.unknown](enerror/code/unknown.md)
  Failure has an unknown cause.
- [ENError.Code.unsupported](enerror/code/unsupported.md)
  Operation is not supported.
- [ENError.Code.dataInaccessible](enerror/code/datainaccessible.md)
  The user must unlock the device before it can access data.
- [ENError.Code.travelStatusNotAvailable](enerror/code/travelstatusnotavailable.md)
  The system can’t determine whether the user is traveling.
### Initializers
- [init?(rawValue: Int)](enerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ENError](enerror.md)
  Errors that the exposure notification framework issues.
- [let ENErrorDomain: String](enerrordomain.md)
  The domain for an error.
- [typealias ENErrorHandler](enerrorhandler.md)
  The handler for error conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerror/code)*