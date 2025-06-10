# NSPickerTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a picker control with multiple options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSPickerTouchBarItem
```

## Topics

### Creating a picker item
- [convenience init(identifier: NSTouchBarItem.Identifier, images: [UIImage], selectionMode: NSPickerTouchBarItem.SelectionMode, target: Any?, action: Selector?)](nspickertouchbaritem/init(identifier:images:selectionmode:target:action:).md)
- [convenience init(identifier: NSTouchBarItem.Identifier, labels: [String], selectionMode: NSPickerTouchBarItem.SelectionMode, target: Any?, action: Selector?)](nspickertouchbaritem/init(identifier:labels:selectionmode:target:action:).md)
### Configuring picker appearance
- [var numberOfOptions: Int](nspickertouchbaritem/numberofoptions.md)
- [func setLabel(String, at: Int)](nspickertouchbaritem/setlabel(_:at:).md)
- [func label(at: Int) -> String?](nspickertouchbaritem/label(at:).md)
- [func setImage(UIImage?, at: Int)](nspickertouchbaritem/setimage(_:at:).md)
- [func image(at: Int) -> UIImage?](nspickertouchbaritem/image(at:).md)
- [var collapsedRepresentationImage: UIImage?](nspickertouchbaritem/collapsedrepresentationimage.md)
- [var collapsedRepresentationLabel: String](nspickertouchbaritem/collapsedrepresentationlabel.md)
- [var controlRepresentation: NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.property.md)
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
### Configuring picker state
- [var isEnabled: Bool](nspickertouchbaritem/isenabled.md)
- [func isEnabled(at: Int) -> Bool](nspickertouchbaritem/isenabled(at:).md)
- [func setEnabled(Bool, at: Int)](nspickertouchbaritem/setenabled(_:at:).md)
### Handling selection
- [var selectedIndex: Int](nspickertouchbaritem/selectedindex.md)
- [var selectionColor: UIColor?](nspickertouchbaritem/selectioncolor.md)
- [var selectionMode: NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.property.md)
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.
### Handling picker interaction
- [var action: Selector?](nspickertouchbaritem/action.md)
- [var target: AnyObject?](nspickertouchbaritem/target.md)
### Configuring bar customization
- [var customizationLabel: String!](nspickertouchbaritem/customizationlabel.md)

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
- [class NSSliderTouchBarItem](nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
- [class NSStepperTouchBarItem](nssteppertouchbaritem.md)
  A bar item that provides a stepper control for incrementing or decrementing a value.
- [class NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspickertouchbaritem)*