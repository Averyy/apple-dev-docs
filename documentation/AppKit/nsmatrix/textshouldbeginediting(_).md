# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to begin editing text.

**Availability**:
- macOS

## Declaration

```swift
func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldBeginEditing:(NSText *) textObject;
```

#### Return Value

[`true`](../../Swift/true.md) if the text object should proceed to make changes. If the delegate returns [`false`](../../Swift/false.md), the text object abandons the editing operation.

#### Discussion

The default behavior of this method is to return the value obtained from [`control(_:textShouldBeginEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldbeginediting%29.md), unless the delegate doesn’t respond to that method, in which case it returns [`true`](../../Swift/true.md), thereby allowing text editing to proceed.

This method is invoked to let the [`NSTextField`](../nstextfield.md) respond to impending changes to its text. This method’s default behavior is to send [`control(_:textShouldBeginEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldbeginediting%29.md) to the receiver’s delegate (passing the receiver and `textObject` as parameters).

## Parameters

- `textObject`: The text object requesting permission to begin editing.

## See Also

### Related Documentation
- [var delegate: (any NSMatrixDelegate)?](./delegate.md)
  The delegate for messages from the field editor.
### Editing Text in Cells
- [func selectText(Any?)](./selecttext%28_%29.md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](./selecttext%28atrow,column%29.md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textshouldbeginediting(_:))*