# control(_:textShouldBeginEditing:)

**Framework**: AppKit  
**Kind**: method

Invoked when the user tries to enter a character in a cell of a control that allows editing of text (such as a text field or form field).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func control(_ control: NSControl, textShouldBeginEditing fieldEditor: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the control’s field editor should be allowed to start editing the text; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

You can use this method to allow or disallow editing in a control. This message is sent by the control directly to its delegate object.

## Parameters

- `control`: The control whose content is about to be edited.
- `fieldEditor`: The field editor of the control.

## See Also

- [func control(NSControl, textShouldEndEditing: NSText) -> Bool](nscontroltexteditingdelegate/control(_:textshouldendediting:).md)
  Invoked when the insertion point tries to leave a cell of the control that has been edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/control(_:textshouldbeginediting:))*