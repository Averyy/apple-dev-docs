# menuNeedsUpdate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a menu is about to be displayed at the start of a tracking session.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func menuNeedsUpdate(_ menu: NSMenu)
```

```objc
- (void) menuNeedsUpdate:(NSMenu *) menu;
```

#### Discussion

Using this method, the delegate can change the menu by adding, removing, or modifying menu items. If populating the menu will take a long time, implement [`numberOfItems(in:)`](./numberofitems%28in%29.md) and [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md) instead.

Menu item validation occurs after this method is called. If the menu is updated because the user pressed a command key, only the menu item with the matching command key is validated; if the menu is updated because the user opened it, then every menu item is validated.

## Parameters

- `menu`: The menu object that is about to be displayed.

## See Also

### Handling Tracking
- [func numberOfItems(in: NSMenu) -> Int](./numberofitems%28in%29.md)
  Invoked when a menu is about to be displayed at the start of a tracking session so the delegate can specify the number of items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menuneedsupdate(_:))*