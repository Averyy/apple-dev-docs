# init(authorization:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a file manager object that is authorized to perform privileged file system operations.

**Availability**:
- macOS 10.14+

## Declaration

```swift
convenience init(authorization: NSWorkspace.Authorization)
```

```objc
+ (instancetype) fileManagerWithAuthorization:(NSWorkspaceAuthorization *) authorization;
```

## See Also

### Creating a file manager
- [class var `default`: FileManager](./default.md)
  The shared file manager object for the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/init(authorization:))*