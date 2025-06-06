# setHoldingPriority(_:forSubviewAt:)

**Framework**: AppKit  
**Kind**: method

Sets the priority for split view subviews to maintain their width or height.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func setHoldingPriority(_ priority: NSLayoutConstraint.Priority, forSubviewAt subviewIndex: Int)
```

#### Discussion

Calling this method sets the priority that split view subviews use to maintain their width (for a vertical split view) or height (for a horizontal split view). During a split view resize, subviews with higher priorities maintain their sizes before subviews with lower priorities. The subview with the lowest priority is the first to gain additional thickness if the split view grows or shrinks.

The default priority is [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md). Use priorities less than [`dragThatCannotResizeWindow`](nslayoutconstraint/priority-swift.struct/dragthatcannotresizewindow.md).

## Parameters

- `priority`: The priority.
- `subviewIndex`: The index of the subview

## See Also

- [func adjustSubviews()](nssplitview/adjustsubviews.md)
  Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.
- [func isSubviewCollapsed(NSView) -> Bool](nssplitview/issubviewcollapsed(_:).md)
  Returns whether the specified view is in a collapsed state.
- [func holdingPriorityForSubview(at: Int) -> NSLayoutConstraint.Priority](nssplitview/holdingpriorityforsubview(at:).md)
  Returns the priority of the subview’s width or height when resizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/setholdingpriority(_:forsubviewat:))*