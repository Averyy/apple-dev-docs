# NSWorkspace.AuthorizationType.replaceFile

**Framework**: AppKit  
**Kind**: case

Authorization for the app to perform an atomic file write without changing the target file’s permissions.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case replaceFile
```

#### Discussion

Signifies that the user has granted authorization for [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](https://developer.apple.com/documentation/foundation/filemanager/1412432-replaceitem). When you use a [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) with this authorization, the file manager ignores the `backupItemName` and `options` parameters.

## See Also

- [NSWorkspace.AuthorizationType.createSymbolicLink](nsworkspace/authorizationtype/createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.setAttributes](nsworkspace/authorizationtype/setattributes.md)
  Authorization for the app to change specific file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/replacefile)*