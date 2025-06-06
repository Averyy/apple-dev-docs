# doubleAction

**Framework**: AppKit  
**Kind**: property

The message sent to the table view’s target when the user double-clicks a cell or column header.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var doubleAction: Selector? { get set }
```

#### Discussion

This property stores a selector that corresponds to a method of the following form:

```objc
-(void)myCustomMethod:(id)sender
```

When the user double-clicks a cell or column header, the table calls the specified method of its [`target`](nscontrol/target.md) object. The default value of this property is nil. If you do not specify a value for this property, the table view begins editing the cell.

The [`clickedRow`](nstableview/clickedrow.md) and [`clickedColumn`](nstableview/clickedcolumn.md) properties allow you to determine which row and column the double-click occurred in or if, rather than in a row, the double-click occurred in a column heading.

Note that if the table view uses Cocoa bindings and the Double Click Target binding is bound, both messages are invoked on their respective targets: First the Cocoa binding message is sent, then the `setDoubleAction:` message.

## See Also

- [var target: AnyObject?](nscontrol/target.md)
  The target object that receives action messages from the cell.
- [var clickedColumn: Int](nstableview/clickedcolumn.md)
  The index of the column the user clicked.
- [var clickedRow: Int](nstableview/clickedrow.md)
  The index of the row the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/doubleaction)*