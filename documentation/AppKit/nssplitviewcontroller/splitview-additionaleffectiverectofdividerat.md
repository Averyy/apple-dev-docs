# splitView(_:additionalEffectiveRectOfDividerAt:)

**Framework**: AppKit  
**Kind**: method

Allows the split view controller to return an additional rectangle where mouse clicks can initiate divider dragging.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func splitView(_ splitView: NSSplitView, additionalEffectiveRectOfDividerAt dividerIndex: Int) -> NSRect
```

## See Also

- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](nssplitviewcontroller/splitview(_:effectiverect:fordrawnrect:ofdividerat:).md)
  Allows the split view controller to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](nssplitviewcontroller/splitview(_:shouldhidedividerat:).md)
  Allows the split view controller to determine whether the user can drag a divider or adjust it off the edge of the split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/splitview(_:additionaleffectiverectofdividerat:))*