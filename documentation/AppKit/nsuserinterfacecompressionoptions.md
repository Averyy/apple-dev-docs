# NSUserInterfaceCompressionOptions

**Framework**: AppKit  
**Kind**: class

An object that specifies how user interface elements resize themselves when space is constrained.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSUserInterfaceCompressionOptions
```

#### Overview

An instance of [`NSUserInterfaceCompressionOptions`](nsuserinterfacecompressionoptions.md) contains zero or more options. Because a compression options object behaves like a set, you can use common operations like intersection, union and subtraction to interact with instances and their members.

You can access system-defined options through the class methods detailed in Creating standard options, or you can create your own custom options with the [`init(identifier:)`](nsuserinterfacecompressionoptions/init(identifier:).md) initializer.

To compare two different compression options objects, use the methods described in the Comparing compression options section.

## Topics

### Creating a compression option
- [init()](nsuserinterfacecompressionoptions/init.md)
  Creates an option object containing no options.
- [init(options: Set<NSUserInterfaceCompressionOptions>)](nsuserinterfacecompressionoptions/init(options:).md)
  Creates an option object that represents the union of the supplied options.
- [init(identifier: String)](nsuserinterfacecompressionoptions/init(identifier:).md)
  Creates an option object with the given identifier string.
- [init(coder: NSCoder)](nsuserinterfacecompressionoptions/init(coder:).md)
  Creates an option object from data in an unarchiver.
### Creating standard options
- [class var hideImages: NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/hideimages.md)
  An option specifying that views should hide their images.
- [class var hideText: NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/hidetext.md)
  An option specifying that views should hide their text.
- [class var reduceMetrics: NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/reducemetrics.md)
  An option specifying that views should reduce their internal metrics.
- [class var breakEqualWidths: NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/breakequalwidths.md)
  An option specifying that views should no longer maintain equal width constraints.
- [class var standardOptions: NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/standardoptions.md)
  An option that represents the union of all standard compression options.
### Comparing compression options
- [var isEmpty: Bool](nsuserinterfacecompressionoptions/isempty.md)
  A Boolean value that denotes whether the option is empty.
- [func contains(NSUserInterfaceCompressionOptions) -> Bool](nsuserinterfacecompressionoptions/contains(_:).md)
  Determines whether the supplied compression options are all present in the current instance.
- [func intersects(NSUserInterfaceCompressionOptions) -> Bool](nsuserinterfacecompressionoptions/intersects(_:).md)
  Determines whether the supplied compression options intersect with the current instance’s options.
### Combining compression options
- [func union(NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/union(_:).md)
  Creates a new compression options object representing the union with the provided options.
- [func subtracting(NSUserInterfaceCompressionOptions) -> NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions/subtracting(_:).md)
  Creates a new compression options object with the supplied options removed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacecompressionoptions)*