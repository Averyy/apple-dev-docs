# Accessibility modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Make your SwiftUI apps accessible to everyone, including people with disabilities.

#### Overview

Like all Apple UI frameworks, SwiftUI comes with built-in accessibility support. The framework introspects common elements like navigation views, lists, text fields, sliders, buttons, and so on, and provides basic accessibility labels and values by default. You don’t have to do any extra work to enable these standard accessibility features.

SwiftUI also provides tools to help you enhance the accessibility of your app. For example, you can explicitly add accessibility labels to elements in your UI using the [`accessibilityLabel(_:)`](./view/accessibilitylabel%28_%29.md) or the [`accessibilityValue(_:)`](./view/accessibilityvalue%28_%29.md) view modifier.

To learn more about adding accessibility features to your app, see [Accessibility fundamentals](./accessibility-fundamentals.md).

## Topics

### Labels
- [func accessibilityLabel(_:)](./view/accessibilitylabel%28_%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(_:isEnabled:)](./view/accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](./view/accessibilitylabel%28content%29.md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels(_:)](./view/accessibilityinputlabels%28_%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels(_:isEnabled:)](./view/accessibilityinputlabels%28_,isenabled%29.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](./view/accessibilitylabeledpair%28role,id,in%29.md)
  Pairs an accessibility element representing a label with the element for the matching content.
### Values
- [func accessibilityValue(_:)](./view/accessibilityvalue%28_%29.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(_:isEnabled:)](./view/accessibilityvalue%28_,isenabled%29.md)
  Adds a textual description of the value that the view contains.
### Hints
- [func accessibilityHint(_:)](./view/accessibilityhint%28_%29.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(_:isEnabled:)](./view/accessibilityhint%28_,isenabled%29.md)
  Communicates to the user what happens after performing the view’s action.
### Actions
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityaction%28_,_%29.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](./view/accessibilityactions%28_%29.md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](./view/accessibilityactions%28category,_%29.md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityAction(named:_:)](./view/accessibilityaction%28named,_%29.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](./view/accessibilityaction%28action,label%29.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I, Label>(intent: I, label: () -> Label) -> some View](./view/accessibilityaction%28intent,label%29.md)
  Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityaction%28_,intent%29.md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named:intent:)](./view/accessibilityaction%28named,intent%29.md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityadjustableaction%28_%29.md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityscrollaction%28_%29.md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(_:isEnabled:)](./view/accessibilityscrollstatus%28_,isenabled%29.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
### Gestures
- [func accessibilityActivationPoint(_:)](./view/accessibilityactivationpoint%28_%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](./view/accessibilityactivationpoint%28_,isenabled%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityDragPoint(_:description:)](./view/accessibilitydragpoint%28_,description%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](./view/accessibilitydragpoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](./view/accessibilitydroppoint%28_,description%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](./view/accessibilitydroppoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilitydirecttouch%28_,options%29.md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityzoomaction%28_%29.md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
### Elements
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](./view/accessibilityelement%28children%29.md)
  Creates a new accessibility element, or modifies the [`AccessibilityChildBehavior`](./accessibilitychildbehavior.md) of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](./view/accessibilitychildren%28children%29.md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityhidden%28_%29.md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityhidden%28_,isenabled%29.md)
  Specifies whether to hide this view from system accessibility features.
### Custom controls
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](./view/accessibilityrepresentation%28representation%29.md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityrespondstouserinteraction%28_%29.md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityrespondstouserinteraction%28_,isenabled%29.md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
### Custom content
- [func accessibilityCustomContent(_:_:importance:)](./view/accessibilitycustomcontent%28_,_,importance%29.md)
  Add additional accessibility information to the view.
### Working with rotors
- [func accessibilityRotor(_:entries:)](./view/accessibilityrotor%28_,entries%29.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor(_:entries:entryID:entryLabel:)](./view/accessibilityrotor%28_,entries,entryid,entrylabel%29.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:entries:entryLabel:)](./view/accessibilityrotor%28_,entries,entrylabel%29.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(_:textRanges:)](./view/accessibilityrotor%28_,textranges%29.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
### Configuring rotors
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](./view/accessibilityrotorentry%28id,in%29.md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](./view/accessibilitylinkedgroup%28id,in%29.md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilitysortpriority%28_%29.md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
### Focus
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](./view/accessibilityfocused%28_%29.md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](./view/accessibilityfocused%28_,equals%29.md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](./view/accessibilitydefaultfocus%28_,_%29.md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
### Traits
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityaddtraits%28_%29.md)
  Adds the given traits to the view.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityremovetraits%28_%29.md)
  Removes the given traits from this view.
### Identity
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityidentifier%28_%29.md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view.
### Color inversion
- [func accessibilityIgnoresInvertColors(Bool) -> some View](./view/accessibilityignoresinvertcolors%28_%29.md)
  Sets whether this view should ignore the system Smart Invert setting.
### Content descriptions
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilitytextcontenttype%28_%29.md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityheading%28_%29.md)
  Sets the accessibility level of this heading.
### VoiceOver
- [func speechAdjustedPitch(Double) -> some View](./view/speechadjustedpitch%28_%29.md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](./view/speechalwaysincludespunctuation%28_%29.md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](./view/speechannouncementsqueued%28_%29.md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](./view/speechspellsoutcharacters%28_%29.md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
### Charts
- [func accessibilityChartDescriptor<R>(R) -> some View](./view/accessibilitychartdescriptor%28_%29.md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
### Large content
- [func accessibilityShowsLargeContentViewer() -> some View](./view/accessibilityshowslargecontentviewer%28%29.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](./view/accessibilityshowslargecontentviewer%28_%29.md)
  Adds a custom large content view to be shown by the large content viewer.
### Quick actions
- [func accessibilityQuickAction<Style, Content>(style: Style, content: () -> Content) -> some View](./view/accessibilityquickaction%28style,content%29.md)
  Adds a quick action to be shown by the system when active.
- [func accessibilityQuickAction<Style, Content>(style: Style, isActive: Binding<Bool>, content: () -> Content) -> some View](./view/accessibilityquickaction%28style,isactive,content%29.md)
  Adds a quick action to be shown by the system when active.
### Using assistive access
- [func assistiveAccessNavigationIcon(Image) -> some View](./view/assistiveaccessnavigationicon%28_%29.md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](./view/assistiveaccessnavigationicon%28systemimage%29.md)
  Configures the view’s icon for purposes of navigation.

## See Also

### Configuring view elements
- [Appearance modifiers](./view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](./view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](./view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](./view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-accessibility)*