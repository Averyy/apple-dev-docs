# isSelectable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user can select the content of the text field.

**Availability**:
- macOS

## Declaration

```swift
var isSelectable: Bool { get set }
```

```objc
@property (getter=isSelectable) BOOL selectable;
```

#### Discussion

If [`true`](../../Swift/true.md), the text field becomes selectable but not editable. Use [`isEditable`](./iseditable.md) to make the text field selectable and editable. If [`false`](../../Swift/false.md), the text is neither editable nor selectable.

## See Also

### Controlling selection and editing
- [var isEditable: Bool](./iseditable.md)
  A Boolean value that controls whether the user can edit the value in the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/isselectable)*