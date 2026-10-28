# insertRow(at:with:asSubrowOfRow:animate:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a new row of a given type at a given location.

**Availability**:
- macOS

## Declaration

```swift
func insertRow(at rowIndex: Int, with rowType: NSRuleEditor.RowType, asSubrowOfRow parentRow: Int, animate shouldAnimate: Bool)
```

```objc
- (void) insertRowAtIndex:(NSInteger) rowIndex withType:(NSRuleEditorRowType) rowType asSubrowOfRow:(NSInteger) parentRow animate:(BOOL) shouldAnimate;
```

## Discussion

> ❗ **Important**:  If `parentRow` is greater than or equal to `rowIndex`, or if `rowIndex` would fall amongst the children of some other parent, or if the nesting mode forbids this configuration, an `NSInvalidArgumentException` is raised.

## Parameters

- `rowIndex`: The index at which the new row should be inserted. `rowIndex` must be greater than `parentRow`, and much specify a row that does not fall amongst the children of some other parent.
- `rowType`: The type of the new row.
- `parentRow`: The index of the row of which the new row is a child. Pass `-1` to indicate that the new row should be a root row.
- `shouldAnimate`: [`true`](../../Swift/true.md) if creation of the new row should be animated, otherwise [`false`](../../Swift/false.md).

## See Also

### Manipulating Rows
- [func addRow(Any?)](./addrow%28_%29.md)
  Adds a row to the receiver.
- [func removeRow(at: Int)](./removerow%28at%29.md)
  Removes the row at a given index.
- [func removeRows(at: IndexSet, includeSubrows: Bool)](./removerows%28at,includesubrows%29.md)
  Removes the rows at given indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/insertrow(at:with:assubrowofrow:animate:))*