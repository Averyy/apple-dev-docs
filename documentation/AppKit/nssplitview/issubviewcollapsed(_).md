# isSubviewCollapsed(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified view is in a collapsed state.

**Availability**:
- macOS

## Declaration

```swift
func isSubviewCollapsed(_ subview: NSView) -> Bool
```

```objc
- (BOOL) isSubviewCollapsed:(NSView *) subview;
```

#### Return Value

[`true`](../../Swift/true.md) if `subview` is in a collapsed state; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `subview`: The subview in the split view.

## See Also

### Managing Subviews
- [func adjustSubviews()](./adjustsubviews%28%29.md)
  Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.
- [func holdingPriorityForSubview(at: Int) -> NSLayoutConstraint.Priority](./holdingpriorityforsubview%28at%29.md)
  Returns the priority of the subview’s width or height when resizing.
- [func setHoldingPriority(NSLayoutConstraint.Priority, forSubviewAt: Int)](./setholdingpriority%28_,forsubviewat%29.md)
  Sets the priority for split view subviews to maintain their width or height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/issubviewcollapsed(_:))*