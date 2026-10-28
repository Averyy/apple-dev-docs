# addItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a menu item to the end of the menu.

**Availability**:
- macOS

## Declaration

```swift
func addItem(_ newItem: NSMenuItem)
```

```objc
- (void) addItem:(NSMenuItem *) newItem;
```

## Discussion

This method invokes [`insertItem(_:at:)`](./insertitem%28_,at%29.md). Thus, the menu does not accept the menu item if it already belongs to another menu. After adding the menu item, the menu updates itself.

## Parameters

- `newItem`: The menu item (an object conforming to the NSMenuItem protocol) to add to the menu.

## See Also

### Adding and Removing Menu Items
- [func insertItem(NSMenuItem, at: Int)](./insertitem%28_,at%29.md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](./insertitem%28withtitle,action,keyequivalent,at%29.md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](./additem%28withtitle,action,keyequivalent%29.md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](./removeitem%28_%29.md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](./itemchanged%28_%29.md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/additem(_:))*