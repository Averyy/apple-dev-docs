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

Signifies that the user has granted authorization for [`setAttributes(_:ofItemAtPath:)`](https://developer.apple.com/documentation/Foundation/FileManager/setAttributes(_:ofItemAtPath:)).

Only these attributes can be modified:

- [`ownerAccountID`](https://developer.apple.com/documentation/Foundation/FileAttributeKey/ownerAccountID)
- [`groupOwnerAccountID`](https://developer.apple.com/documentation/Foundation/FileAttributeKey/groupOwnerAccountID)
- [`posixPermissions`](https://developer.apple.com/documentation/Foundation/FileAttributeKey/posixPermissions)

## See Also

- [NSWorkspace.AuthorizationType.createSymbolicLink](nsworkspace/authorizationtype/createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.replaceFile](nsworkspace/authorizationtype/replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/setattributes)*