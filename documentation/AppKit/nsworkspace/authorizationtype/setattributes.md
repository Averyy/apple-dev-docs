# NSWorkspace.AuthorizationType.setAttributes

**Framework**: AppKit  
**Kind**: case

Authorization for the app to change specific file attributes.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case setAttributes
```

#### Discussion

Signifies that the user has granted authorization for [`setAttributes(_:ofItemAtPath:)`](https://developer.apple.com/documentation/foundation/filemanager/1413667-setattributes).

Only these attributes can be modified:

- [`ownerAccountID`](https://developer.apple.com/documentation/foundation/fileattributekey/1417871-owneraccountid)
- [`groupOwnerAccountID`](https://developer.apple.com/documentation/foundation/fileattributekey/1416961-groupowneraccountid)
- [`posixPermissions`](https://developer.apple.com/documentation/foundation/fileattributekey/1418260-posixpermissions)

## See Also

- [NSWorkspace.AuthorizationType.createSymbolicLink](nsworkspace/authorizationtype/createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.replaceFile](nsworkspace/authorizationtype/replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/setattributes)*