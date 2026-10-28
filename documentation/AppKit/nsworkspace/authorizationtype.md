# NSWorkspace.AuthorizationType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The types of privileged file operations that can be authorized by the user.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum AuthorizationType
```

```c
enum NSWorkspaceAuthorizationType : NSInteger;
```

## Overview

To enable your app to prompt the user for these file permissions, you must have a Privileged File Operation entitlement. If you have an app on the Mac App Store or plan to submit your app for review, you can [request this entitlement](https://developer.apple.com/go/?id=workspace-authorization).

## Topics

### Types of Authorization
- [NSWorkspace.AuthorizationType.createSymbolicLink](./authorizationtype/createsymboliclink.md)
  Authorization for the app to create a symbolic link.
- [NSWorkspace.AuthorizationType.replaceFile](./authorizationtype/replacefile.md)
  Authorization for the app to perform an atomic file write without changing the target file’s permissions.
- [NSWorkspace.AuthorizationType.setAttributes](./authorizationtype/setattributes.md)
  Authorization for the app to change specific file attributes.
### Initializers
- [init?(rawValue: Int)](./authorizationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing Privileged Operations
- [func requestAuthorization(to: NSWorkspace.AuthorizationType, completionHandler: (NSWorkspace.Authorization?, (any Error)?) -> Void)](./requestauthorization%28to,completionhandler%29.md)
  Requests authorization to perform a privileged file operation.
- [NSWorkspace.Authorization](./authorization.md)
  The authorization granted to the app by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorizationtype)*