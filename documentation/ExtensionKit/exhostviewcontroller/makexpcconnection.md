# makeXPCConnection()

**Framework**: ExtensionKit  
**Kind**: method

Attempts to connect to the extension over XPC.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func makeXPCConnection() throws -> NSXPCConnection
```

#### Return Value

An object representing the connection.

## See Also

- [var delegate: (any EXHostViewControllerDelegate)?](exhostviewcontroller/delegate.md)
  The connection delegate.
- [protocol EXHostViewControllerDelegate](exhostviewcontrollerdelegate.md)
  The delegate for a hosted view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/makexpcconnection())*