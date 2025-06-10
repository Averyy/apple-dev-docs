# NSSliderTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a slider control for choosing a value in a range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSSliderTouchBarItem
```

## Topics

### Configuring the slider
- [var slider: NSSlider](nsslidertouchbaritem/slider.md)
  The slider displayed by the bar item.
- [var label: String?](nsslidertouchbaritem/label.md)
  The text displayed alongside the slider.
- [var view: any NSView & NSUserInterfaceCompression](nsslidertouchbaritem/view.md)
### Configuring slider accessories
- [var minimumValueAccessory: NSSliderAccessory?](nsslidertouchbaritem/minimumvalueaccessory.md)
  The accessory that appears at the end of the slider with the minimum value.
- [var maximumValueAccessory: NSSliderAccessory?](nsslidertouchbaritem/maximumvalueaccessory.md)
  The accessory that appears at the end of the slider with the maximum value.
- [var valueAccessoryWidth: NSSliderAccessory.Width](nsslidertouchbaritem/valueaccessorywidth.md)
  The width of the value accessories that appear at either end of the slider.
### Managing the slider’s value
- [var minimumSliderWidth: CGFloat](nsslidertouchbaritem/minimumsliderwidth.md)
  The minimum width of the slider’s track.
- [var maximumSliderWidth: CGFloat](nsslidertouchbaritem/maximumsliderwidth.md)
  The maximum width of the slider’s track.
- [var doubleValue: Double](nsslidertouchbaritem/doublevalue.md)
  The double value of the slider.
### Handling slider interaction
- [var target: AnyObject?](nsslidertouchbaritem/target.md)
  An object that is notified when a user interacts with the slider or either of the accessories.
- [var action: Selector?](nsslidertouchbaritem/action.md)
  The selector on the target object that is invoked when a user interacts with the slider or either of the accessories.
### Configuring bar customization
- [var customizationLabel: String!](nsslidertouchbaritem/customizationlabel.md)
  The user-visible string identifying this item during bar customization.

## Relationships

### Inherits From
- [NSTouchBarItem](nstouchbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTouchBarItem](nstouchbaritem.md)
  A UI control shown in the Touch Bar on supported models of MacBook Pro.
- [class NSCandidateListTouchBarItem](nscandidatelisttouchbaritem.md)
  A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.
- [class NSCustomTouchBarItem](nscustomtouchbaritem.md)
  A bar item that contains a responder of your choice, such as a view, a button, or a scrubber.
- [class NSGroupTouchBarItem](nsgrouptouchbaritem.md)
  A bar item that provides a bar to contain other items.
- [class NSPopoverTouchBarItem](nspopovertouchbaritem.md)
  A bar item that provides a two-state control that can expand into its second state, showing the contents of a bar that it owns.
- [class NSSharingServicePickerTouchBarItem](nssharingservicepickertouchbaritem.md)
  A bar item that, along with its delegate, provides a list of objects eligible for sharing.
- [class NSStepperTouchBarItem](nssteppertouchbaritem.md)
  A bar item that provides a stepper control for incrementing or decrementing a value.
- [class NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidertouchbaritem)*