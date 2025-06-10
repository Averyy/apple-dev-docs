# NSSliderCell

**Framework**: AppKit  
**Kind**: class

The appearance and behavior of an [`NSSlider`](nsslider.md) object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSliderCell
```

#### Overview

You can customize an [`NSSliderCell`](nsslidercell.md) to a certain degree, using its properties. If this doesn’t give you sufficient flexibility, you can create a subclass. In that subclass, you can override any of the following methods: [`knobRect(flipped:)`](nsslidercell/knobrect(flipped:).md), [`drawBar(inside:flipped:)`](nsslidercell/drawbar(inside:flipped:).md), [`drawKnob(_:)`](nsslidercell/drawknob(_:).md), and [`prefersTrackingUntilMouseUp`](nsslidercell/preferstrackinguntilmouseup.md).

## Topics

### Managing Cell Behavior
- [var altIncrementValue: Double](nsslidercell/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the knob.
- [class var prefersTrackingUntilMouseUp: Bool](nsslidercell/preferstrackinguntilmouseup.md)
  Returns a Boolean value indicating whether the `NSSliderCell` continues to track the pointer until the next mouse up.
- [var trackRect: NSRect](nsslidercell/trackrect.md)
  The rectangle within which the cell tracks the pointer while the mouse button is down.
### Managing the Slider Type
- [var sliderType: NSSlider.SliderType](nsslidercell/slidertype.md)
  The slider type, either linear or circular.
### Displaying the Cell
- [func barRect(flipped: Bool) -> NSRect](nsslidercell/barrect(flipped:).md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](nsslidercell/drawtickmarks.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](nsslidercell/knobrect(flipped:).md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](nsslidercell/drawbar(inside:flipped:).md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.
- [func drawKnob(NSRect)](nsslidercell/drawknob(_:).md)
  Draws the slider knob in the given rectangle.
### Managing Cell Appearance
- [var knobThickness: CGFloat](nsslidercell/knobthickness.md)
  The thickness of the slider knob, in pixels.
- [var isVertical: Bool](nsslidercell/isvertical.md)
  An integer indicating the orientation (vertical or horizontal) of the slider.
### Managing Value Limits
- [var maxValue: Double](nsslidercell/maxvalue.md)
  The maximum value the slider can send to its target.
- [var minValue: Double](nsslidercell/minvalue.md)
  The minimum value the slider can send to its target.
### Managing Tick Marks
- [var allowsTickMarkValuesOnly: Bool](nsslidercell/allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslidercell/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslidercell/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the specified point.
- [var numberOfTickMarks: Int](nsslidercell/numberoftickmarks.md)
  The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.
- [func rectOfTickMark(at: Int) -> NSRect](nsslidercell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslidercell/tickmarkposition.md)
  The position of the tick marks relative to the receiver.
- [func tickMarkValue(at: Int) -> Double](nsslidercell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index.
### Constants
- [NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell)*