# numberOfItems(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a menu is about to be displayed at the start of a tracking session so the delegate can specify the number of items in the menu.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func numberOfItems(in menu: NSMenu) -> Int
```

```objc
- (NSInteger) numberOfItemsInMenu:(NSMenu *) menu;
```

#### Return Value

The number of menu items in the menu.

#### Discussion

If you return a positive value, the menu is resized by either removing or adding items. Newly created items are blank. After the menu is resized, your [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md) method is called for each item. If you return a negative value, the number of items is left unchanged and [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md) is not called. If you can populate the menu quickly, you can implement [`menuNeedsUpdate(_:)`](./menuneedsupdate%28_%29.md) instead of [`numberOfItems(in:)`](./numberofitems%28in%29.md) and [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md).

## Parameters

- `menu`: The menu object about to be displayed.

## See Also

### Handling Tracking
- [func menuNeedsUpdate(NSMenu)](./menuneedsupdate%28_%29.md)
  Invoked when a menu is about to be displayed at the start of a tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/numberofitems(in:))*