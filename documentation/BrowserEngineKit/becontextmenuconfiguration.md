# BEContextMenuConfiguration

**Framework**: BrowserEngineKit  
**Kind**: class

An object that defers presentation of a contextual menu.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class BEContextMenuConfiguration
```

#### Overview

Return an instance of this class when you don’t yet know whether a contextual menu is presentable, or don’t have the menu items available when the system calls your interaction delegate’s [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](https://developer.apple.com/documentation/UIKit/UIContextMenuInteractionDelegate/contextMenuInteraction(_:configurationForMenuAtLocation:)) method. Once you have the real configuration, call [`fulfill(using:)`](becontextmenuconfiguration/fulfill(using:).md) with it, or pass `nil` to indicate that no menu presentation is possible.

> **Note**:  In most situations, use [`UIDeferredMenuElement`](https://developer.apple.com/documentation/UIKit/UIDeferredMenuElement) when you don’t have the content of a contextual menu element at the time the system asks your delegate and you need to calculate it asynchronously. Use this class instead when the calculation involves a short deferral, for example, an XPC call to a browser extension.

## Topics

### Creating a context menu configuration
- [init()](becontextmenuconfiguration/init.md)
  Creates a context menu configuration.
### Fulfilling the configuration
- [func fulfill(using: UIContextMenuConfiguration?) -> Bool](becontextmenuconfiguration/fulfill(using:).md)
  Supplies a contextual menu configuration to the system.

## Relationships

### Inherits From
- [UIContextMenuConfiguration](../UIKit/UIContextMenuConfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration)*