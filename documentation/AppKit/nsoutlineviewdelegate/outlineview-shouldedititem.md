# outlineView(_:shouldEdit:item:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the outline view should allow editing of a given item in a given table column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldEdit tableColumn: NSTableColumn?, item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit `outlineView` to edit the cell specified by `tableColumn` and `item`, [`false`](https://developer.apple.com/documentation/Swift/false) to deny permission.

#### Discussion

If this method returns [`true`](https://developer.apple.com/documentation/Swift/true), the cell may still not be editable—for example, if you have set up a custom `NSTextFieldCell` as a data cell, it must return [`true`](https://developer.apple.com/documentation/Swift/true) for `isEditable` to allow editing.

The delegate can implement this method to disallow editing of specific cells.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.
- `item`: The item.

## See Also

- [func outlineView(NSOutlineView, setObjectValue: Any?, for: NSTableColumn?, byItem: Any?)](nsoutlineviewdatasource/outlineview(_:setobjectvalue:for:byitem:).md)
  Set the data object for a given item in a given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldedit:item:))*