# menu(_:update:at:shouldCancel:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to let the delegate update a menu item before it is displayed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func menu(_ menu: NSMenu, update item: NSMenuItem, at index: Int, shouldCancel: Bool) -> Bool
```

```objc
- (BOOL) menu:(NSMenu *) menu updateItem:(NSMenuItem *) item atIndex:(NSInteger) index shouldCancel:(BOOL) shouldCancel;
```

#### Return Value

[`true`](../../Swift/true.md) to continue the process. If you return [`false`](../../Swift/false.md), your [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md) is not called again. In that case, it’s your responsibility to trim any extra items from the menu.

#### Discussion

If your [`numberOfItems(in:)`](./numberofitems%28in%29.md) delegate method returns a positive value, then your [`menu(_:update:at:shouldCancel:)`](./menu%28_,update,at,shouldcancel%29.md) method is called for each item in the menu. You can then update the menu title, image, and so forth for each menu item.

## Parameters

- `menu`: The menu object that owns `item`.
- `item`: The menu-item object that may be updated.
- `index`: The integer index of the menu item.
- `shouldCancel`: Set to [`true`](../../Swift/true.md) if, due to some user action, the menu no longer needs to be displayed before all the menu items have been updated. You can ignore this flag, return [`true`](../../Swift/true.md), and continue; or you can save your work (to save time the next time your delegate is called) and return [`false`](../../Swift/false.md) to stop the updating.

## See Also

### Updating Menu Layout
- [func confinementRect(for: NSMenu, on: NSScreen?) -> NSRect](./confinementrect%28for,on%29.md)
  Invoked to allow the delegate to specify a display location for the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenudelegate/menu(_:update:at:shouldcancel:))*