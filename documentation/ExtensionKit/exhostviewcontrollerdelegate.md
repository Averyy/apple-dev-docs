# EXHostViewControllerDelegate

**Framework**: ExtensionKit  
**Kind**: protocol  
**Role**: Protocol

An interface you use to track the activation and deactivation of an app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
protocol EXHostViewControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to activation and deactivation events
- [func hostViewControllerDidActivate(EXHostViewController)](./exhostviewcontrollerdelegate/hostviewcontrollerdidactivate%28_%29.md)
  Tells the host that the app extension is active and ready to accept an XPC connection.
- [func hostViewControllerWillDeactivate(EXHostViewController, error: (any Error)?)](./exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate%28_,error%29.md)
  Tells the host that the app extension disconnected and is no longer available.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to activation and deactivation events
- [var delegate: (any EXHostViewControllerDelegate)?](./exhostviewcontroller/delegate.md)
  A custom delegate object you use to receive notifications about the activation and deactivation of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate)*