# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Requests permission to end editing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textShouldEndEditing(_ textObject: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the text object should proceed to finish editing and resign first responder status. If the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false), the text object selects all of its text and remains the first responder.

#### Discussion

The [`NSMatrix`](nsmatrix.md) method returns [`false`](https://developer.apple.com/documentation/Swift/false) if the text field contains invalid contents; otherwise it returns the value passed back from [`control(_:textShouldEndEditing:)`](nscontroltexteditingdelegate/control(_:textshouldendediting:).md).

This method is invoked to let the [`NSTextField`](nstextfield.md) respond to impending loss of first-responder status. This method’s default behavior checks the text field for validity; providing that the field contents are deemed valid, and providing that the delegate responds, [`control(_:textShouldEndEditing:)`](nscontroltexteditingdelegate/control(_:textshouldendediting:).md) is sent to the receiver’s delegate (passing the receiver and `textObject` as parameters).

## Parameters

- `textObject`: The text object requesting permission to end editing.

## See Also

- [var delegate: (any NSMatrixDelegate)?](nsmatrix/delegate.md)
  The delegate for messages from the field editor.
- [func selectText(Any?)](nsmatrix/selecttext(_:).md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](nsmatrix/selecttext(atrow:column:).md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textShouldBeginEditing(NSText) -> Bool](nsmatrix/textshouldbeginediting(_:).md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](nsmatrix/textdidbeginediting(_:).md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](nsmatrix/textdidchange(_:).md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textDidEndEditing(Notification)](nsmatrix/textdidendediting(_:).md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textshouldendediting(_:))*