# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to end editing.

**Availability**:
- macOS

## Declaration

```swift
func textShouldEndEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldEndEditing:(NSText *) textObject;
```

#### Return Value

[`true`](../../Swift/true.md) if the text object should proceed to finish editing and resign first responder status. If the delegate returns [`false`](../../Swift/false.md), the text object selects all of its text and remains the first responder.

#### Discussion

The [`NSMatrix`](../nsmatrix.md) method returns [`false`](../../Swift/false.md) if the text field contains invalid contents; otherwise it returns the value passed back from [`control(_:textShouldEndEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldendediting%29.md).

This method is invoked to let the [`NSTextField`](../nstextfield.md) respond to impending loss of first-responder status. This method’s default behavior checks the text field for validity; providing that the field contents are deemed valid, and providing that the delegate responds, [`control(_:textShouldEndEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldendediting%29.md) is sent to the receiver’s delegate (passing the receiver and `textObject` as parameters).

## Parameters

- `textObject`: The text object requesting permission to end editing.

## See Also

### Related Documentation
- [var delegate: (any NSMatrixDelegate)?](./delegate.md)
  The delegate for messages from the field editor.
### Editing Text in Cells
- [func selectText(Any?)](./selecttext%28_%29.md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](./selecttext%28atrow,column%29.md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textshouldendediting(_:))*