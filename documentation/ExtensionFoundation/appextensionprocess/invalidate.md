# invalidate()

**Framework**: ExtensionFoundation  
**Kind**: method

Stop the extension process.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

When you call this method, you tell the system your app no longer needs this extension process. If this is the last connection from the host process to the extension process, the system terminates the extension process.

## See Also

- [func makeXPCConnection() throws -> NSXPCConnection](appextensionprocess/makexpcconnection.md)
  Creates a new XPC connection to the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/invalidate())*