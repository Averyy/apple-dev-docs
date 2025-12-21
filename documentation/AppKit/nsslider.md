# NSSlider

**Framework**: AppKit  
**Kind**: class

A display of a bar representing a continuous range of numerical values and a knob representing the currently selected value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSlider
```

#### Overview

A slider is a UI element that displays a range of values in the app. Sliders can be vertical or horizontal bars or circular dials. An indicator, or knob, notes the current setting. The user can move the knob in the slider’s bar—or rotate the knob in a circular slider—to change the setting.

The `NSSlider` class uses the [`NSSliderCell`](nsslidercell.md) class to implement its user interface.

## Topics

### Creating sliders
- [convenience init(target: Any?, action: Selector?)](nsslider/init(target:action:).md)
  Creates a continuous horizontal slider whose values range from `0.0` to `1.0`.
- [convenience init(value: Double, minValue: Double, maxValue: Double, target: Any?, action: Selector?)](nsslider/init(value:minvalue:maxvalue:target:action:).md)
  Creates a continuous horizontal slider that represents values over the specified range.
### Managing the slider’s appearance
- [var sliderType: NSSlider.SliderType](nsslider/slidertype-swift.property.md)
  The type of the slider, such as vertical or circular.
- [NSSlider.SliderType](nsslider/slidertype-swift.enum.md)
  The types of sliders, used by [`sliderType`](nsslidercell/slidertype.md).
- [var altIncrementValue: Double](nsslider/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the slider knob.
- [var knobThickness: CGFloat](nsslider/knobthickness.md)
  The knob’s thickness, in pixels.
- [var isVertical: Bool](nsslider/isvertical.md)
  An integer indicating the orientation (horizontal or vertical) of the slider.
- [var trackFillColor: NSColor?](nsslider/trackfillcolor.md)
  The color of the filled portion of the slider track, in appearances that support it.
- [var tintProminence: NSTintProminence](nsslider/tintprominence.md)
  The tint prominence of the slider. The automatic behavior for a regular slider tints its track fill, while a slider with tick marks is untinted. Setting the tint prominence will override this default behavior and choose an explicit track fill tint behavior. See [`NSTintProminence`](nstintprominence.md) for a list of possible values.
- [enum NSTintProminence](nstintprominence.md)
  Controls how strongly the tint color applies in a view.
### Asking about the value limits
- [var maxValue: Double](nsslider/maxvalue.md)
  The maximum value the slider can send to its target.
- [var minValue: Double](nsslider/minvalue.md)
  The minimum value the slider can send to its target.
### Handling mouse-down events
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsslider/acceptsfirstmouse(for:).md)
  Returns a Boolean value indicating whether a mouse-down event both activates the window and starts dragging the slider’s knob.
### Managing tick marks
- [var allowsTickMarkValuesOnly: Bool](nsslider/allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslider/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslider/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the given point.
- [var numberOfTickMarks: Int](nsslider/numberoftickmarks.md)
  The number of tick marks associated with the slider.
- [func rectOfTickMark(at: Int) -> NSRect](nsslider/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the given index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](nsslider/tickmarkvalue(at:).md)
  Returns the slider’s value represented by the tick mark at the specified index.
### Instance Properties
- [var neutralValue: Double](nsslider/neutralvalue.md)
  The value this slider will be filled from. This slider will be filled from its `neutralValue` to its current value. If `neutralValue` has not been explicitly set before, access to `neutralValue` will return `minValue`.

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
- [NSAccessibilitySlider](nsaccessibilityslider.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider)*