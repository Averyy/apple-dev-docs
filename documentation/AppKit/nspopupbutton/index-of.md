# index(of:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the specified menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func index(of item: NSMenuItem) -> Int
```

#### Return Value

The index of the item or `-1` if no such item was found.

#### Discussion

This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `item`: The menu item whose index you want.

## See Also

- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbutton/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbutton/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/index(of:))*