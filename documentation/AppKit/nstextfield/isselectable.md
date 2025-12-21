# isSelectable

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the user can select the content of the text field.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isSelectable: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the text field becomes selectable but not editable. Use [`isEditable`](nstextfield/iseditable.md) to make the text field selectable and editable. If [`false`](https://developer.apple.com/documentation/Swift/false), the text is neither editable nor selectable.

## See Also

- [var isEditable: Bool](nstextfield/iseditable.md)
  A Boolean value that controls whether the user can edit the value in the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/isselectable)*