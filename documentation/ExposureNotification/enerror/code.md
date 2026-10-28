# ENError.Code

**Framework**: Exposure Notification  
**Kind**: enum  
**Role**: Enumeration

Error codes that the exposure notification framework issues.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
enum Code
```

```c
enum ENErrorCode : NSInteger;
```

## Overview

> ❗ **Important**:  This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### Error Codes
- [ENError.Code.apiMisuse](./code/apimisuse.md)
  The API use is incorrect.
- [ENError.Code.badFormat](./code/badformat.md)
  A file is formated incorrectly.
- [ENError.Code.badParameter](./code/badparameter.md)
  The parameter is missing or incorrect.
- [ENError.Code.restricted](./code/restricted.md)
  Exposure notification is disabled due to system policies.
- [ENError.Code.bluetoothOff](./code/bluetoothoff.md)
  Bluetooth is turned off.
- [ENError.Code.insufficientMemory](./code/insufficientmemory.md)
  The memory is insufficient to perform the operation.
- [ENError.Code.insufficientStorage](./code/insufficientstorage.md)
  The storage is insufficient to enable notifications.
- [ENError.Code.internal](./code/internal.md)
  A bug in the internal notification framework.
- [ENError.Code.invalidated](./code/invalidated.md)
  A call to invalidate before the operation completes normally.
- [ENError.Code.notAuthorized](./code/notauthorized.md)
  The user has denied access to the notification framework.
- [ENError.Code.notEnabled](./code/notenabled.md)
  Notification is not enabled.
- [ENError.Code.notEntitled](./code/notentitled.md)
  Process of calling is not entitled.
- [ENError.Code.rateLimited](./code/ratelimited.md)
  API calls are too frequent.
- [ENError.Code.unknown](./code/unknown.md)
  Failure has an unknown cause.
- [ENError.Code.unsupported](./code/unsupported.md)
  Operation is not supported.
- [ENError.Code.dataInaccessible](./code/datainaccessible.md)
  The user must unlock the device before it can access data.
- [ENError.Code.travelStatusNotAvailable](./code/travelstatusnotavailable.md)
  The system can’t determine whether the user is traveling.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct ENError](../enerror.md)
  Errors that the exposure notification framework issues.
- [let ENErrorDomain: String](../enerrordomain.md)
  The domain for an error.
- [typealias ENErrorHandler](../enerrorhandler.md)
  The handler for error conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enerror/code)*