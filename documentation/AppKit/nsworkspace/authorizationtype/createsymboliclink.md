# NSWorkspace.AuthorizationType.createSymbolicLink

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Authorization for the app to create a symbolic link.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case createSymbolicLink
```

```c
NSWorkspaceAuthorizationTypeCreateSymbolicLink
```

#### Discussion

Signifies that the user has granted authorization for [`createSymbolicLink(at:withDestinationURL:)`](../../../Foundation/filemanager/createsymboliclink%28at,withdestinationurl%29.md).

## See Also

### Types of Authorization
- [NSWorkspace.AuthorizationType.replaceFile](./replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.
- [NSWorkspace.AuthorizationType.setAttributes](./setattributes.md)
  Authorization for the app to change specific file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/createsymboliclink)*