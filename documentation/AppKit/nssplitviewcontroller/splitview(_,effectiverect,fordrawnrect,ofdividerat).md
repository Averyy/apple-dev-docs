# splitView(_:effectiveRect:forDrawnRect:ofDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the split view controller to modify the rectangle where mouse clicks initiate divider dragging.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, effectiveRect proposedEffectiveRect: NSRect, forDrawnRect drawnRect: NSRect, ofDividerAt dividerIndex: Int) -> NSRect
```

```objc
- (NSRect) splitView:(NSSplitView *) splitView effectiveRect:(NSRect) proposedEffectiveRect forDrawnRect:(NSRect) drawnRect ofDividerAtIndex:(NSInteger) dividerIndex;
```

## See Also

### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](./splitview%28_,shouldhidedividerat%29.md)
  Allows the split view controller to determine whether the user can drag a divider or adjust it off the edge of the split view.
- [func splitView(NSSplitView, additionalEffectiveRectOfDividerAt: Int) -> NSRect](./splitview%28_,additionaleffectiverectofdividerat%29.md)
  Allows the split view controller to return an additional rectangle where mouse clicks can initiate divider dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:effectiverect:fordrawnrect:ofdividerat:))*