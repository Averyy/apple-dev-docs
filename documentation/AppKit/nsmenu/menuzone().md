# menuZone()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the zone from which `NSMenu` objects should be allocated.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
class func menuZone() -> NSZone!
```

```objc
+ (NSZone *) menuZone;
```

## Return Value

The zone from which `NSMenu` objects should be allocated.

## Discussion

This is left in for compatibility and always returns [`NSDefaultMallocZone`](../../Foundation/nsdefaultmalloczone.md). It is not necessary to use this.

## See Also

### Deprecated methods
- [func helpRequested(with: NSEvent)](./helprequested%28with%29.md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [- attachedMenu](./attachedmenu.md)
  Returns the menu currently attached to the menu.
- [- isAttached](./isattached.md)
  Returns a Boolean value that indicates whether the menu is currently attached to another menu.
- [- locationForSubmenu:](./locationforsubmenu_.md)
  Returns the location in screen coordinates where the given submenu is displayed when opened as a submenu of the menu.
- [- sizeToFit](./sizetofit.md)
  Resizes the menu to exactly fit its items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuzone())*