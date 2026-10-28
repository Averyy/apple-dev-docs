# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the user can edit the value in the text field.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (getter=isEditable) BOOL editable;
```

## Discussion

If [`true`](../../Swift/true.md), the user can select and edit text. If [`false`](../../Swift/false.md), the user can’t edit text, and the ability to select the text field’s content is dependent on the value of [`isSelectable`](./isselectable.md).

For example, if an `NSTextField` object is selectable but uneditable, becomes editable for a time, and then becomes uneditable again, it remains selectable. To ensure that text is neither editable nor selectable, use [`isSelectable`](./isselectable.md) to disable text selection.

## See Also

### Controlling selection and editing
- [var isSelectable: Bool](./isselectable.md)
  A Boolean value that determines whether the user can select the content of the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/iseditable)*