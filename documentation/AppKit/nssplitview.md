# NSSplitView

**Framework**: AppKit  
**Kind**: class

A view that arranges two or more views in a linear stack running horizontally or vertically.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSplitView
```

#### Overview

A split view manages the dividers and orientation for a split view controller ([`NSSplitViewController`](nssplitviewcontroller.md)). By default, dividers have a horizontal orientation so that the split view arranges its panes vertically from top to bottom.

Divider indices are zero-based. If the [`isVertical`](nssplitview/isvertical.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), which is the default value, the top divider has an index of `0`. If [`isVertical`](nssplitview/isvertical.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the leading divider has an index of `0`.

## Topics

### Customizing the Split View Behavior
- [var delegate: (any NSSplitViewDelegate)?](nssplitview/delegate.md)
  The split view’s delegate.
- [protocol NSSplitViewDelegate](nssplitviewdelegate.md)
  A set of optional methods that a delegate of a split view implements.
### Arranging Subviews
- [var arrangesAllSubviews: Bool](nssplitview/arrangesallsubviews.md)
  A Boolean value that determines whether the split view arranges all of its subviews as split panes.
- [var arrangedSubviews: [NSView]](nssplitview/arrangedsubviews.md)
  The array of views that the split view arranges as its split panes.
- [func addArrangedSubview(NSView)](nssplitview/addarrangedsubview(_:).md)
  Adds a view as an arranged split pane.
- [func insertArrangedSubview(NSView, at: Int)](nssplitview/insertarrangedsubview(_:at:).md)
  Adds a view as an arranged split pane at the specified index.
- [func removeArrangedSubview(NSView)](nssplitview/removearrangedsubview(_:).md)
  Removes a view as an arranged split pane.
### Managing Subviews
- [func adjustSubviews()](nssplitview/adjustsubviews.md)
  Adjusts the sizes of the split view’s subviews so they (plus the dividers) fill the split view.
- [func isSubviewCollapsed(NSView) -> Bool](nssplitview/issubviewcollapsed(_:).md)
  Returns whether the specified view is in a collapsed state.
- [func holdingPriorityForSubview(at: Int) -> NSLayoutConstraint.Priority](nssplitview/holdingpriorityforsubview(at:).md)
  Returns the priority of the subview’s width or height when resizing.
- [func setHoldingPriority(NSLayoutConstraint.Priority, forSubviewAt: Int)](nssplitview/setholdingpriority(_:forsubviewat:).md)
  Sets the priority for split view subviews to maintain their width or height.
### Managing Divider Orientation
- [var isVertical: Bool](nssplitview/isvertical.md)
  A Boolean value that determines the geometric orientation of the split view’s dividers.
### Configuring and Drawing Dividers
- [var dividerStyle: NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerColor: NSColor](nssplitview/dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [var dividerThickness: CGFloat](nssplitview/dividerthickness.md)
  The thickness of the dividers for the split view.
- [func drawDivider(in: NSRect)](nssplitview/drawdivider(in:).md)
  Draws a divider between two of the split view’s subviews.
### Saving Subview Positions
- [var autosaveName: NSSplitView.AutosaveName?](nssplitview/autosavename-swift.property.md)
  The name to use when the system automatically saves the split view’s divider configuration.
- [NSSplitView.AutosaveName](nssplitview/autosavename-swift.typealias.md)
  The type that specifies the split view’s autosave name.
### Constraining Split Position
- [func minPossiblePositionOfDivider(at: Int) -> CGFloat](nssplitview/minpossiblepositionofdivider(at:).md)
  Returns the minimum possible position of the divider at the specified index.
- [func maxPossiblePositionOfDivider(at: Int) -> CGFloat](nssplitview/maxpossiblepositionofdivider(at:).md)
  Returns the maximum possible position of the divider at the specified index.
- [func setPosition(CGFloat, ofDividerAt: Int)](nssplitview/setposition(_:ofdividerat:).md)
  Updates the location of a divider you specify by index.
### Managing Notifications
- [class let willResizeSubviewsNotification: NSNotification.Name](nssplitview/willresizesubviewsnotification.md)
  A notification that posts before a change to the size of some or all subviews of a split view.
- [class let didResizeSubviewsNotification: NSNotification.Name](nssplitview/didresizesubviewsnotification.md)
  A notification that posts after a change to the size of some or all subviews of a split view.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSSplitViewController](nssplitviewcontroller.md)
  An object that manages an array of adjacent child views, and has a split view object for managing dividers between those views.
- [class NSSplitViewItem](nssplitviewitem.md)
  An item in a split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview)*