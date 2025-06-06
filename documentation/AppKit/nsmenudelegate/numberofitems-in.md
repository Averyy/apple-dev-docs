# numberOfItems(in:)

**Framework**: AppKit  
**Kind**: method

Invoked when a menu is about to be displayed at the start of a tracking session so the delegate can specify the number of items in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func numberOfItems(in menu: NSMenu) -> Int
```

#### Return Value

The number of menu items in the menu.

#### Discussion

If you return a positive value, the menu is resized by either removing or adding items. Newly created items are blank. After the menu is resized, your [`menu(_:update:at:shouldCancel:)`](nsmenudelegate/menu(_:update:at:shouldcancel:).md) method is called for each item. If you return a negative value, the number of items is left unchanged and [`menu(_:update:at:shouldCancel:)`](nsmenudelegate/menu(_:update:at:shouldcancel:).md) is not called. If you can populate the menu quickly, you can implement [`menuNeedsUpdate(_:)`](nsmenudelegate/menuneedsupdate(_:).md) instead of [`numberOfItems(in:)`](nsmenudelegate/numberofitems(in:).md) and [`menu(_:update:at:shouldCancel:)`](nsmenudelegate/menu(_:update:at:shouldcancel:).md).

## Parameters

- `menu`: The menu object about to be displayed.

## See Also

- [func menuNeedsUpdate(NSMenu)](nsmenudelegate/menuneedsupdate(_:).md)
  Invoked when a menu is about to be displayed at the start of a tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/numberofitems(in:))*