# indexOfItem(withTag:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the menu item with the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withTag tag: Int) -> Int
```

#### Return Value

The index of the item or `-1` if no item with the specified tag was found.

#### Discussion

This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `tag`: The tag of the menu item you want.

## See Also

- [func index(of: NSMenuItem) -> Int](nspopupbutton/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbutton/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbutton/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtag:))*