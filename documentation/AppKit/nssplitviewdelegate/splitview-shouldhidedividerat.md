# splitView(_:shouldHideDividerAt:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to determine whether the user can drag a divider or adjust it off the edge of the split view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, shouldHideDividerAt dividerIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user can drag the divider off the edge of the split view, resulting in it not being visible.

#### Discussion

If a split view has no delegate, or if its delegate doesn’t respond to this message, the split view behaves as if it has a delegate that returns [`false`](https://developer.apple.com/documentation/swift/false) when it receives this message.

## Parameters

- `splitView`: The split view that sends the message.
- `dividerIndex`: The zero-based index of the divider.

## See Also

- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](nssplitviewdelegate/splitview(_:effectiverect:fordrawnrect:ofdividerat:).md)
  Allows the delegate to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, additionalEffectiveRectOfDividerAt: Int) -> NSRect](nssplitviewdelegate/splitview(_:additionaleffectiverectofdividerat:).md)
  Allows the delegate to return an additional rectangle where mouse clicks can initiate divider dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:shouldhidedividerat:))*