# NSWorkspace.AuthorizationType

**Framework**: AppKit  
**Kind**: enum

The types of privileged file operations that can be authorized by the user.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum AuthorizationType
```

#### Overview

To enable your app to prompt the user for these file permissions, you must have a Privileged File Operation entitlement. If you have an app on the Mac App Store or plan to submit your app for review, you can [`request this entitlement`](https://developer.apple.comhttps://developer.apple.com/go/?id=workspace-authorization).

## Topics

### Types of Authorization
- [NSWorkspace.AuthorizationType.createSymbolicLink](nsworkspace/authorizationtype/createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.replaceFile](nsworkspace/authorizationtype/replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.
- [NSWorkspace.AuthorizationType.setAttributes](nsworkspace/authorizationtype/setattributes.md)
  Authorization for the app to change specific file attributes.
### Initializers
- [init?(rawValue: Int)](nsworkspace/authorizationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestAuthorization(to: NSWorkspace.AuthorizationType, completionHandler: (NSWorkspace.Authorization?, (any Error)?) -> Void)](nsworkspace/requestauthorization(to:completionhandler:).md)
  Requests authorization to perform a privileged file operation.
- [NSWorkspace.Authorization](nsworkspace/authorization.md)
  The authorization granted to the app by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype)*