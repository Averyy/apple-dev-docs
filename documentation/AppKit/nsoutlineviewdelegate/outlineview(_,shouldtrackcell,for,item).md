# outlineView(_:shouldTrackCell:for:item:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a given cell should be tracked.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldTrackCell cell: NSCell, for tableColumn: NSTableColumn?, item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldTrackCell:(NSCell *) cell forTableColumn:(NSTableColumn *) tableColumn item:(id) item;
```

#### Return Value

[`true`](../../Swift/true.md) if the cell should be tracked for the item `item` in column `tableColumn`, otherwise [`false`](../../Swift/false.md).

#### Discussion

Normally, only selectable or selected cells can be tracked. If you implement this method, cells which are not selectable or selected can be tracked (and vice-versa). For example, this allows you to have a button cell in a table which does not change the selection, but can still be clicked on and tracked.

## Parameters

- `outlineView`: The outline view that sent the message.
- `cell`: The cell used to display item `item` in column `tableColumn`
- `tableColumn`: A table column in the outline view.
- `item`: An item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldtrackcell:for:item:))*