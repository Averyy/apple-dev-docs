# NSWorkspace.Authorization

**Framework**: AppKit  
**Kind**: class

The authorization granted to the app by the user.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class Authorization
```

#### Overview

To enable your app to prompt the user for these file permissions, you must have a Privileged File Operation entitlement. If you have an app on the Mac App Store or plan to submit your app for review, you can [`request this entitlement`](https://developer.apple.comhttps://developer.apple.com/go/?id=workspace-authorization).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func requestAuthorization(to: NSWorkspace.AuthorizationType, completionHandler: (NSWorkspace.Authorization?, (any Error)?) -> Void)](nsworkspace/requestauthorization(to:completionhandler:).md)
  Requests authorization to perform a privileged file operation.
- [NSWorkspace.AuthorizationType](nsworkspace/authorizationtype.md)
  The types of privileged file operations that can be authorized by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/authorization)*