# subrowIndexes(forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the immediate subrows of a given row.

**Availability**:
- macOS

## Declaration

```swift
func subrowIndexes(forRow rowIndex: Int) -> IndexSet
```

```objc
- (NSIndexSet *) subrowIndexesForRow:(NSInteger) rowIndex;
```

## Return Value

The immediate subrows of the row at `rowIndex`.

## Discussion

Rows are numbered starting at `0`.

## Parameters

- `rowIndex`: The index of a row in the receiver, or `-1` to get the top-level rows.

  > ❗ **Important**:  Raises an `NSRangeException` if `rowIndex` is less than `-1` or greater than or equal to the number of rows.

## See Also

### Obtaining Row Information
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](./parentrow%28forrow%29.md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](./row%28fordisplayvalue%29.md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](./rowtype%28forrow%29.md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](./rowtype.md)
  Specifies a type for row types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/subrowindexes(forrow:))*