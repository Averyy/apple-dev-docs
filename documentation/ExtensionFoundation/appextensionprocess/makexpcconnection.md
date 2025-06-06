# makeXPCConnection()

**Framework**: ExtensionFoundation  
**Kind**: method

Creates a new XPC connection to the extension process.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func makeXPCConnection() throws -> NSXPCConnection
```

#### Return Value

The connection object representing the created XPC connection.

#### Discussion

This method creates a connection to the extension process and returns it. You’re responsible for configuring the connection. While you retain a reference to the returned connection object, the extension receives processing time. Once you deallocate the connection object, the system suspends or terminates the extension process.

## See Also

- [func invalidate()](appextensionprocess/invalidate.md)
  Stop the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/makexpcconnection())*