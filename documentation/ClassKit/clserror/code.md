# CLSError.Code

**Framework**: ClassKit  
**Kind**: enum  
**Role**: Enumeration

Error codes that ClassKit issues.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum CLSErrorCode : NSInteger;
```

## Topics

### Error codes
- [CLSError.Code.none](./code/none.md)
  No error.
- [CLSError.Code.authorizationDenied](./code/authorizationdenied.md)
  The app isn’t authorized to perform the requested operation.
- [CLSError.Code.classKitUnavailable](./code/classkitunavailable.md)
  ClassKit isn’t available on this device.
- [CLSError.Code.databaseInaccessible](./code/databaseinaccessible.md)
  ClassKit isn’t accessible because the device is locked.
- [CLSError.Code.invalidAccountCredentials](./code/invalidaccountcredentials.md)
- [CLSError.Code.invalidArgument](./code/invalidargument.md)
  An invalid argument was provided to the API.
- [CLSError.Code.invalidCreate](./code/invalidcreate.md)
  An attempt to save a new object that already exists in the data store failed.
- [CLSError.Code.invalidModification](./code/invalidmodification.md)
  An attempt to modify a read-only object failed.
- [CLSError.Code.invalidUpdate](./code/invalidupdate.md)
  ClassKit failed to save an updated object in the data store.
- [CLSError.Code.limits](./code/limits.md)
  A limit has been exceeded.
- [CLSError.Code.partialFailure](./code/partialfailure.md)
  ClassKit encountered more than one error.
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
- [struct CLSError](../clserror.md)
  Errors issued by ClassKit.
- [let CLSErrorCodeDomain: String](../clserrorcodedomain.md)
  The error domain that ClassKit uses when issuing errors.
- [struct CLSErrorUserInfoKey](../clserroruserinfokey.md)
  Keys that appear in the user info dictionary in errors that ClassKit creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserror/code)*