# row(forDisplayValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the row containing a given value.

**Availability**:
- macOS

## Declaration

```swift
func row(forDisplayValue displayValue: Any) -> Int
```

```objc
- (NSInteger) rowForDisplayValue:(id) displayValue;
```

#### Return Value

The index of the row containing `displayValue`, or `NSNotFound`.

#### Discussion

This method searches each row via pointer equality for the given display value, which may be present as an alternative in a popup menu for that row.

## Parameters

- `displayValue`: The display value (string, view, or menu item) of an item in the receiver. This value must not be `nil`.

  > ❗ **Important**:  Raises `NSInvalidArgumentException` if `displayValue` is `nil`.

## See Also

### Obtaining Row Information
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](./parentrow%28forrow%29.md)
  Returns the index of the parent of a given row.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](./rowtype%28forrow%29.md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](./rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](./subrowindexes%28forrow%29.md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/row(fordisplayvalue:))*