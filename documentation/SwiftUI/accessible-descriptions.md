# Accessible descriptions

**Framework**: SwiftUI

Describe interface elements to help people understand what they represent.

#### Overview

SwiftUI can often infer some information about your user interface elements, but you can use accessibility modifiers to provide even more information for users that need it.

![None](https://docs-assets.developer.apple.com/published/f52d60c9e7c4a20b6bbd457a3d013a84/accessible-descriptions-hero%402x.png)

For design guidance, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility#Content-descriptions) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Applying labels
- [func accessibilityLabel(_:)](view/accessibilitylabel(_:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](view/accessibilitylabel(_:isenabled:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](view/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels(_:)](view/accessibilityinputlabels(_:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](view/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](view/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [enum AccessibilityLabeledPairRole](accessibilitylabeledpairrole.md)
  The role of an accessibility element in a label / content pair.
### Describing values
- [func accessibilityValue(_:)](view/accessibilityvalue(_:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(_:isEnabled:)](view/accessibilityvalue(_:isenabled:).md)
  Adds a textual description of the value that the view contains.
### Describing content
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [enum AccessibilityHeadingLevel](accessibilityheadinglevel.md)
  The hierarchy of a heading in relation to other headings.
- [struct AccessibilityTextContentType](accessibilitytextcontenttype.md)
  Textual context that assistive technologies can use to improve the presentation of spoken text.
### Describing charts
- [func accessibilityChartDescriptor<R>(R) -> some View](view/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [protocol AXChartDescriptorRepresentable](axchartdescriptorrepresentable.md)
  A type to generate an `AXChartDescriptor` object that you use to provide information about a chart and its data for an accessible experience in VoiceOver or other assistive technologies.
### Adding custom descriptions
- [func accessibilityCustomContent(_:_:importance:)](view/accessibilitycustomcontent(_:_:importance:).md)
  Add additional accessibility information to the view.
- [struct AccessibilityCustomContentKey](accessibilitycustomcontentkey.md)
  Key used to specify the identifier and label associated with an entry of additional accessibility information.
### Assigning traits to content
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [struct AccessibilityTraits](accessibilitytraits.md)
  A set of accessibility traits that describe how an element behaves.
### Offering hints
- [func accessibilityHint(_:)](view/accessibilityhint(_:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(_:isEnabled:)](view/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after performing the view’s action.
### Configuring VoiceOver
- [func speechAdjustedPitch(Double) -> some View](view/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](view/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](view/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](view/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.

## See Also

- [Accessibility fundamentals](accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible appearance](accessible-appearance.md)
  Enhance the legibility of content in your app’s interface.
- [Accessible controls](accessible-controls.md)
  Improve access to actions that your app can undertake.
- [Accessible navigation](accessible-navigation.md)
  Enable users to navigate to specific user interface elements using rotors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessible-descriptions)*