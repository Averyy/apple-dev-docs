# EXHostViewControllerDelegate

**Framework**: ExtensionKit  
**Kind**: protocol

The delegate for a hosted view controller.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol EXHostViewControllerDelegate : NSObjectProtocol
```

## Topics

### Delegate Methods
- [func hostViewControllerDidActivate(EXHostViewController)](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md)
  A delegate method the view controller calls when a connection succeeds.
- [func hostViewControllerWillDeactivate(EXHostViewController, error: (any Error)?)](exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:).md)
  A delegate method the host view controller calls when an extension disconnects.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func makeXPCConnection() throws -> NSXPCConnection](exhostviewcontroller/makexpcconnection.md)
  Attempts to connect to the extension over XPC.
- [var delegate: (any EXHostViewControllerDelegate)?](exhostviewcontroller/delegate.md)
  The connection delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate)*