# NSValidatedUserInterfaceItem

**Framework**: AppKit  
**Kind**: protocol

A protocol that a custom class can adopt to manage the automatic enablement of a UI control.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSValidatedUserInterfaceItem
```

#### Overview

The [`NSValidatedUserInterfaceItem`](nsvalidateduserinterfaceitem.md) protocol works with the [`NSUserInterfaceValidations`](nsuserinterfacevalidations.md) protocol to enable or disable a control automatically, depending on whether any responder in the responder chain can handle the control’s action method. The [`NSMenuItem`](nsmenuitem.md) and [`NSToolbarItem`](nstoolbaritem.md) classes implement this protocol.

By conforming to this protocol, your control can participate in this validation mechanism. To validate a control, the application calls [`validateUserInterfaceItem(_:)`](nsuserinterfacevalidations/validateuserinterfaceitem(_:).md) for each item in the responder chain, starting with the first responder. If no responder returns [`true`](https://developer.apple.com/documentation/swift/true), the item is disabled. For example, a menu item that sends the `copy:` action message would disable itself if no responder in the responder chain can be copied.

## Topics

### Getting information about a user interface item
- [var action: Selector?](nsvalidateduserinterfaceitem/action.md)
  Returns the selector of the receiver’s action method.
- [var tag: Int](nsvalidateduserinterfaceitem/tag.md)
  Returns the receiver’s tag integer.

## Relationships

### Conforming Types
- [NSMenuItem](nsmenuitem.md)
- [NSMenuToolbarItem](nsmenutoolbaritem.md)
- [NSSearchToolbarItem](nssearchtoolbaritem.md)
- [NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
- [NSToolbarItem](nstoolbaritem.md)
- [NSToolbarItemGroup](nstoolbaritemgroup.md)
- [NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)

## See Also

- [protocol NSUserInterfaceValidations](nsuserinterfacevalidations.md)
  A protocol that a custom class can adopt to manage the enabled state of a UI element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvalidateduserinterfaceitem)*