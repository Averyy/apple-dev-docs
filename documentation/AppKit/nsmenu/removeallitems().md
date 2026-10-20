# removeAllItems()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all the menu items in the menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func removeAllItems()
```

```objc
- (void) removeAllItems;
```

#### Discussion

This method is more efficient than removing menu items individually.

Unlike the other remove methods, this method does not post [`didChangeItemNotification`](./didchangeitemnotification.md) notifications.

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
- [func itemChanged(NSMenuItem)](./itemchanged%28_%29.md)
  Invoked when a menu item is modified visually (for example, its title changes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/removeallitems())*