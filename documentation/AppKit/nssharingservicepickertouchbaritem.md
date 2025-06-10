# NSSharingServicePickerTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that, along with its delegate, provides a list of objects eligible for sharing.

**Availability**:
- iOS 10.13+
- iPadOS 10.13+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSSharingServicePickerTouchBarItem
```

## Topics

### Setting the delegate
- [var delegate: (any NSSharingServicePickerTouchBarItemDelegate)?](nssharingservicepickertouchbaritem/delegate.md)
  The object that acts as the delegate of the sharing service picker bar item.
- [protocol NSSharingServicePickerTouchBarItemDelegate](nssharingservicepickertouchbaritemdelegate.md)
  A protocol that a sharing service picker item delegate uses to provide a list of items eligible for sharing.
### Configuring the appearance
- [var buttonImage: NSImage?](nssharingservicepickertouchbaritem/buttonimage.md)
  The image displayed in the sharing service picker item button.
- [var buttonTitle: String](nssharingservicepickertouchbaritem/buttontitle.md)
  The text displayed in the sharing service picker item button.
### Enabling the item
- [var isEnabled: Bool](nssharingservicepickertouchbaritem/isenabled.md)
  A Boolean value that specifies whether the sharing service picker item is enabled.
### Supporting sharing
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](nssharingservicepickertouchbaritem/activityitemsconfiguration.md)

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
- [class NSSliderTouchBarItem](nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickertouchbaritem)*