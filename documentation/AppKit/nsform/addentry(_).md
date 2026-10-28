# addEntry(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a new entry to the end of the receiver and gives it the specified title.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func addEntry(_ title: String) -> NSFormCell
```

```objc
- (NSFormCell *) addEntry:(NSString *) title;
```

## Return Value

The form cell object that was created for the entry.

## Discussion

The new entry has no tag, target, or action, but is enabled and editable.

## Parameters

- `title`: The title for the new form entry.

## See Also

### Related Documentation
- [var action: Selector?](../nsactioncell/action.md)
  Returns the receiver’s action-message selector.
- [var target: AnyObject?](../nsactioncell/target.md)
  Returns the receiver’s target object.
- [var isEnabled: Bool](../nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var isEditable: Bool](../nscell/iseditable.md)
  A Boolean value indicating whether the cell is editable.
- [var tag: Int](../nsactioncell/tag.md)
  Returns the receiver’s tag.
- [Form Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Form/Form.html#//apple_ref/doc/uid/10000021i)
### Adding and Removing Entries
- [func insertEntry(String, at: Int) -> NSFormCell!](./insertentry%28_,at%29.md)
  Inserts an entry with the specified title into the receiver.
- [func removeEntry(at: Int)](./removeentry%28at%29.md)
  Removes and releases the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/addentry(_:))*