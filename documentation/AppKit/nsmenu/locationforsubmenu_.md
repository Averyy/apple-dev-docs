# locationForSubmenu:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the location in screen coordinates where the given submenu is displayed when opened as a submenu of the menu.

**Availability**:
- macOS 10.0+ - Deprecated in 10.2

## Declaration

```objc
- (NSPoint) locationForSubmenu:(NSMenu *) submenu;
```

#### Return Value

An `NSPoint` structure describing the location or (0.0, 0.0) if the submenu does not exist in the menu.

## Parameters

- `submenu`: A menu object that is a submenu of the menu.

## See Also

### Deprecated methods
- [- attachedMenu](./attachedmenu.md)
  Returns the menu currently attached to the menu.
- [- isAttached](./isattached.md)
  Returns a Boolean value that indicates whether the menu is currently attached to another menu.
- [- sizeToFit](./sizetofit.md)
  Resizes the menu to exactly fit its items.
- [func helpRequested(with: NSEvent)](./helprequested%28with%29.md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [class func menuZone() -> NSZone!](./menuzone%28%29.md)
  Returns the zone from which `NSMenu` objects should be allocated.
- [+ setMenuZone:](./setmenuzone_.md)
  Sets the zone from which `NSMenu` objects should be allocated
- [- contextMenuRepresentation](./contextmenurepresentation.md)
  Deprecated.
- [- setContextMenuRepresentation:](./setcontextmenurepresentation_.md)
  Deprecated.
- [- tearOffMenuRepresentation](./tearoffmenurepresentation.md)
  Deprecated.
- [- setTearOffMenuRepresentation:](./settearoffmenurepresentation_.md)
  Deprecated.
- [- setMenuRepresentation:](./setmenurepresentation_.md)
  Deprecated.
- [- menuRepresentation](./menurepresentation.md)
  Deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/locationforsubmenu:)*