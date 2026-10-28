# confinementRect(for:on:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to specify a display location for the menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func confinementRect(for menu: NSMenu, on screen: NSScreen?) -> NSRect
```

```objc
- (NSRect) confinementRectForMenu:(NSMenu *) menu onScreen:(NSScreen *) screen;
```

## Return Value

The rectangle the menu should be displayed within, in screen coordinates.

## Discussion

This method is sent to the delegate when a menu is about to be opened on the specified screen.

If you return `NSZeroRect`, or if the delegate doesn’t implement this method, the menu will be confined to the bounds appropriate for the given screen. The returned rect may not be honored in all cases, for example, if it would force the menu to be too small.

## Parameters

- `menu`: The menu object.
- `screen`: The screen the menu will open on.

## See Also

### Updating Menu Layout
- [func menu(NSMenu, update: NSMenuItem, at: Int, shouldCancel: Bool) -> Bool](./menu%28_,update,at,shouldcancel%29.md)
  Invoked to let the delegate update a menu item before it is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/confinementrect(for:on:))*