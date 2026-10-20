# outlineView(_:shouldEdit:item:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the outline view should allow editing of a given item in a given table column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldEdit tableColumn: NSTableColumn?, item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldEditTableColumn:(NSTableColumn *) tableColumn item:(id) item;
```

#### Return Value

[`true`](../../Swift/true.md) to permit `outlineView` to edit the cell specified by `tableColumn` and `item`, [`false`](../../Swift/false.md) to deny permission.

#### Discussion

If this method returns [`true`](../../Swift/true.md), the cell may still not be editable—for example, if you have set up a custom `NSTextFieldCell` as a data cell, it must return [`true`](../../Swift/true.md) for `isEditable` to allow editing.

The delegate can implement this method to disallow editing of specific cells.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.
- `item`: The item.

## See Also

### Related Documentation
- [func outlineView(NSOutlineView, setObjectValue: Any?, for: NSTableColumn?, byItem: Any?)](../nsoutlineviewdatasource/outlineview%28_,setobjectvalue,for,byitem%29.md)
  Set the data object for a given item in a given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldedit:item:))*