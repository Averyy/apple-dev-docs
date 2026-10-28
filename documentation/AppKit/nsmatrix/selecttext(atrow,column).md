# selectText(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the text in the cell at the specified location and returns the cell.

**Availability**:
- macOS

## Declaration

```swift
func selectText(atRow row: Int, column col: Int) -> NSCell?
```

```objc
- (NSCell *) selectTextAtRow:(NSInteger) row column:(NSInteger) col;
```

## Return Value

If it is both editable and selectable, the cell at the specified row and column. If the cell at the specified location, is either not editable or not selectable, this method does nothing and returns nil. If `row` and `column` indicate a cell that is outside the receiver, this method does nothing and returns the receiver.

## Parameters

- `row`: The row containing the text to select.
- `col`: The column containing the text to select.

## See Also

### Editing Text in Cells
- [func selectText(Any?)](./selecttext%28_%29.md)
  Selects text in the currently selected cell or in the key cell.
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selecttext(atrow:column:))*