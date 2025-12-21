# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Requests permission to begin editing text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the text object should proceed to make changes. If the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false), the text object abandons the editing operation.

#### Discussion

The default behavior of this method is to return the value obtained from [`control(_:textShouldBeginEditing:)`](nscontroltexteditingdelegate/control(_:textshouldbeginediting:).md), unless the delegate doesn’t respond to that method, in which case it returns [`true`](https://developer.apple.com/documentation/Swift/true), thereby allowing text editing to proceed.

This method is invoked to let the [`NSTextField`](nstextfield.md) respond to impending changes to its text. This method’s default behavior is to send [`control(_:textShouldBeginEditing:)`](nscontroltexteditingdelegate/control(_:textshouldbeginediting:).md) to the receiver’s delegate (passing the receiver and `textObject` as parameters).

## Parameters

- `textObject`: The text object requesting permission to begin editing.

## See Also

- [var delegate: (any NSMatrixDelegate)?](nsmatrix/delegate.md)
  The delegate for messages from the field editor.
- [func selectText(Any?)](nsmatrix/selecttext(_:).md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](nsmatrix/selecttext(atrow:column:).md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textDidBeginEditing(Notification)](nsmatrix/textdidbeginediting(_:).md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](nsmatrix/textdidchange(_:).md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](nsmatrix/textshouldendediting(_:).md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](nsmatrix/textdidendediting(_:).md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textshouldbeginediting(_:))*