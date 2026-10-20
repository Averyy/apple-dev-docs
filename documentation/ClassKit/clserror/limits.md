# limits

**Framework**: ClassKit  
**Kind**: property  
**Role**: Type Property

A limit has been exceeded.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var limits: CLSError.Code { get }
```

## See Also

### Error codes
- [static var none: CLSError.Code](./none.md)
  No error.
- [static var authorizationDenied: CLSError.Code](./authorizationdenied.md)
  The app isn’t authorized to perform the requested operation.
- [static var classKitUnavailable: CLSError.Code](./classkitunavailable.md)
  ClassKit isn’t available on this device.
- [static var databaseInaccessible: CLSError.Code](./databaseinaccessible.md)
  ClassKit isn’t accessible because the device is locked.
- [static var errorDomain: String](./errordomain.md)
- [static var invalidAccountCredentials: CLSError.Code](./invalidaccountcredentials.md)
- [static var invalidArgument: CLSError.Code](./invalidargument.md)
  An invalid argument was provided to the API.
- [static var invalidCreate: CLSError.Code](./invalidcreate.md)
  An attempt to save a new object that already exists in the data store failed.
- [static var invalidModification: CLSError.Code](./invalidmodification.md)
  An attempt to modify a read-only object failed.
- [static var invalidUpdate: CLSError.Code](./invalidupdate.md)
  ClassKit failed to save an updated object in the data store.
- [static var partialFailure: CLSError.Code](./partialfailure.md)
  ClassKit encountered more than one error.
- [CLSError.Code](./code.md)
  Error codes that ClassKit issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clserror/limits)*