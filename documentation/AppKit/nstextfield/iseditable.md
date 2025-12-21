# isEditable

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the user can edit the value in the text field.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEditable: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the user can select and edit text. If [`false`](https://developer.apple.com/documentation/Swift/false), the user can’t edit text, and the ability to select the text field’s content is dependent on the value of [`isSelectable`](nstextfield/isselectable.md).

For example, if an `NSTextField` object is selectable but uneditable, becomes editable for a time, and then becomes uneditable again, it remains selectable. To ensure that text is neither editable nor selectable, use [`isSelectable`](nstextfield/isselectable.md) to disable text selection.

## See Also

- [var isSelectable: Bool](nstextfield/isselectable.md)
  A Boolean value that determines whether the user can select the content of the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/iseditable)*