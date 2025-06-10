# NSToolbarItemValidation

**Framework**: AppKit  
**Kind**: protocol

Validation of a toolbar item.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSToolbarItemValidation : NSObjectProtocol
```

#### Overview

A toolbar item with a valid target and action is enabled by default. To allow a toolbar item to be disabled in certain situations, a toolbar item’s target can implement the [`validateToolbarItem(_:)`](nstoolbaritemvalidation/validatetoolbaritem(_:).md) method.

> **Note**:  The [`NSToolbarItem`](nstoolbaritem.md) [`validate()`](nstoolbaritem/validate().md) method is called only if the item’s target has a valid action defined on its target and if the item isn’t a custom view item. If you want to validate a custom view item, then you have to subclass [`NSToolbarItem`](nstoolbaritem.md) and override [`validate()`](nstoolbaritem/validate().md).

## Topics

### Enabling and disabling toolbar items
- [func validateToolbarItem(NSToolbarItem) -> Bool](nstoolbaritemvalidation/validatetoolbaritem(_:).md)
  If this method is implemented and returns [`false`](https://developer.apple.com/documentation/swift/false), NSToolbar will disable `theItem`; returning [`true`](https://developer.apple.com/documentation/swift/true) causes `theItem` to be enabled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Integrating a Toolbar and Touch Bar into Your App](integrating-a-toolbar-and-touch-bar-into-your-app.md)
  Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
- [class NSToolbar](nstoolbar.md)
  An object that manages the space above your app’s custom content and either below or integrated with the window’s title bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemvalidation)*