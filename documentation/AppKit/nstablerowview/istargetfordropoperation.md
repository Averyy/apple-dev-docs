# isTargetForDropOperation

**Framework**: AppKit  
**Kind**: property

Specifies whether this row will draw a drop indicator based on the current dragging feedback style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isTargetForDropOperation: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), the row view will draw a drop on indicator based on the current [`draggingDestinationFeedbackStyle`](nstableview/draggingdestinationfeedbackstyle-swift.property.md).

## See Also

- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstablerowview/draggingdestinationfeedbackstyle.md)
  Specifies the dragging destination feedback style.
- [var indentationForDropOperation: CGFloat](nstablerowview/indentationfordropoperation.md)
  Defines the amount the drag target for a row should be indented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/istargetfordropoperation)*