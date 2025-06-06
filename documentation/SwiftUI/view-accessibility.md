# Accessibility modifiers

**Framework**: SwiftUI

Make your SwiftUI apps accessible to everyone, including people with disabilities.

#### Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility support. The framework introspects common elements like navigation views, lists, text fields, sliders, buttons, and so on, and provides basic accessibility labels and values by default. You don’t have to do any extra work to enable these standard accessibility features.

SwiftUI also provides tools to help you enhance the accessibility of your app. For example, you can explicitly add accessibility labels to elements in your UI using the [`accessibilityLabel(_:)`](view/accessibilitylabel(_:).md) or the [`accessibilityValue(_:)`](view/accessibilityvalue(_:).md) view modifier.

To learn more about adding accessibility features to your app, see [`Accessibility fundamentals`](accessibility-fundamentals.md).

## Topics

### Labels
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
### Values
- [func accessibilityValue(_:)](view/accessibilityvalue(_:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(_:isEnabled:)](view/accessibilityvalue(_:isenabled:).md)
  Adds a textual description of the value that the view contains.
### Hints
- [func accessibilityHint(_:)](view/accessibilityhint(_:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(_:isEnabled:)](view/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after performing the view’s action.
### Actions
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](view/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityAction(named:_:)](view/accessibilityaction(named:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](view/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I, Label>(intent: I, label: () -> Label) -> some View](view/accessibilityaction(intent:label:).md)
  Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaction(_:intent:).md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named:intent:)](view/accessibilityaction(named:intent:).md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
### Gestures
- [func accessibilityActivationPoint(_:)](view/accessibilityactivationpoint(_:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](view/accessibilityactivationpoint(_:isenabled:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityDragPoint(_:description:)](view/accessibilitydragpoint(_:description:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](view/accessibilitydragpoint(_:description:isenabled:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](view/accessibilitydroppoint(_:description:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](view/accessibilitydroppoint(_:description:isenabled:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
### Elements
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](view/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](accessibilitychildbehavior.md) of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](view/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
### Custom controls
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](view/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
### Custom content
- [func accessibilityCustomContent(_:_:importance:)](view/accessibilitycustomcontent(_:_:importance:).md)
  Add additional accessibility information to the view.
### Working with rotors
- [func accessibilityRotor(_:entries:)](view/accessibilityrotor(_:entries:).md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor(_:entries:entryID:entryLabel:)](view/accessibilityrotor(_:entries:entryid:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:entries:entryLabel:)](view/accessibilityrotor(_:entries:entrylabel:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:textRanges:)](view/accessibilityrotor(_:textranges:).md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
### Configuring rotors
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](view/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](view/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
### Focus
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](view/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](view/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
### Traits
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
### Identity
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
### Color inversion
- [func accessibilityIgnoresInvertColors(Bool) -> some View](view/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
### Content descriptions
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
### VoiceOver
- [func speechAdjustedPitch(Double) -> some View](view/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](view/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](view/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](view/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
### Charts
- [func accessibilityChartDescriptor<R>(R) -> some View](view/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
### Large content
- [func accessibilityShowsLargeContentViewer() -> some View](view/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](view/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
### Quick actions
- [func accessibilityQuickAction<Style, Content>(style: Style, content: () -> Content) -> some View](view/accessibilityquickaction(style:content:).md)
  Adds a quick action to be shown by the system when active.
- [func accessibilityQuickAction<Style, Content>(style: Style, isActive: Binding<Bool>, content: () -> Content) -> some View](view/accessibilityquickaction(style:isactive:content:).md)
  Adds a quick action to be shown by the system when active.

## See Also

- [Appearance modifiers](view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-accessibility)*