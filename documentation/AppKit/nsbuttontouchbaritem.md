# NSButtonTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a button.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSButtonTouchBarItem
```

## Topics

### Creating a button item
- [convenience init(identifier: NSTouchBarItem.Identifier, image: UIImage, target: Any?, action: Selector?)](nsbuttontouchbaritem/init(identifier:image:target:action:).md)
- [convenience init(identifier: NSTouchBarItem.Identifier, title: String, image: UIImage, target: Any?, action: Selector?)](nsbuttontouchbaritem/init(identifier:title:image:target:action:).md)
- [convenience init(identifier: NSTouchBarItem.Identifier, title: String, target: Any?, action: Selector?)](nsbuttontouchbaritem/init(identifier:title:target:action:).md)
### Configuring button appearance
- [var title: String](nsbuttontouchbaritem/title.md)
- [var image: UIImage?](nsbuttontouchbaritem/image.md)
- [var bezelColor: UIColor?](nsbuttontouchbaritem/bezelcolor.md)
### Configuring button state
- [var isEnabled: Bool](nsbuttontouchbaritem/isenabled.md)
### Handling button interaction
- [var target: AnyObject?](nsbuttontouchbaritem/target.md)
- [var action: Selector?](nsbuttontouchbaritem/action.md)
### Configuring bar customization
- [var customizationLabel: String!](nsbuttontouchbaritem/customizationlabel.md)

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
- [class NSSliderTouchBarItem](nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
- [class NSStepperTouchBarItem](nssteppertouchbaritem.md)
  A bar item that provides a stepper control for incrementing or decrementing a value.
- [class NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttontouchbaritem)*