# splitView(_:additionalEffectiveRectOfDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to return an additional rectangle where mouse clicks can initiate divider dragging.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, additionalEffectiveRectOfDividerAt dividerIndex: Int) -> NSRect
```

```objc
- (NSRect) splitView:(NSSplitView *) splitView additionalEffectiveRectOfDividerAtIndex:(NSInteger) dividerIndex;
```

## Return Value

An additional rectangle, in the coordinate system that `splitView` defines, where mouse clicks can initiate divider dragging. Returning [`NSZeroRect`](../../Foundation/nszerorect.md) indicates no additional dragging rectangle is necessary.

## Discussion

If a split view has no delegate, or if its delegate doesn’t respond to this message, only mouse clicks within the effective frame of a divider initiate divider dragging.

## Parameters

- `splitView`: The split view that sends the message.
- `dividerIndex`: The index of the divider.

## See Also

### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](./splitview%28_,effectiverect,fordrawnrect,ofdividerat%29.md)
  Allows the delegate to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](./splitview%28_,shouldhidedividerat%29.md)
  Allows the delegate to determine whether the user can drag a divider or adjust it off the edge of the split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:additionaleffectiverectofdividerat:))*