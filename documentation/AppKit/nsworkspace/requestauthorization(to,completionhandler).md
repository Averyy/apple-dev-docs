# requestAuthorization(to:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests authorization to perform a privileged file operation.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func requestAuthorization(to type: NSWorkspace.AuthorizationType, completionHandler: @escaping @Sendable (NSWorkspace.Authorization?, (any Error)?) -> Void)
```

```swift
func requestAuthorization(to type: NSWorkspace.AuthorizationType) async throws -> NSWorkspace.Authorization
```

```objc
- (void) requestAuthorizationOfType:(NSWorkspaceAuthorizationType) type completionHandler:(void (^)(NSWorkspaceAuthorization *authorization, NSError *error)) completionHandler;
```

## Discussion

## Parameters

- `type`: The type of file operation to perform.
- `completionHandler`: The completion handler to call when the authorization request is completed.

  The completion handler takes two parameters:

  - **authorization**: The authorization granted for this app. Use it when creating a new [`FileManager`](../../Foundation/filemanager.md) with [`init(authorization:)`](../../Foundation/filemanager/init%28authorization%29.md).
  - **error**: `nil` if the app is authorized; otherwise, a pointer to the authorization error.

## See Also

### Performing Privileged Operations
- [NSWorkspace.Authorization](./authorization.md)
  The authorization granted to the app by the user.
- [NSWorkspace.AuthorizationType](./authorizationtype.md)
  The types of privileged file operations that can be authorized by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/requestauthorization(to:completionhandler:))*