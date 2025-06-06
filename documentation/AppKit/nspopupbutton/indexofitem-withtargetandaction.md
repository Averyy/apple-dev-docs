# indexOfItem(withTarget:andAction:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the menu item with the specified target and action.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withTarget target: Any?, andAction actionSelector: Selector?) -> Int
```

#### Return Value

The index of the menu item, or `-1` if no menu item contains the specified target and action.

#### Discussion

If you specify `NULL` for the `actionSelector` parameter, the index of the first menu item with the specified target is returned. This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `target`: The target object associated with the menu item.
- `actionSelector`: The action method associated with the menu item.

## See Also

- [func index(of: NSMenuItem) -> Int](nspopupbutton/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbutton/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtarget:andaction:))*