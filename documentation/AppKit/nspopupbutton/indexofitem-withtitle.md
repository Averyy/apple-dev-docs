# indexOfItem(withTitle:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the item with the specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withTitle title: String) -> Int
```

#### Return Value

The index of the item or `-1` if no item with the specified title was found.

## Parameters

- `title`: The title of the item you want.

## See Also

- [func index(of: NSMenuItem) -> Int](nspopupbutton/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbutton/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbutton/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtitle:))*