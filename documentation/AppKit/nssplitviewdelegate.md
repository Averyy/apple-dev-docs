# NSSplitViewDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods that a delegate of a split view implements.

**Availability**:
- macOS

## Declaration

```swift
protocol NSSplitViewDelegate : NSObjectProtocol
```

```objc
@protocol NSSplitViewDelegate <NSObject>
```

## Topics

### Managing Subviews
- [func splitViewWillResizeSubviews(Notification)](./nssplitviewdelegate/splitviewwillresizesubviews%28_%29.md)
  Notifies the delegate when the split view is about to resize its subviews.
- [func splitViewDidResizeSubviews(Notification)](./nssplitviewdelegate/splitviewdidresizesubviews%28_%29.md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](./nssplitviewdelegate/splitview%28_,cancollapsesubview%29.md)
  Allows the delegate to determine whether the user can collapse and expand the specified subview.
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](./nssplitviewdelegate/splitview%28_,shouldcollapsesubview,fordoubleclickondividerat%29.md)
  Allows a delegate to determine if a subview collapses in response to a double click.
### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](./nssplitviewdelegate/splitview%28_,effectiverect,fordrawnrect,ofdividerat%29.md)
  Allows the delegate to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](./nssplitviewdelegate/splitview%28_,shouldhidedividerat%29.md)
  Allows the delegate to determine whether the user can drag a divider or adjust it off the edge of the split view.
- [func splitView(NSSplitView, additionalEffectiveRectOfDividerAt: Int) -> NSRect](./nssplitviewdelegate/splitview%28_,additionaleffectiverectofdividerat%29.md)
  Allows the delegate to return an additional rectangle where mouse clicks can initiate divider dragging.
### Constraining Split Position
- [func splitView(NSSplitView, constrainSplitPosition: CGFloat, ofSubviewAt: Int) -> CGFloat](./nssplitviewdelegate/splitview%28_,constrainsplitposition,ofsubviewat%29.md)
  Allows the delegate to constrain the divider to certain positions.
### Adjusting Subviews Manually
- [func splitView(NSSplitView, constrainMinCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](./nssplitviewdelegate/splitview%28_,constrainmincoordinate,ofsubviewat%29.md)
  Allows the delegate to constrain the minimum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, constrainMaxCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](./nssplitviewdelegate/splitview%28_,constrainmaxcoordinate,ofsubviewat%29.md)
  Allows the delegate to constrain the maximum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, resizeSubviewsWithOldSize: NSSize)](./nssplitviewdelegate/splitview%28_,resizesubviewswitholdsize%29.md)
  Allows the delegate to specify custom sizing behavior for the subviews of the split view.
- [func splitView(NSSplitView, shouldAdjustSizeOfSubview: NSView) -> Bool](./nssplitviewdelegate/splitview%28_,shouldadjustsizeofsubview%29.md)
  Allows the delegate to specify whether to resize the subview.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSSplitViewController](./nssplitviewcontroller.md)

## See Also

### Customizing the Split View Behavior
- [var delegate: (any NSSplitViewDelegate)?](./nssplitview/delegate.md)
  The split view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate)*