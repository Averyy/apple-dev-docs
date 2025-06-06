# nestingMode

**Framework**: AppKit  
**Kind**: property

The rule editor’s nesting mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var nestingMode: NSRuleEditor.NestingMode { get set }
```

#### Discussion

You typically set the nesting mode at view creation time and do not subsequently modify it. The default is `NSRuleEditorNestingModeCompound`. For a list of valid modes, see `Nesting Modes`.

## See Also

- [var isEditable: Bool](nsruleeditor/iseditable.md)
  A Boolean value that determines whether the rule editor is editable.
- [NSRuleEditor.NestingMode](nsruleeditor/nestingmode-swift.enum.md)
  Specifies a type for nesting modes.
- [var canRemoveAllRows: Bool](nsruleeditor/canremoveallrows.md)
  A Boolean value that indicates whether all the rows can be removed.
- [var rowHeight: CGFloat](nsruleeditor/rowheight.md)
  The rule editor’s row height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/nestingmode-swift.property)*