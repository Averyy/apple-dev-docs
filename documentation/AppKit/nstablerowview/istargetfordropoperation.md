# isTargetForDropOperation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether this row will draw a drop indicator based on the current dragging feedback style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isTargetForDropOperation: Bool { get set }
```

```objc
@property (getter=isTargetForDropOperation) BOOL targetForDropOperation;
```

## Discussion

When [`true`](../../Swift/true.md), the row view will draw a drop on indicator based on the current [`draggingDestinationFeedbackStyle`](../nstableview/draggingdestinationfeedbackstyle-swift.property.md).

## See Also

### Drag and Drop
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](./draggingdestinationfeedbackstyle.md)
  Specifies the dragging destination feedback style.
- [var indentationForDropOperation: CGFloat](./indentationfordropoperation.md)
  Defines the amount the drag target for a row should be indented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/istargetfordropoperation)*