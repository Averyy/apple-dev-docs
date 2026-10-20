# NSSegmentedCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An `NSSegmentedCell` object implements the appearance and behavior of a horizontal button divided into multiple segments. This class is used in conjunction with the [`NSSegmentedControl`](./nssegmentedcontrol.md) class to implement a segmented control.

**Availability**:
- macOS

## Declaration

```swift
class NSSegmentedCell
```

```objc
@interface NSSegmentedCell : NSActionCell
```

#### Overview

Use the methods of `NSSegmentedCell` to customize the attributes of a segmented control. To customize the appearance of individual segments, you can also subclass and override the [`drawSegment(_:inFrame:with:)`](./nssegmentedcell/drawsegment%28_,inframe,with%29.md) method.

## Topics

### Specifying the Number of Segments
- [var segmentCount: Int](./nssegmentedcell/segmentcount.md)
  The number of segments in the segmented control.
### Specifying the Selected Segment
- [func setSelected(Bool, forSegment: Int)](./nssegmentedcell/setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func selectSegment(withTag: Int) -> Bool](./nssegmentedcell/selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func makeNextSegmentKey()](./nssegmentedcell/makenextsegmentkey%28%29.md)
  Selects the next segment.
- [func makePreviousSegmentKey()](./nssegmentedcell/makeprevioussegmentkey%28%29.md)
  Selects the previous segment.
- [var selectedSegment: Int](./nssegmentedcell/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [func isSelected(forSegment: Int) -> Bool](./nssegmentedcell/isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected,
### Specifying the Tracking Mode
- [var trackingMode: NSSegmentedControl.SwitchTracking](./nssegmentedcell/trackingmode.md)
  The tracking mode used for the segments of the control.
### Configuring Individual Segments
- [func setLabel(String, forSegment: Int)](./nssegmentedcell/setlabel%28_,forsegment%29.md)
  Sets the label for the specified segment.
- [func label(forSegment: Int) -> String?](./nssegmentedcell/label%28forsegment%29.md)
  Returns the label of the specified segment.
- [func setImage(NSImage?, forSegment: Int)](./nssegmentedcell/setimage%28_,forsegment%29.md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](./nssegmentedcell/image%28forsegment%29.md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](./nssegmentedcell/setimagescaling%28_,forsegment%29.md)
  Sets the image scaling mode for the specified segment.
- [func imageScaling(forSegment: Int) -> NSImageScaling](./nssegmentedcell/imagescaling%28forsegment%29.md)
  Returns the image scaling mode associated with the specified segment.
- [func setWidth(CGFloat, forSegment: Int)](./nssegmentedcell/setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](./nssegmentedcell/width%28forsegment%29.md)
  Returns the width of the specified segment.
- [func setEnabled(Bool, forSegment: Int)](./nssegmentedcell/setenabled%28_,forsegment%29.md)
  Sets the enabled state of the specified segment
- [func isEnabled(forSegment: Int) -> Bool](./nssegmentedcell/isenabled%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is enabled.
- [func setMenu(NSMenu?, forSegment: Int)](./nssegmentedcell/setmenu%28_,forsegment%29.md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](./nssegmentedcell/menu%28forsegment%29.md)
  Returns the menu for the specified segment.
- [func setToolTip(String?, forSegment: Int)](./nssegmentedcell/settooltip%28_,forsegment%29.md)
  Sets the tooltip for the specified segment.
- [func toolTip(forSegment: Int) -> String?](./nssegmentedcell/tooltip%28forsegment%29.md)
  Returns the tooltip of the specified segment.
- [func setTag(Int, forSegment: Int)](./nssegmentedcell/settag%28_,forsegment%29.md)
  Sets the tag for the specified segment.
- [func tag(forSegment: Int) -> Int](./nssegmentedcell/tag%28forsegment%29.md)
  Returns the tag of the specified segment.
### Drawing Custom Content
- [func drawSegment(Int, inFrame: NSRect, with: NSView)](./nssegmentedcell/drawsegment%28_,inframe,with%29.md)
  Draws the image and label of the segment in the specified view.
### Specifying Segment Visual Styles
- [func interiorBackgroundStyle(forSegment: Int) -> NSView.BackgroundStyle](./nssegmentedcell/interiorbackgroundstyle%28forsegment%29.md)
  Returns the interior background style for the specified segment.
- [var segmentStyle: NSSegmentedControl.Style](./nssegmentedcell/segmentstyle.md)
  The visual style used to display the segmented control.

## Relationships

### Inherits From
- [NSActionCell](./nsactioncell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell)*