# NSPickerTouchBarItem.SelectionMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify selection modes for picker bar items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
enum SelectionMode
```

```c
enum NSPickerTouchBarItemSelectionMode : NSInteger;
```

## Topics

### Selection modes
- [NSPickerTouchBarItem.SelectionMode.selectOne](./selectionmode-swift.enum/selectone.md)
  A mode in which a person can only select one option in the control at a time.
- [NSPickerTouchBarItem.SelectionMode.selectAny](./selectionmode-swift.enum/selectany.md)
  A mode in which a person can select one or more options in the control at a time.
- [NSPickerTouchBarItem.SelectionMode.momentary](./selectionmode-swift.enum/momentary.md)
  A mode in which an option is only selected while a person is interacting within the bounds of that option.
### Initializers
- [init?(rawValue: Int)](./selectionmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Touch Bar items
- [class NSTouchBarItem](../nstouchbaritem.md)
  A UI control shown in the Touch Bar on supported models of MacBook Pro.
- [class NSCandidateListTouchBarItem](../nscandidatelisttouchbaritem.md)
  A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.
- [class NSColorPickerTouchBarItem](../nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.
- [class NSCustomTouchBarItem](../nscustomtouchbaritem.md)
  A bar item that contains a responder of your choice, such as a view, a button, or a scrubber.
- [class NSGroupTouchBarItem](../nsgrouptouchbaritem.md)
  A bar item that provides a bar to contain other items.
- [class NSPopoverTouchBarItem](../nspopovertouchbaritem.md)
  A bar item that provides a two-state control that can expand into its second state, showing the contents of a bar that it owns.
- [class NSSharingServicePickerTouchBarItem](../nssharingservicepickertouchbaritem.md)
  A bar item that, along with its delegate, provides a list of objects eligible for sharing.
- [class NSSliderTouchBarItem](../nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
- [class NSStepperTouchBarItem](../nssteppertouchbaritem.md)
  A bar item that provides a stepper control for incrementing or decrementing a value.
- [class NSUserInterfaceCompressionOptions](../nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSButtonTouchBarItem](../nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](../nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](./controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspickertouchbaritem/selectionmode-swift.enum)*