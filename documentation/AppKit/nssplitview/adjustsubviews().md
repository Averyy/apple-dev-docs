# adjustSubviews()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.

**Availability**:
- macOS

## Declaration

```swift
func adjustSubviews()
```

```objc
- (void) adjustSubviews;
```

## Discussion

When you call this method, the split view’s subviews resize proportionally; the relative sizes of the subviews don’t change.

The default implementation of this method resizes subviews proportionally so that the ratio of heights (when using horizontal dividers) or widths (when using vertical dividers) doesn’t change, even though the absolute sizes change.

Call this method on split views where you’ve added or removed subviews to reestablish the consistency of subview placement.

This method invalidates the cursor when it is over a divider, ensuring the cursor is always of the correct type during and after resizing animations.

## See Also

### Managing Subviews
- [func isSubviewCollapsed(NSView) -> Bool](./issubviewcollapsed%28_%29.md)
  Returns whether the specified view is in a collapsed state.
- [func holdingPriorityForSubview(at: Int) -> NSLayoutConstraint.Priority](./holdingpriorityforsubview%28at%29.md)
  Returns the priority of the subview’s width or height when resizing.
- [func setHoldingPriority(NSLayoutConstraint.Priority, forSubviewAt: Int)](./setholdingpriority%28_,forsubviewat%29.md)
  Sets the priority for split view subviews to maintain their width or height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/adjustsubviews())*