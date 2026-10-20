# rowType(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the type of a given row.

**Availability**:
- macOS

## Declaration

```swift
func rowType(forRow rowIndex: Int) -> NSRuleEditor.RowType
```

```objc
- (NSRuleEditorRowType) rowTypeForRow:(NSInteger) rowIndex;
```

#### Return Value

The type of the row at `rowIndex`.

## Parameters

- `rowIndex`: The index of a row in the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if `rowIndex` is less than `0` or greater than or equal to the number of rows.

## See Also

### Obtaining Row Information
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](./parentrow%28forrow%29.md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](./row%28fordisplayvalue%29.md)
  Returns the index of the row containing a given value.
- [NSRuleEditor.RowType](./rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](./subrowindexes%28forrow%29.md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtype(forrow:))*