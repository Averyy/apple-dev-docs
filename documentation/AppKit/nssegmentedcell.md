# NSSegmentedCell

**Framework**: AppKit  
**Kind**: class

An `NSSegmentedCell` object implements the appearance and behavior of a horizontal button divided into multiple segments. This class is used in conjunction with the [`NSSegmentedControl`](nssegmentedcontrol.md) class to implement a segmented control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSegmentedCell
```

#### Overview

Use the methods of `NSSegmentedCell` to customize the attributes of a segmented control. To customize the appearance of individual segments, you can also subclass and override the [`drawSegment(_:inFrame:with:)`](nssegmentedcell/drawsegment(_:inframe:with:).md) method.

## Topics

### Specifying the Number of Segments
- [var segmentCount: Int](nssegmentedcell/segmentcount.md)
  The number of segments in the segmented control.
### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](nssegmentedcell/setselected(_:forsegment:).md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](nssegmentedcell/selectsegment(withtag:).md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](nssegmentedcell/makenextsegmentkey.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](nssegmentedcell/makeprevioussegmentkey.md)
  Selects the previous segment.
- [var selectedSegment: Int](nssegmentedcell/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](nssegmentedcell/isselected(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is selected,
### Specifying the Tracking Mode
- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcell/trackingmode.md)
  The tracking mode used for the segments of the control.
### Configuring Individual Segments
- [func setLabel(String, forSegment: Int)](nssegmentedcell/setlabel(_:forsegment:).md)
  Sets the label for the specified segment.
- [func label(forSegment: Int) -> String?](nssegmentedcell/label(forsegment:).md)
  Returns the label of the specified segment.
- [func setImage(NSImage?, forSegment: Int)](nssegmentedcell/setimage(_:forsegment:).md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](nssegmentedcell/image(forsegment:).md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](nssegmentedcell/setimagescaling(_:forsegment:).md)
  Sets the image scaling mode for the specified segment.
- [func imageScaling(forSegment: Int) -> NSImageScaling](nssegmentedcell/imagescaling(forsegment:).md)
  Returns the image scaling mode associated with the specified segment.
- [func setWidth(CGFloat, forSegment: Int)](nssegmentedcell/setwidth(_:forsegment:).md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](nssegmentedcell/width(forsegment:).md)
  Returns the width of the specified segment.
- [func setEnabled(Bool, forSegment: Int)](nssegmentedcell/setenabled(_:forsegment:).md)
  Sets the enabled state of the specified segment
- [func isEnabled(forSegment: Int) -> Bool](nssegmentedcell/isenabled(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is enabled.
- [func setMenu(NSMenu?, forSegment: Int)](nssegmentedcell/setmenu(_:forsegment:).md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](nssegmentedcell/menu(forsegment:).md)
  Returns the menu for the specified segment.
- [func setToolTip(String?, forSegment: Int)](nssegmentedcell/settooltip(_:forsegment:).md)
  Sets the tooltip for the specified segment.
- [func toolTip(forSegment: Int) -> String?](nssegmentedcell/tooltip(forsegment:).md)
  Returns the tooltip of the specified segment.
- [func setTag(Int, forSegment: Int)](nssegmentedcell/settag(_:forsegment:).md)
  Sets the tag for the specified segment.
- [func tag(forSegment: Int) -> Int](nssegmentedcell/tag(forsegment:).md)
  Returns the tag of the specified segment.
### Drawing Custom Content
- [func drawSegment(Int, inFrame: NSRect, with: NSView)](nssegmentedcell/drawsegment(_:inframe:with:).md)
  Draws the image and label of the segment in the specified view.
### Specifying Segment Visual Styles
- [func interiorBackgroundStyle(forSegment: Int) -> NSView.BackgroundStyle](nssegmentedcell/interiorbackgroundstyle(forsegment:).md)
  Returns the interior background style for the specified segment.
- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcell/segmentstyle.md)
  The visual style used to display the segmented control.

## Relationships

### Inherits From
- [NSActionCell](nsactioncell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell)*