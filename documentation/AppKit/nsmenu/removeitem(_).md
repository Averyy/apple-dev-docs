# removeItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a menu item from the menu.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(_ item: NSMenuItem)
```

```objc
- (void) removeItem:(NSMenuItem *) item;
```

## Parameters

- `item`: The menu item to remove.

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
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](./itemchanged%28_%29.md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/removeitem(_:))*