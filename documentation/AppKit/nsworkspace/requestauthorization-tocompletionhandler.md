# requestAuthorization(to:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Requests authorization to perform a privileged file operation.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func requestAuthorization(to type: NSWorkspace.AuthorizationType) async throws -> NSWorkspace.Authorization
```

#### Discussion

## Parameters

- `type`: The type of file operation to perform.
- `completionHandler`: The completion handler takes two parameters:

## See Also

- [NSWorkspace.Authorization](nsworkspace/authorization.md)
  The authorization granted to the app by the user.
- [NSWorkspace.AuthorizationType](nsworkspace/authorizationtype.md)
  The types of privileged file operations that can be authorized by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/requestauthorization(to:completionhandler:))*