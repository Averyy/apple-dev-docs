# menu(_:update:at:shouldCancel:)

**Framework**: AppKit  
**Kind**: method

Invoked to let the delegate update a menu item before it is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func menu(_ menu: NSMenu, update item: NSMenuItem, at index: Int, shouldCancel: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to continue the process. If you return [`false`](https://developer.apple.com/documentation/swift/false), your [`menu(_:update:at:shouldCancel:)`](nsmenudelegate/menu(_:update:at:shouldcancel:).md) is not called again. In that case, it’s your responsibility to trim any extra items from the menu.

#### Discussion

If your [`numberOfItems(in:)`](nsmenudelegate/numberofitems(in:).md) delegate method returns a positive value, then your [`menu(_:update:at:shouldCancel:)`](nsmenudelegate/menu(_:update:at:shouldcancel:).md) method is called for each item in the menu. You can then update the menu title, image, and so forth for each menu item.

## Parameters

- `menu`: The menu object that owns  .
- `item`: The menu-item object that may be updated.
- `index`: The integer index of the menu item.
- `shouldCancel`: Set to   if, due to some user action, the menu no longer needs to be displayed before all the menu items have been updated. You can ignore this flag, return  , and continue; or you can save your work (to save time the next time your delegate is called) and return   to stop the updating.

## See Also

- [func confinementRect(for: NSMenu, on: NSScreen?) -> NSRect](nsmenudelegate/confinementrect(for:on:).md)
  Invoked to allow the delegate to specify a display location for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menu(_:update:at:shouldcancel:))*