# holdingPriorityForSubview(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the priority of the subview’s width or height when resizing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func holdingPriorityForSubview(at subviewIndex: Int) -> NSLayoutConstraint.Priority
```

```objc
- (NSLayoutPriority) holdingPriorityForSubviewAtIndex:(NSInteger) subviewIndex;
```

#### Return Value

The layout priority of the subview at the index.

#### Discussion

The priority is the manner that the split view subviews use to maintain their width (for a vertical split view) or height (for a horizontal split view). During a split view resize, subviews with higher priorities maintain their sizes before subviews with lower priorities. The subview with the lowest priority is the first to gain additional thickness if the split view grows or shrinks.

## Parameters

- `subviewIndex`: The index of the subview.

## See Also

### Managing Subviews
- [func adjustSubviews()](./adjustsubviews%28%29.md)
  Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.
- [func isSubviewCollapsed(NSView) -> Bool](./issubviewcollapsed%28_%29.md)
  Returns whether the specified view is in a collapsed state.
- [func setHoldingPriority(NSLayoutConstraint.Priority, forSubviewAt: Int)](./setholdingpriority%28_,forsubviewat%29.md)
  Sets the priority for split view subviews to maintain their width or height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/holdingpriorityforsubview(at:))*