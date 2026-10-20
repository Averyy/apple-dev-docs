# splitView(_:shouldHideDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the split view controller to determine whether the user can drag a divider or adjust it off the edge of the split view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, shouldHideDividerAt dividerIndex: Int) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView shouldHideDividerAtIndex:(NSInteger) dividerIndex;
```

#### Discussion

By default, [`NSSplitViewController`](../nssplitviewcontroller.md) hides the first and last dividers if their outer neighbor is in a collapsed state.

## See Also

### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](./splitview%28_,effectiverect,fordrawnrect,ofdividerat%29.md)
  Allows the split view controller to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, additionalEffectiveRectOfDividerAt: Int) -> NSRect](./splitview%28_,additionaleffectiverectofdividerat%29.md)
  Allows the split view controller to return an additional rectangle where mouse clicks can initiate divider dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:shouldhidedividerat:))*