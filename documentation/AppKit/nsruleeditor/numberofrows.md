# numberOfRows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of rows in the rule editor.

**Availability**:
- macOS

## Declaration

```swift
var numberOfRows: Int { get }
```

```objc
@property (readonly) NSInteger numberOfRows;
```

## See Also

### Obtaining Row Information
- [func parentRow(forRow: Int) -> Int](./parentrow%28forrow%29.md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](./row%28fordisplayvalue%29.md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](./rowtype%28forrow%29.md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](./rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](./subrowindexes%28forrow%29.md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/numberofrows)*