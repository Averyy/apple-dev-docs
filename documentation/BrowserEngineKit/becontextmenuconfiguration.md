# BEContextMenuConfiguration

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An object that defers presentation of a contextual menu.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class BEContextMenuConfiguration
```

```objc
@interface BEContextMenuConfiguration : UIContextMenuConfiguration
```

## Overview

Return an instance of this class when you don’t yet know whether a contextual menu is presentable, or don’t have the menu items available when the system calls your interaction delegate’s [`contextMenuInteraction(_:configurationForMenuAtLocation:)`](../UIKit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_,configurationformenuatlocation%29.md) method. Once you have the real configuration, call [`fulfill(using:)`](./becontextmenuconfiguration/fulfill%28using%29.md) with it, or pass `nil` to indicate that no menu presentation is possible.

> **Note**:  In most situations, use [`UIDeferredMenuElement`](../UIKit/uideferredmenuelement.md) when you don’t have the content of a contextual menu element at the time the system asks your delegate and you need to calculate it asynchronously. Use this class instead when the calculation involves a short deferral, for example, an XPC call to a browser extension.

## Topics

### Creating a context menu configuration
- [init()](./becontextmenuconfiguration/init%28%29.md)
  Creates a context menu configuration.
### Fulfilling the configuration
- [func fulfill(using: UIContextMenuConfiguration?) -> Bool](./becontextmenuconfiguration/fulfill%28using%29.md)
  Supplies a contextual menu configuration to the system.

## Relationships

### Inherits From
- [UIContextMenuConfiguration](../UIKit/uicontextmenuconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration)*