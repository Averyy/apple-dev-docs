# NSWorkspace.AuthorizationType.replaceFile

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Authorization for the app to perform an atomic file write without changing the target file’s permissions.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case replaceFile
```

```c
NSWorkspaceAuthorizationTypeReplaceFile
```

## Discussion

Signifies that the user has granted authorization for [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](../../../Foundation/filemanager/replaceitem%28at,withitemat,backupitemname,options,resultingitemurl%29.md). When you use a [`FileManager`](../../../Foundation/filemanager.md) with this authorization, the file manager ignores the `backupItemName` and `options` parameters.

## See Also

### Types of Authorization
- [NSWorkspace.AuthorizationType.createSymbolicLink](./createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.setAttributes](./setattributes.md)
  Authorization for the app to change specific file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/replacefile)*