# insertItem(withTitle:action:keyEquivalent:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates and adds a menu item at a specified location in the menu.

**Availability**:
- macOS

## Declaration

```swift
func insertItem(withTitle string: String, action selector: Selector?, keyEquivalent charCode: String, at index: Int) -> NSMenuItem
```

```objc
- (NSMenuItem *) insertItemWithTitle:(NSString *) string action:(SEL) selector keyEquivalent:(NSString *) charCode atIndex:(NSInteger) index;
```

## Return Value

The new menu item (an object conforming to the NSMenuItem protocol) or `nil` if the item could not be created

## Parameters

- `string`: A string to be made the title of the menu item.
- `selector`: The action-message selector to assign to the menu item.
- `charCode`: A string identifying the key to use as a key equivalent for the menu item. If you do not want the menu item to have a key equivalent, `keyEquiv` should be an empty string (`@""`) and not `nil`.
- `index`: An integer index identifying the location of the menu item in the menu.

## See Also

### Adding and Removing Menu Items
- [func insertItem(NSMenuItem, at: Int)](./insertitem%28_,at%29.md)
  Inserts a menu item into the menu at a specific location.
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
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/insertitem(withtitle:action:keyequivalent:at:))*