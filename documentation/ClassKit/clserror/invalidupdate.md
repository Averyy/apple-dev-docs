# invalidUpdate

**Framework**: ClassKit  
**Kind**: property

ClassKit failed to save an updated object in the data store.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var invalidUpdate: CLSError.Code { get }
```

## See Also

- [static var none: CLSError.Code](clserror/none.md)
  No error.
- [static var authorizationDenied: CLSError.Code](clserror/authorizationdenied.md)
  The app isn’t authorized to perform the requested operation.
- [static var classKitUnavailable: CLSError.Code](clserror/classkitunavailable.md)
  ClassKit isn’t available on this device.
- [static var databaseInaccessible: CLSError.Code](clserror/databaseinaccessible.md)
  ClassKit isn’t accessible because the device is locked.
- [static var invalidAccountCredentials: CLSError.Code](clserror/invalidaccountcredentials.md)
- [static var invalidArgument: CLSError.Code](clserror/invalidargument.md)
  An invalid argument was provided to the API.
- [static var invalidCreate: CLSError.Code](clserror/invalidcreate.md)
  An attempt to save a new object that already exists in the data store failed.
- [static var invalidModification: CLSError.Code](clserror/invalidmodification.md)
  An attempt to modify a read-only object failed.
- [static var limits: CLSError.Code](clserror/limits.md)
  A limit has been exceeded.
- [static var partialFailure: CLSError.Code](clserror/partialfailure.md)
  ClassKit encountered more than one error.
- [CLSError.Code](clserror/code.md)
  Error codes that ClassKit issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserror/invalidupdate)*