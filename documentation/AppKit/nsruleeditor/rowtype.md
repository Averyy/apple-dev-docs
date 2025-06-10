# NSRuleEditor.RowType

**Framework**: AppKit  
**Kind**: enum

Specifies a type for row types.

**Availability**:
- macOS ?+

## Declaration

```swift
enum RowType
```

#### Overview

See `Row Types` for possible values.

## Topics

### Enumeration Cases
- [NSRuleEditor.RowType.compound](nsruleeditor/rowtype/compound.md)
  Specifies a compound row.
- [NSRuleEditor.RowType.simple](nsruleeditor/rowtype/simple.md)
  Specifies a simple row.
### Initializers
- [init?(rawValue: UInt)](nsruleeditor/rowtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtype)*