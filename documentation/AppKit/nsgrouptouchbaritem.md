# NSGroupTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a bar to contain other items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSGroupTouchBarItem
```

## Topics

### Creating a group
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])](nsgrouptouchbaritem/init(identifier:items:).md)
  Initializes and returns a group item whose bar is constructed from the supplied items.
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)](nsgrouptouchbaritem/init(identifier:items:allowedcompressionoptions:).md)
  Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.
- [convenience init(alertStyleWithIdentifier: NSTouchBarItem.Identifier)](nsgrouptouchbaritem/init(alertstylewithidentifier:).md)
  Initializes and returns a group item configured to match system alerts.
### Configuring groups
- [var groupTouchBar: NSTouchBar](nsgrouptouchbaritem/grouptouchbar.md)
  A bar that holds this group’s items.
- [var groupUserInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nsgrouptouchbaritem/groupuserinterfacelayoutdirection.md)
  The user interface direction that controls the layout order of the items.
### Configuring item width
- [var prefersEqualWidths: Bool](nsgrouptouchbaritem/prefersequalwidths.md)
  A Boolean value that specifies that items should have equal widths when possible.
- [var preferredItemWidth: CGFloat](nsgrouptouchbaritem/preferreditemwidth.md)
  The preferred width for items in the group when [`prefersEqualWidths`](nsgrouptouchbaritem/prefersequalwidths.md) is [`true`](https://developer.apple.com/documentation/swift/true).
### Configuring item compression
- [var effectiveCompressionOptions: NSUserInterfaceCompressionOptions](nsgrouptouchbaritem/effectivecompressionoptions.md)
  The compression options that are currently active on the group.
- [var prioritizedCompressionOptions: [NSUserInterfaceCompressionOptions]](nsgrouptouchbaritem/prioritizedcompressionoptions.md)
  The allowed compression options, in the order they should be applied.
### Configuring bar customization
- [var customizationLabel: String!](nsgrouptouchbaritem/customizationlabel.md)
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

## See Also

- [class NSTouchBarItem](nstouchbaritem.md)
  A UI control shown in the Touch Bar on supported models of MacBook Pro.
- [class NSCandidateListTouchBarItem](nscandidatelisttouchbaritem.md)
  A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.
- [class NSCustomTouchBarItem](nscustomtouchbaritem.md)
  A bar item that contains a responder of your choice, such as a view, a button, or a scrubber.
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
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem)*