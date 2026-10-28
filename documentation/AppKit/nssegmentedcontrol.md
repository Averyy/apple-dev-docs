# NSSegmentedControl

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

Display one or more buttons in a single horizontal group.

**Availability**:
- macOS

## Declaration

```swift
class NSSegmentedControl
```

```objc
@interface NSSegmentedControl : NSControl
```

## Overview

The `NSSegmentedControl` class uses an [`NSSegmentedCell`](./nssegmentedcell.md) class to implement much of the control’s functionality. Most methods in `NSSegmentedControl` are simply cover methods that call the corresponding method in [`NSSegmentedCell`](./nssegmentedcell.md). The methods of [`NSSegmentedCell`](./nssegmentedcell.md) that do not have covers relate to accessing and setting values for tags and tooltips, programatically setting the key segment, and establishing the mode of the control.

The features of a segmented control include the following:

- A segment can have an image, text (label), menu, tooltip, and tag.
- A segmented control can contain images or text, but not both.
- Either the control or individual segments can be enabled or disabled.
- Segmented controls have four tracking modes, described in [`NSSegmentedControl.SwitchTracking`](./nssegmentedcontrol/switchtracking.md). You use these modes with the [`trackingMode`](./nssegmentedcontrol/trackingmode.md) property.
- Each segment can be either a fixed width or autosized to fit the contents.
- If a segment has text and is marked as autosizing, then the text may be truncated so that the control completely fits.
- If an image is too large to fit in a segment, it is clipped.
- If Full Keyboard Access is enabled in System Preferences > Keyboard, the keyboard may be used to move between and select segments.

## Topics

### Creating a segmented control
- [convenience init(images: [NSImage], trackingMode: NSSegmentedControl.SwitchTracking, target: Any?, action: Selector?)](./nssegmentedcontrol/init%28images,trackingmode,target,action%29.md)
  Creates a standard segmented control containing one segment for each of the provided images.
- [convenience init(labels: [String], trackingMode: NSSegmentedControl.SwitchTracking, target: Any?, action: Selector?)](./nssegmentedcontrol/init%28labels,trackingmode,target,action%29.md)
  Creates a standard segmented control containing one segment for each of the provided labels.
### Configuring the cell
- [class NSSegmentedCell](./nssegmentedcell.md)
  An `NSSegmentedCell` object implements the appearance and behavior of a horizontal button divided into multiple segments. This class is used in conjunction with the [`NSSegmentedControl`](./nssegmentedcontrol.md) class to implement a segmented control.
### Specifying the segment behavior
- [var trackingMode: NSSegmentedControl.SwitchTracking](./nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [NSSegmentedControl.SwitchTracking](./nssegmentedcontrol/switchtracking.md)
  Constants that specify the type of tracking behavior a segmented control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](./nssegmentedcontrol/segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](./nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](./nssegmentedcontrol/segmentstyle.md).
- [var role: NSSegmentedControl.Role](./nssegmentedcontrol/role-swift.property.md)
- [NSSegmentedControl.Role](./nssegmentedcontrol/role-swift.enum.md)
### Specifying number of segments
- [var segmentCount: Int](./nssegmentedcontrol/segmentcount.md)
  The number of segments in the control.
### Configuring the segment text
- [func label(forSegment: Int) -> String?](./nssegmentedcontrol/label%28forsegment%29.md)
  Returns the label of the specified segment.
- [func setLabel(String, forSegment: Int)](./nssegmentedcontrol/setlabel%28_,forsegment%29.md)
  Sets the label for the specified segment.
- [func setAlignment(NSTextAlignment, forSegment: Int)](./nssegmentedcontrol/setalignment%28_,forsegment%29.md)
- [func alignment(forSegment: Int) -> NSTextAlignment](./nssegmentedcontrol/alignment%28forsegment%29.md)
### Configuring a segment image
- [func setImage(NSImage?, forSegment: Int)](./nssegmentedcontrol/setimage%28_,forsegment%29.md)
  Sets the image for the specified segment.
- [func image(forSegment: Int) -> NSImage?](./nssegmentedcontrol/image%28forsegment%29.md)
  Returns the image associated with the specified segment.
