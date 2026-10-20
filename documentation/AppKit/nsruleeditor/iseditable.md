# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the rule editor is editable.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (getter=isEditable) BOOL editable;
```

#### Discussion

The default is [`true`](../../Swift/true.md).

## See Also

### Configuring a Rule Editor
- [var nestingMode: NSRuleEditor.NestingMode](./nestingmode-swift.property.md)
  The rule editor’s nesting mode.
- [NSRuleEditor.NestingMode](./nestingmode-swift.enum.md)
  Specifies a type for nesting modes.
- [var canRemoveAllRows: Bool](./canremoveallrows.md)
  A Boolean value that indicates whether all the rows can be removed.
- [var rowHeight: CGFloat](./rowheight.md)
  The rule editor’s row height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/iseditable)*