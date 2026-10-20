# NSWorkspace.AuthorizationType.setAttributes

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Authorization for the app to change specific file attributes.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case setAttributes
```

```c
NSWorkspaceAuthorizationTypeSetAttributes
```

#### Discussion

Signifies that the user has granted authorization for [`setAttributes(_:ofItemAtPath:)`](../../../Foundation/filemanager/setattributes%28_,ofitematpath%29.md).

Only these attributes can be modified:

- [`ownerAccountID`](../../../Foundation/fileattributekey/owneraccountid.md)
- [`groupOwnerAccountID`](../../../Foundation/fileattributekey/groupowneraccountid.md)
- [`posixPermissions`](../../../Foundation/fileattributekey/posixpermissions.md)

## See Also

### Types of Authorization
- [NSWorkspace.AuthorizationType.createSymbolicLink](./createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.replaceFile](./replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/setattributes)*