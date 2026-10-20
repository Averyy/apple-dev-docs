# NSRuleEditor.NestingMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Specifies a type for nesting modes.

**Availability**:
- macOS

## Declaration

```swift
enum NestingMode
```

```c
enum NSRuleEditorNestingMode : NSUInteger;
```

#### Overview

See `Nesting Modes` for possible values.

## Topics

### Modes
- [NSRuleEditor.NestingMode.compound](./nestingmode-swift.enum/compound.md)
  Unlimited nesting and compound rows.
- [NSRuleEditor.NestingMode.list](./nestingmode-swift.enum/list.md)
  Allows a single list, with no nesting and no compound rows.
- [NSRuleEditor.NestingMode.simple](./nestingmode-swift.enum/simple.md)
  One compound row at the top with subrows beneath it, and no further nesting allowed.
- [NSRuleEditor.NestingMode.single](./nestingmode-swift.enum/single.md)
  Only a single row is allowed.
### Initializers
- [init?(rawValue: UInt)](./nestingmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a Rule Editor
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that determines whether the rule editor is editable.
- [var nestingMode: NSRuleEditor.NestingMode](./nestingmode-swift.property.md)
  The rule editor’s nesting mode.
- [var canRemoveAllRows: Bool](./canremoveallrows.md)
  A Boolean value that indicates whether all the rows can be removed.
- [var rowHeight: CGFloat](./rowheight.md)
  The rule editor’s row height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/nestingmode-swift.enum)*