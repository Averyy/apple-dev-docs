# NSRuleEditor.NestingMode

**Framework**: AppKit  
**Kind**: enum

Specifies a type for nesting modes.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NestingMode
```

#### Overview

See `Nesting Modes` for possible values.

## Topics

### Modes
- [NSRuleEditor.NestingMode.compound](nsruleeditor/nestingmode-swift.enum/compound.md)
  Unlimited nesting and compound rows.
- [NSRuleEditor.NestingMode.list](nsruleeditor/nestingmode-swift.enum/list.md)
  Allows a single list, with no nesting and no compound rows.
- [NSRuleEditor.NestingMode.simple](nsruleeditor/nestingmode-swift.enum/simple.md)
  One compound row at the top with subrows beneath it, and no further nesting allowed.
- [NSRuleEditor.NestingMode.single](nsruleeditor/nestingmode-swift.enum/single.md)
  Only a single row is allowed.
### Initializers
- [init?(rawValue: UInt)](nsruleeditor/nestingmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isEditable: Bool](nsruleeditor/iseditable.md)
  A Boolean value that determines whether the rule editor is editable.
- [var nestingMode: NSRuleEditor.NestingMode](nsruleeditor/nestingmode-swift.property.md)
  The rule editor’s nesting mode.
- [var canRemoveAllRows: Bool](nsruleeditor/canremoveallrows.md)
  A Boolean value that indicates whether all the rows can be removed.
- [var rowHeight: CGFloat](nsruleeditor/rowheight.md)
  The rule editor’s row height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/nestingmode-swift.enum)*