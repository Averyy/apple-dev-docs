# NSWorkspace.Authorization

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The authorization granted to the app by the user.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class Authorization
```

```objc
@interface NSWorkspaceAuthorization : NSObject
```

#### Overview

To enable your app to prompt the user for these file permissions, you must have a Privileged File Operation entitlement. If you have an app on the Mac App Store or plan to submit your app for review, you can [request this entitlement](https://developer.apple.com/go/?id=workspace-authorization).

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing Privileged Operations
- [func requestAuthorization(to: NSWorkspace.AuthorizationType, completionHandler: (NSWorkspace.Authorization?, (any Error)?) -> Void)](./requestauthorization%28to,completionhandler%29.md)
  Requests authorization to perform a privileged file operation.
- [NSWorkspace.AuthorizationType](./authorizationtype.md)
  The types of privileged file operations that can be authorized by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorization)*