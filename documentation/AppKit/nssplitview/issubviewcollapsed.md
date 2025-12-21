# isSubviewCollapsed(_:)

**Framework**: AppKit  
**Kind**: method

Returns whether the specified view is in a collapsed state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isSubviewCollapsed(_ subview: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `subview` is in a collapsed state; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `subview`: The subview in the split view.

## See Also

- [func adjustSubviews()](nssplitview/adjustsubviews.md)
  Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.
- [func holdingPriorityForSubview(at: Int) -> NSLayoutConstraint.Priority](nssplitview/holdingpriorityforsubview(at:).md)
  Returns the priority of the subview’s width or height when resizing.
- [func setHoldingPriority(NSLayoutConstraint.Priority, forSubviewAt: Int)](nssplitview/setholdingpriority(_:forsubviewat:).md)
  Sets the priority for split view subviews to maintain their width or height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/issubviewcollapsed(_:))*