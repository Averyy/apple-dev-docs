# numberOfRows

**Framework**: AppKit  
**Kind**: property

The number of rows in the rule editor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfRows: Int { get }
```

## See Also

- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/numberofrows)*