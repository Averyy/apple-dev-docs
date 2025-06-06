# NSScroller

**Framework**: AppKit  
**Kind**: class

An object that controls scrolling of a document view within a scroll view or other type of container view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSScroller
```

#### Overview

A scroller displays a slot containing a knob that the user can drag directly to the desired location. The knob indicates both the position within the document view and—by varying in size within the slot—the amount visible relative to the size of the document view.

Typically, you don’t need to program with scrollers; instead, you configure them with an [`NSScrollView`](nsscrollview.md) object in a [`Nib file`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/NibFile.html#//apple_ref/doc/uid/TP40008195-CH34).

Don’t use an scroller when a slider would be more appropriate. An [`NSSlider`](nsslider.md) object represents a range of values for something in the application and lets the user choose a setting. A scroller represents the relative position of the visible portion of a view and lets the user choose which portion to view.

## Topics

### Determining Scroller Size
- [class func scrollerWidth(for: NSControl.ControlSize, scrollerStyle: NSScroller.Style) -> CGFloat](nsscroller/scrollerwidth(for:scrollerstyle:).md)
  Returns the width for scrollers of the receiving class for a given control size and scroller style.
- [var controlSize: NSControl.ControlSize](nsscroller/controlsize.md)
  The size of the scroller.
### Laying out a Scroller
- [var arrowsPosition: NSScroller.ArrowPosition](nsscroller/arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](nsscroller/arrowposition.md).
### Setting the Knob Position
- [var knobProportion: CGFloat](nsscroller/knobproportion.md)
  The proportion of the knob slot that the knob should fill.
### Calculating Layout
- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func testPart(NSPoint) -> NSScroller.Part](nsscroller/testpart(_:).md)
  Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).
- [func checkSpaceForParts()](nsscroller/checkspaceforparts.md)
  Checks to see if there is enough room in the receiver to display the knob and buttons.
- [var usableParts: NSScroller.UsableParts](nsscroller/usableparts-swift.property.md)
  A value that indicates which parts of the receiver are displayed and usable.
### Drawing Scroller Parts
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func drawKnobSlot(in: NSRect, highlight: Bool)](nsscroller/drawknobslot(in:highlight:).md)
  Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.
- [func drawKnob()](nsscroller/drawknob.md)
  Draws the knob.
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.
### Event Handling
- [var hitPart: NSScroller.Part](nsscroller/hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.
- [func trackKnob(with: NSEvent)](nsscroller/trackknob(with:).md)
  Tracks the knob and sends action messages to the receiver’s target.
- [func trackScrollButtons(with: NSEvent)](nsscroller/trackscrollbuttons(with:).md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.
### Setting Control Tint
- [var controlTint: NSControlTint](nsscroller/controltint.md)
  The scroller’s control tint.
### Managing Presentation Style
- [class var preferredScrollerStyle: NSScroller.Style](nsscroller/preferredscrollerstyle.md)
  Returns the style of scrollers that applications should use wherever possible.
- [var scrollerStyle: NSScroller.Style](nsscroller/scrollerstyle.md)
  The scroller style for this scroller.
- [var knobStyle: NSScroller.KnobStyle](nsscroller/knobstyle-swift.property.md)
  The scroller’s knob style.
### Constants
- [NSScroller.Style](nsscroller/style.md)
  Constants to specify the scroller style.
- [NSScroller.KnobStyle](nsscroller/knobstyle-swift.enum.md)
  Specify different knob styles.
- [NSScroller.Part](nsscroller/part.md)
  These constants specify the different parts of the scroller:
- [NSScroller.Arrow](nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md).
- [NSScroller.ArrowPosition](nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.
- [NSScroller.UsableParts](nsscroller/usableparts-swift.enum.md)
  These constants specify which parts of the scroller are visible.
### Notifications
- [class let preferredScrollerStyleDidChangeNotification: NSNotification.Name](nsscroller/preferredscrollerstyledidchangenotification.md)
  Posted if the preferred scroller style changes.
### Instance Properties
- [var knobProportion: CGFloat](nsscroller/knobproportion.md)
  The proportion of the knob slot that the knob should fill.
### Type Properties
- [class var isCompatibleWithOverlayScrollers: Bool](nsscroller/iscompatiblewithoverlayscrollers.md)

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
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

## See Also

- [class NSScrollView](nsscrollview.md)
  A view that displays a portion of a document view and provides scroll bars that allow the user to move the document view within the scroll view.
- [class NSClipView](nsclipview.md)
  An object that clips a document view to a scroll view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller)*