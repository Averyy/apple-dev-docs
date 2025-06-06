# CLSError.Code.partialFailure

**Framework**: ClassKit  
**Kind**: case

ClassKit encountered more than one error.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case partialFailure
```

#### Discussion

When you receive an error of this type, the [`underlyingErrorsKey`](clserroruserinfokey/underlyingerrorskey.md) key in the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary provides an array of the individual errors contributing to this one.

## See Also

- [CLSError.Code.none](clserror/code/none.md)
  No error.
- [CLSError.Code.authorizationDenied](clserror/code/authorizationdenied.md)
  The app isn’t authorized to perform the requested operation.
- [CLSError.Code.classKitUnavailable](clserror/code/classkitunavailable.md)
  ClassKit isn’t available on this device.
- [CLSError.Code.databaseInaccessible](clserror/code/databaseinaccessible.md)
  ClassKit isn’t accessible because the device is locked.
- [CLSError.Code.invalidAccountCredentials](clserror/code/invalidaccountcredentials.md)
- [CLSError.Code.invalidArgument](clserror/code/invalidargument.md)
  An invalid argument was provided to the API.
- [CLSError.Code.invalidCreate](clserror/code/invalidcreate.md)
  An attempt to save a new object that already exists in the data store failed.
- [CLSError.Code.invalidModification](clserror/code/invalidmodification.md)
  An attempt to modify a read-only object failed.
- [CLSError.Code.invalidUpdate](clserror/code/invalidupdate.md)
  ClassKit failed to save an updated object in the data store.
- [CLSError.Code.limits](clserror/code/limits.md)
  A limit has been exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserror/code/partialfailure)*