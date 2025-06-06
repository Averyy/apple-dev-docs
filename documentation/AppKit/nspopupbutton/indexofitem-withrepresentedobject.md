# indexOfItem(withRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the menu item that holds the specified represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withRepresentedObject obj: Any?) -> Int
```

#### Return Value

The index of the menu item that owns the specified object, or `-1` if no such menu item was found.

#### Discussion

Represented objects bear some direct relation to the title or image of a menu item; for example, an item entitled “100” might have an `NSNumber` object encapsulating that value as its represented object. This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `obj`: The represented object associated with a menu item.

## See Also

- [func index(of: NSMenuItem) -> Int](nspopupbutton/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbutton/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withrepresentedobject:))*