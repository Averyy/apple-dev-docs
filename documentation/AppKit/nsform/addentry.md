# addEntry(_:)

**Framework**: AppKit  
**Kind**: method

Adds a new entry to the end of the receiver and gives it the specified title.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func addEntry(_ title: String) -> NSFormCell
```

#### Return Value

The form cell object that was created for the entry.

#### Discussion

The new entry has no tag, target, or action, but is enabled and editable.

## Parameters

- `title`: The title for the new form entry.

## See Also

- [var action: Selector?](nsactioncell/action.md)
  Returns the receiver’s action-message selector.
- [var target: AnyObject?](nsactioncell/target.md)
  Returns the receiver’s target object.
- [var isEnabled: Bool](nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var isEditable: Bool](nscell/iseditable.md)
  A Boolean value indicating whether the cell is editable.
- [var tag: Int](nsactioncell/tag.md)
  Returns the receiver’s tag.
- [Form Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Form/Form.html#//apple_ref/doc/uid/10000021i)
- [Matrix Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Matrix.html#//apple_ref/doc/uid/10000022i)
- [func insertEntry(String, at: Int) -> NSFormCell!](nsform/insertentry(_:at:).md)
  Inserts an entry with the specified title into the receiver.
- [func removeEntry(at: Int)](nsform/removeentry(at:).md)
  Removes and releases the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/addentry(_:))*