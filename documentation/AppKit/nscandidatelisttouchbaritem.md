# NSCandidateListTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSCandidateListTouchBarItem<CandidateType> where CandidateType : AnyObject
```

## Topics

### Providing a client and a delegate
- [var client: (any NSView & NSTextInputClient)?](nscandidatelisttouchbaritem/client.md)
  The client object for the candidate list item.
- [var delegate: (any NSCandidateListTouchBarItemDelegate)?](nscandidatelisttouchbaritem/delegate.md)
  The delegate of the candidate list item.
- [protocol NSCandidateListTouchBarItemDelegate](nscandidatelisttouchbaritemdelegate.md)
  A set of methods that a candidate list item delegate uses to enable selection state and list visibility.
### Populating the candidate list
- [func setCandidates([CandidateType], forSelectedRange: NSRange, in: String?)](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md)
  Sets an array of candidate objects to be displayed in the candidate list bar item.
- [var candidates: [CandidateType]](nscandidatelisttouchbaritem/candidates.md)
  The array of candidate objects previously set by [`setCandidates(_:forSelectedRange:in:)`](nscandidatelisttouchbaritem/setcandidates(_:forselectedrange:in:).md).
- [var attributedStringForCandidate: ((CandidateType, Int) -> NSAttributedString)?](nscandidatelisttouchbaritem/attributedstringforcandidate.md)
  A block that converts a candidate object into an attributed string for display in the candidate list item.
- [var allowsTextInputContextCandidates: Bool](nscandidatelisttouchbaritem/allowstextinputcontextcandidates.md)
  A Boolean value that specifies whether a candidate list item displays candidates from text input providers.
### Handling collapsible behavior
- [var allowsCollapsing: Bool](nscandidatelisttouchbaritem/allowscollapsing.md)
  A Boolean value that specifies whether the item can be collapsed.
- [var isCollapsed: Bool](nscandidatelisttouchbaritem/iscollapsed.md)
  A Boolean value that controls the visibility of the candidate list.
### Managing candidate list visibility
- [var isCandidateListVisible: Bool](nscandidatelisttouchbaritem/iscandidatelistvisible.md)
  A Boolean value that represents the visibility of this item’s candidate list.
- [func update(withInsertionPointVisibility: Bool)](nscandidatelisttouchbaritem/update(withinsertionpointvisibility:).md)
  Updates the candidate list visibility configuration based on the client’s insertion point state.
### Configuring bar customization
- [var customizationLabel: String!](nscandidatelisttouchbaritem/customizationlabel.md)
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
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem)*