# NSPopoverTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a two-state control that can expand into its second state, showing the contents of a bar that it owns.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSPopoverTouchBarItem
```

## Topics

### Configuring the collapsed popover
- [var collapsedRepresentation: NSView](nspopovertouchbaritem/collapsedrepresentation.md)
  The view displayed when this item is displayed in its parent bar.
- [var collapsedRepresentationImage: UIImage?](nspopovertouchbaritem/collapsedrepresentationimage.md)
  The image displayed by the button for the default collapsed representation.
- [var collapsedRepresentationLabel: String](nspopovertouchbaritem/collapsedrepresentationlabel.md)
  The localized string displayed by the button for the default collapsed representation.
### Configuring the expanded popover
- [var popoverTouchBar: NSTouchBar](nspopovertouchbaritem/popovertouchbar.md)
  The bar displayed when this item is “popped.”
- [var showsCloseButton: Bool](nspopovertouchbaritem/showsclosebutton.md)
  A Boolean value that determines whether a close button should be shown on the popover bar.
- [var pressAndHoldTouchBar: NSTouchBar?](nspopovertouchbaritem/pressandholdtouchbar.md)
  The bar that is displayed when a user press-and-holds on the popover item.
### Expanding and collapsing a popover
- [func showPopover(Any?)](nspopovertouchbaritem/showpopover(_:).md)
  Replaces the main bar with this item’s popover bar.
- [func dismissPopover(Any?)](nspopovertouchbaritem/dismisspopover(_:).md)
  Restores the previously visible main bar.
- [func makeStandardActivatePopoverGestureRecognizer() -> NSGestureRecognizer](nspopovertouchbaritem/makestandardactivatepopovergesturerecognizer.md)
  Returns a gesture recognizer, configured to invoke the [`showPopover(_:)`](nspopovertouchbaritem/showpopover(_:).md) method.
### Configuring bar customization
- [var customizationLabel: String!](nspopovertouchbaritem/customizationlabel.md)
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
- [class NSSharingServicePickerTouchBarItem](nssharingservicepickertouchbaritem.md)
  A bar item that, along with its delegate, provides a list of objects eligible for sharing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopovertouchbaritem)*