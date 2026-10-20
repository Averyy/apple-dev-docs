# NSRuleEditor.RowType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Specifies a type for row types.

**Availability**:
- macOS

## Declaration

```swift
enum RowType
```

```c
enum NSRuleEditorRowType : NSUInteger;
```

#### Overview

See `Row Types` for possible values.

## Topics

### Enumeration Cases
- [NSRuleEditor.RowType.compound](./rowtype/compound.md)
  Specifies a compound row.
- [NSRuleEditor.RowType.simple](./rowtype/simple.md)
  Specifies a simple row.
### Initializers
- [init?(rawValue: UInt)](./rowtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func subrowIndexes(forRow: Int) -> IndexSet](./subrowindexes%28forrow%29.md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtype)*