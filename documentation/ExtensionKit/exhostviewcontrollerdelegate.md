# EXHostViewControllerDelegate

**Framework**: ExtensionKit  
**Kind**: protocol

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
- [func hostViewControllerDidActivate(EXHostViewController)](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md)
  Tells the host that the app extension is active and ready to accept an XPC connection.
- [func hostViewControllerWillDeactivate(EXHostViewController, error: (any Error)?)](exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:).md)
  Tells the host that the app extension disconnected and is no longer available.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any EXHostViewControllerDelegate)?](exhostviewcontroller/delegate.md)
  A custom delegate object you use to receive notifications about the activation and deactivation of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate)*