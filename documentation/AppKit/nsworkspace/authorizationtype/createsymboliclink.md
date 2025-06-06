# NSWorkspace.AuthorizationType.createSymbolicLink

**Framework**: AppKit  
**Kind**: case

Authorization for the app to create a symbolic link.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case createSymbolicLink
```

#### Discussion

Signifies that the user has granted authorization for [`createSymbolicLink(at:withDestinationURL:)`](https://developer.apple.com/documentation/foundation/filemanager/1414652-createsymboliclink).

## See Also

- [NSWorkspace.AuthorizationType.replaceFile](nsworkspace/authorizationtype/replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.
- [NSWorkspace.AuthorizationType.setAttributes](nsworkspace/authorizationtype/setattributes.md)
  Authorization for the app to change specific file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype/createsymboliclink)*