- [func setImageScaling(NSImageScaling, forSegment: Int)](./nssegmentedcontrol/setimagescaling%28_,forsegment%29.md)
  Sets the scaling mode used to display the specified segment’s image.
- [func imageScaling(forSegment: Int) -> NSImageScaling](./nssegmentedcontrol/imagescaling%28forsegment%29.md)
  Returns the scaling mode used to display the specified segment’s image.
### Configuring a segment menu
- [func setMenu(NSMenu?, forSegment: Int)](./nssegmentedcontrol/setmenu%28_,forsegment%29.md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](./nssegmentedcontrol/menu%28forsegment%29.md)
  Returns the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](./nssegmentedcontrol/setshowsmenuindicator%28_,forsegment%29.md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](./nssegmentedcontrol/showsmenuindicator%28forsegment%29.md)
- [var isSpringLoaded: Bool](./nssegmentedcontrol/isspringloaded.md)
  A Boolean value that indicates whether spring loading is enabled for the control.
### Managing the selected segment
- [var selectedSegment: Int](./nssegmentedcontrol/selectedsegment.md)
  The index of the selected segment of the control, or `-1` if no segment is selected.
- [var indexOfSelectedItem: Int](./nssegmentedcontrol/indexofselecteditem.md)
- [func selectSegment(withTag: Int) -> Bool](./nssegmentedcontrol/selectsegment%28withtag%29.md)
  Selects the segment with the specified tag.
- [func setSelected(Bool, forSegment: Int)](./nssegmentedcontrol/setselected%28_,forsegment%29.md)
  Sets the selection state of the specified segment.
- [func isSelected(forSegment: Int) -> Bool](./nssegmentedcontrol/isselected%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is selected.
- [var selectedSegmentBezelColor: NSColor?](./nssegmentedcontrol/selectedsegmentbezelcolor.md)
  The color of the selected segment’s bezel, in appearances that support it.
- [var doubleValueForSelectedSegment: Double](./nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.
### Adjusting the segment spacing
- [func setWidth(CGFloat, forSegment: Int)](./nssegmentedcontrol/setwidth%28_,forsegment%29.md)
  Sets the width of the specified segment.
- [func width(forSegment: Int) -> CGFloat](./nssegmentedcontrol/width%28forsegment%29.md)
  Returns the width of the specified segment.
- [var segmentDistribution: NSSegmentedControl.Distribution](./nssegmentedcontrol/segmentdistribution.md)
- [NSSegmentedControl.Distribution](./nssegmentedcontrol/distribution.md)
- [var activeCompressionOptions: NSUserInterfaceCompressionOptions](./nssegmentedcontrol/activecompressionoptions.md)
- [func compress(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions])](./nssegmentedcontrol/compress%28withprioritizedcompressionoptions%29.md)
- [func minimumSize(withPrioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]) -> NSSize](./nssegmentedcontrol/minimumsize%28withprioritizedcompressionoptions%29.md)
### Specifying the border shape
- [var borderShape: NSControl.BorderShape](./nssegmentedcontrol/bordershape.md)
- [NSControl.BorderShape](./nscontrol/bordershape.md)
### Enabling and disabling segments
- [func setEnabled(Bool, forSegment: Int)](./nssegmentedcontrol/setenabled%28_,forsegment%29.md)
  Sets the enabled state of the specified segment
- [func isEnabled(forSegment: Int) -> Bool](./nssegmentedcontrol/isenabled%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is enabled.
### Managing tags and tooltips
- [func tag(forSegment: Int) -> Int](./nssegmentedcontrol/tag%28forsegment%29.md)
- [func setTag(Int, forSegment: Int)](./nssegmentedcontrol/settag%28_,forsegment%29.md)
- [func setToolTip(String?, forSegment: Int)](./nssegmentedcontrol/settooltip%28_,forsegment%29.md)
- [func toolTip(forSegment: Int) -> String?](./nssegmentedcontrol/tooltip%28forsegment%29.md)

## Relationships

### Inherits From
- [NSControl](./nscontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceCompression](./nsuserinterfacecompression.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controls
- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](./nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](./nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](./combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](./nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](./date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](./nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](./nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](./path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](./nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](./nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](./nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](./nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](./search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [Slider](./slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol)*