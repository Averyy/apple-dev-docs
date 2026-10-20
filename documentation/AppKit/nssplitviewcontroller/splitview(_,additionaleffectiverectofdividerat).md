# splitView(_:additionalEffectiveRectOfDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the split view controller to return an additional rectangle where mouse clicks can initiate divider dragging.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, additionalEffectiveRectOfDividerAt dividerIndex: Int) -> NSRect
```

```objc
- (NSRect) splitView:(NSSplitView *) splitView additionalEffectiveRectOfDividerAtIndex:(NSInteger) dividerIndex;
```

## See Also

### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](./splitview%28_,effectiverect,fordrawnrect,ofdividerat%29.md)
  Allows the split view controller to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](./splitview%28_,shouldhidedividerat%29.md)
  Allows the split view controller to determine whether the user can drag a divider or adjust it off the edge of the split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:additionaleffectiverectofdividerat:))*