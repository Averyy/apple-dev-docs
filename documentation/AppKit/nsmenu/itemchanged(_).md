# itemChanged(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a menu item is modified visually (for example, its title changes).

**Availability**:
- macOS

## Declaration

```swift
func itemChanged(_ item: NSMenuItem)
```

```objc
- (void) itemChanged:(NSMenuItem *) item;
```

#### Discussion

This method is not called for changes involving the menu item’s action, target, represented object, or tag. Posts an [`didChangeItemNotification`](./didchangeitemnotification.md).

## Parameters

- `item`: The menu item that has visually changed.

## See Also

### Adding and Removing Menu Items
- [func insertItem(NSMenuItem, at: Int)](./insertitem%28_,at%29.md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](./insertitem%28withtitle,action,keyequivalent,at%29.md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](./additem%28_%29.md)
  Adds a menu item to the end of the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](./additem%28withtitle,action,keyequivalent%29.md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](./removeitem%28_%29.md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the menu item at a specified location in the menu.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/itemchanged(_:))*