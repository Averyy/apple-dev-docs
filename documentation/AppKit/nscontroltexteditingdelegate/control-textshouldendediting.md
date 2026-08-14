# control(_:textShouldEndEditing:)

**Framework**: AppKit  
**Kind**: method

Invoked when the insertion point tries to leave a cell of the control that has been edited.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, textShouldEndEditing fieldEditor: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the insertion point should be allowed to end the editing session; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This message is sent only by controls that allow editing of text (such as a text field or a form field). This message is sent by the control directly to its delegate object.

## Parameters

- `control`: The control for which editing is about to end.
- `fieldEditor`: The field editor of the control. You can use this parameter to get the edited text.

## See Also

- [func control(NSControl, textShouldBeginEditing: NSText) -> Bool](nscontroltexteditingdelegate/control(_:textshouldbeginediting:).md)
  Invoked when the user tries to enter a character in a cell of a control that allows editing of text (such as a text field or form field).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:textshouldendediting:))*