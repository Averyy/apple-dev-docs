# View Implementations

**Framework**: MusicKit

## Topics

### Instance Methods
- [func accentColor(Color?) -> some View](artworkimage/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(activationpoint:)-431k4.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(activationpoint:)-9d017.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](artworkimage/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaction(named:_:)-1tuje.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaction(named:_:)-37d42.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaction(named:_:)-3a7uo.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringResource, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaction(named:_:)-568ej.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](artworkimage/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](artworkimage/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityactivationpoint(_:)-4vm2w.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityactivationpoint(_:)-812e5.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityactivationpoint(_:isenabled:)-3c1rd.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityactivationpoint(_:isenabled:)-8vem5.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityChartDescriptor<R>(R) -> some View](artworkimage/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [func accessibilityChildren<V>(children: () -> V) -> some View](artworkimage/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityCustomContent(LocalizedStringResource, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-1k2sx.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-25bbr.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-3nfu5.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-6k9ld.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-6nj2h.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-7au98.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-825hh.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-9s5zo.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-jy7u.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringResource, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-n3ft.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-tpq6.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitycustomcontent(_:_:importance:)-zbc4.md)
  Add additional accessibility information to the view.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](artworkimage/accessibilitydefaultfocus(_:_:).md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:)-2rwlq.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:)-4g0tq.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:)-8oggy.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:)-9pecq.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:isenabled:)-2llh6.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:isenabled:)-3svi1.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:isenabled:)-3yknv.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydragpoint(_:description:isenabled:)-4zyib.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:)-207st.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:)-77azq.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:)-7nqcu.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:)-yq3t.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:isenabled:)-1lvgx.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:isenabled:)-3oyc8.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:isenabled:)-42l16.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitydroppoint(_:description:isenabled:)-8xgw.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](artworkimage/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](artworkimage/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](artworkimage/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:)-3gg9d.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:)-5173h.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:)-7lhuf.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:)-8543q.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:isenabled:)-2rtfl.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:isenabled:)-3luw3.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:isenabled:)-6clj6.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityhint(_:isenabled:)-89l5b.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIgnoresInvertColors(Bool) -> some View](artworkimage/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:)-59kn2.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:)-6ffb9.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:)-95umg.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:isenabled:)-1f07b.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:isenabled:)-7cee5.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityinputlabels(_:isenabled:)-9rzqq.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:)-1z2z9.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:)-4laf.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:)-4stnq.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:)-7zwa0.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:isenabled:)-20crq.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:isenabled:)-59ytu.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:isenabled:)-5oi81.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitylabel(_:isenabled:)-8s46s.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](artworkimage/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](artworkimage/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](artworkimage/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilityQuickAction<Style, Content>(style: Style, content: () -> Content) -> some View](artworkimage/accessibilityquickaction(style:content:).md)
  Adds a quick action to be shown by the system when active.
- [func accessibilityQuickAction<Style, Content>(style: Style, isActive: Binding<Bool>, content: () -> Content) -> some View](artworkimage/accessibilityquickaction(style:isactive:content:).md)
  Adds a quick action to be shown by the system when active.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](artworkimage/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRotor<Content>(LocalizedStringResource, entries: () -> Content) -> some View](artworkimage/accessibilityrotor(_:entries:)-21hu6.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](artworkimage/accessibilityrotor(_:entries:)-48sn1.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](artworkimage/accessibilityrotor(_:entries:)-5zidr.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](artworkimage/accessibilityrotor(_:entries:)-7w9dk.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](artworkimage/accessibilityrotor(_:entries:)-9wtww.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entryid:entrylabel:)-83pqo.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringResource, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entryid:entrylabel:)-8uk3k.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entryid:entrylabel:)-9p123.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entryid:entrylabel:)-9rpf.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entryid:entrylabel:)-m31l.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entrylabel:)-5wrfp.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entrylabel:)-68uq8.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entrylabel:)-6spp5.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entrylabel:)-7anr5.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringResource, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](artworkimage/accessibilityrotor(_:entries:entrylabel:)-d7pu.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](artworkimage/accessibilityrotor(_:textranges:)-140u6.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringResource, textRanges: [Range<String.Index>]) -> some View](artworkimage/accessibilityrotor(_:textranges:)-4n011.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](artworkimage/accessibilityrotor(_:textranges:)-6kd6b.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](artworkimage/accessibilityrotor(_:textranges:)-6lb6v.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](artworkimage/accessibilityrotor(_:textranges:)-axpd.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](artworkimage/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityscrollstatus(_:isenabled:)-1pv5o.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityscrollstatus(_:isenabled:)-8rf40.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityscrollstatus(_:isenabled:)-8s213.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(some StringProtocol, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityscrollstatus(_:isenabled:)-99m8l.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityShowsLargeContentViewer() -> some View](artworkimage/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](artworkimage/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:)-5io2b.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:)-5jpk6.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:)-70az.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:)-8p7kd.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:isenabled:)-3jebt.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:isenabled:)-5ev2i.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:isenabled:)-8gt1u.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityvalue(_:isenabled:)-ojzn.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](artworkimage/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](artworkimage/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](artworkimage/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](artworkimage/alert(_:ispresented:actions:)-1vrzf.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<A>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A) -> some View](artworkimage/alert(_:ispresented:actions:)-6ha08.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](artworkimage/alert(_:ispresented:actions:)-6ptti.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](artworkimage/alert(_:ispresented:actions:)-6t38l.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](artworkimage/alert(_:ispresented:actions:message:)-1or0r.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](artworkimage/alert(_:ispresented:actions:message:)-1wylt.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](artworkimage/alert(_:ispresented:actions:message:)-8hhio.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](artworkimage/alert(_:ispresented:actions:message:)-9e20a.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](artworkimage/alert(_:ispresented:presenting:actions:)-14v8j.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](artworkimage/alert(_:ispresented:presenting:actions:)-16eqg.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](artworkimage/alert(_:ispresented:presenting:actions:)-3yqb0.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](artworkimage/alert(_:ispresented:presenting:actions:)-5kzsf.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/alert(_:ispresented:presenting:actions:message:)-1nb3x.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/alert(_:ispresented:presenting:actions:message:)-57pzj.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/alert(_:ispresented:presenting:actions:message:)-67ryz.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/alert(_:ispresented:presenting:actions:message:)-9clm6.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](artworkimage/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](artworkimage/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](artworkimage/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](artworkimage/alert(item:content:).md)
  Presents an alert to the user.
- [func alignmentGuide(DepthAlignment, computeValue: (ViewDimensions3D) -> CGFloat) -> some View](artworkimage/alignmentguide(_:computevalue:)-26bmg.md)
  Returns a view modified so that its value for the given `guide` is the result of passing the `ViewDimensions` of the underlying element to `computeValue`.
- [func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](artworkimage/alignmentguide(_:computevalue:)-60uml.md)
  Sets the view’s vertical alignment.
- [func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](artworkimage/alignmentguide(_:computevalue:)-92u87.md)
  Sets the view’s horizontal alignment.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](artworkimage/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
- [func allowsHitTesting(Bool) -> some View](artworkimage/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func allowsTightening(Bool) -> some View](artworkimage/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func allowsWindowActivationEvents() -> some View](artworkimage/allowswindowactivationevents.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](artworkimage/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](artworkimage/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](artworkimage/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func animation(Animation?) -> some View](artworkimage/animation(_:).md)
  Applies the given animation to all animatable values within this view.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](artworkimage/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation<V>(Animation?, value: V) -> some View](artworkimage/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](artworkimage/aspectratio(_:contentmode:)-1w20u.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
- [func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View](artworkimage/aspectratio(_:contentmode:)-4cp4r.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](artworkimage/aspectratio3d(_:contentmode:).md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.
- [func assistiveAccessNavigationIcon(Image) -> some View](artworkimage/assistiveaccessnavigationicon(_:).md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](artworkimage/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.
- [func attributedTextFormattingDefinition<S>(KeyPath<AttributeScopes, S.Type>) -> some View](artworkimage/attributedtextformattingdefinition(_:)-64keg.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<D>(D) -> some View](artworkimage/attributedtextformattingdefinition(_:)-6yb2y.md)
  Apply a text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<S>(S.Type) -> some View](artworkimage/attributedtextformattingdefinition(_:)-9whln.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](artworkimage/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func autocorrectionDisabled(Bool) -> some View](artworkimage/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](artworkimage/background(_:alignment:).md)
  Layers the given view behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](artworkimage/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](artworkimage/background(_:in:fillstyle:)-1w7uk.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](artworkimage/background(_:in:fillstyle:)-668ah.md)
  Sets the view’s background to a shape filled with a style.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](artworkimage/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](artworkimage/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](artworkimage/background(in:fillstyle:)-6tdmc.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](artworkimage/background(in:fillstyle:)-vn26.md)
  Sets the view’s background to a shape filled with the default background style.
- [func backgroundExtensionEffect() -> some View](artworkimage/backgroundextensioneffect.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](artworkimage/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](artworkimage/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundStyle<S>(S) -> some View](artworkimage/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func badge(Text?) -> some View](artworkimage/badge(_:)-3blwy.md)
  Generates a badge for the view from a text view.
- [func badge(Int) -> some View](artworkimage/badge(_:)-4kipc.md)
  Generates a badge for the view from an integer value.
- [func badge(LocalizedStringResource?) -> some View](artworkimage/badge(_:)-4ty6e.md)
  Generates a badge for the view from a localized string resource.
- [func badge<S>(S?) -> some View](artworkimage/badge(_:)-59267.md)
  Generates a badge for the view from a string.
- [func badge(LocalizedStringKey?) -> some View](artworkimage/badge(_:)-7afth.md)
  Generates a badge for the view from a localized string key.
- [func badgeProminence(BadgeProminence) -> some View](artworkimage/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [func baselineOffset(CGFloat) -> some View](artworkimage/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func blendMode(BlendMode) -> some View](artworkimage/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func blur(radius: CGFloat, opaque: Bool) -> some View](artworkimage/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func bold(Bool) -> some View](artworkimage/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func border<S>(S, width: CGFloat) -> some View](artworkimage/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func breakthroughEffect(BreakthroughEffect) -> some View](artworkimage/breakthrougheffect(_:).md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [func brightness(Double) -> some View](artworkimage/brightness(_:).md)
  Brightens this view by the specified amount.
- [func buttonBorderShape(ButtonBorderShape) -> some View](artworkimage/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](artworkimage/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func buttonSizing(ButtonSizing) -> some View](artworkimage/buttonsizing(_:).md)
- [func buttonStyle<S>(S) -> some View](artworkimage/buttonstyle(_:)-5tznu.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func buttonStyle<S>(S) -> some View](artworkimage/buttonstyle(_:)-7queo.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func clipShape<S>(S, style: FillStyle) -> some View](artworkimage/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func clipped(antialiased: Bool) -> some View](artworkimage/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func colorEffect(Shader, isEnabled: Bool) -> some View](artworkimage/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func colorInvert() -> some View](artworkimage/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](artworkimage/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func colorScheme(ColorScheme) -> some View](artworkimage/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func compositingGroup() -> some View](artworkimage/compositinggroup.md)
  Wraps this view in a compositing group.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:)-4rjjw.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:)-6sv83.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:)-7eoal.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:)-8dc94.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-1t77r.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-2264m.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-94xn8.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-uofu.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-1tglk.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-7h283.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-9ok8c.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-dpl1.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-10x5j.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-57id5.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-80694.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](artworkimage/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-971mb.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](artworkimage/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](artworkimage/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](artworkimage/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](artworkimage/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](artworkimage/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerShape<T>(T) -> some View](artworkimage/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](artworkimage/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentCaptureProtected(Bool) -> some View](artworkimage/contentcaptureprotected(_:).md)
- [func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) -> some View](artworkimage/contentmargins(_:_:for:)-46so6.md)
  Configures the content margin for a provided placement.
- [func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some View](artworkimage/contentmargins(_:_:for:)-66ndy.md)
  Configures the content margin for a provided placement.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](artworkimage/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](artworkimage/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [func contentShape<S>(S, eoFill: Bool) -> some View](artworkimage/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](artworkimage/contenttoolbar(for:content:)-3f05q.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](artworkimage/contenttoolbar(for:content:)-5zqu0.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentTransition(ContentTransition) -> some View](artworkimage/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](artworkimage/contextmenu(_:).md)
  Adds a context menu to the view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](artworkimage/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](artworkimage/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](artworkimage/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contrast(Double) -> some View](artworkimage/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func controlGroupStyle<S>(S) -> some View](artworkimage/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func controlSize(ControlSize) -> some View](artworkimage/controlsize(_:)-48fb2.md)
  Sets the size for controls within this view.
- [func controlSize<T>(T) -> some View](artworkimage/controlsize(_:)-50nhw.md)
  Limits the control size within the view to the given range.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](artworkimage/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func coordinateSpace<T>(name: T) -> some View](artworkimage/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func copyable<T>(@autoclosure () -> [T]) -> some View](artworkimage/copyable(_:).md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](artworkimage/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](artworkimage/cuttable(for:action:).md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func datePickerStyle<S>(S) -> some View](artworkimage/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](artworkimage/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultAppStorage(UserDefaults) -> some View](artworkimage/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](artworkimage/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func defaultHoverEffect(HoverEffect?) -> some View](artworkimage/defaulthovereffect(_:)-1zf7h.md)
  Sets the default hover effect to use for views within this view.
- [func defaultHoverEffect(some CustomHoverEffect) -> some View](artworkimage/defaulthovereffect(_:)-3gida.md)
  Sets the default hover effect to use within this view hierarchy.
- [func defaultScrollAnchor(UnitPoint?) -> some View](artworkimage/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](artworkimage/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](artworkimage/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [func defersSystemGestures(on: Edge.Set) -> some View](artworkimage/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func deleteDisabled(Bool) -> some View](artworkimage/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [func dialogIcon(Image?) -> some View](artworkimage/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogPreventsAppTermination(Bool?) -> some View](artworkimage/dialogpreventsapptermination(_:).md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
- [func dialogSeverity(DialogSeverity) -> some View](artworkimage/dialogseverity(_:).md)
- [func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>) -> some View](artworkimage/dialogsuppressiontoggle(_:issuppressed:)-2nje9.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringResource, isSuppressed: Binding<Bool>) -> some View](artworkimage/dialogsuppressiontoggle(_:issuppressed:)-4k3xb.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View](artworkimage/dialogsuppressiontoggle(_:issuppressed:)-7fgdv.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View](artworkimage/dialogsuppressiontoggle(_:issuppressed:)-iyp9.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](artworkimage/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func digitalCrownAccessory(Visibility) -> some View](artworkimage/digitalcrownaccessory(_:).md)
  Specifies the visibility of Digital Crown accessory Views on Apple Watch.
- [func digitalCrownAccessory<Content>(content: () -> Content) -> some View](artworkimage/digitalcrownaccessory(content:).md)
  Places an accessory View next to the Digital Crown on Apple Watch.
- [func digitalCrownRotation<V>(Binding<V>) -> some View](artworkimage/digitalcrownrotation(_:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, by: V.Stride?, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool) -> some View](artworkimage/digitalcrownrotation(_:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, from: V, through: V, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](artworkimage/digitalcrownrotation(_:from:through:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(Binding<V>, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](artworkimage/digitalcrownrotation(_:onchange:onidle:).md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by: V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](artworkimage/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:)-1saf8.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func digitalCrownRotation<V>(detent: Binding<V>, from: V, through: V, by: V.Stride, sensitivity: DigitalCrownRotationalSensitivity, isContinuous: Bool, isHapticFeedbackEnabled: Bool, onChange: (DigitalCrownEvent) -> Void, onIdle: () -> Void) -> some View](artworkimage/digitalcrownrotation(detent:from:through:by:sensitivity:iscontinuous:ishapticfeedbackenabled:onchange:onidle:)-2ghzm.md)
  Tracks Digital Crown rotations by updating the specified binding.
- [func disableAutocorrection(Bool?) -> some View](artworkimage/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func disabled(Bool) -> some View](artworkimage/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func disclosureGroupStyle<S>(S) -> some View](artworkimage/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [func dismissalConfirmationDialog<A>(LocalizedStringResource, shouldPresent: Bool, actions: () -> A) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:)-5he12.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<S, A>(S, shouldPresent: Bool, actions: () -> A) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:)-8vjtp.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:)-8ybgr.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(Text, shouldPresent: Bool, actions: () -> A) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:)-9pnm9.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<S, A, M>(S, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-6hkhq.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(LocalizedStringResource, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-70g13.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-8mrni.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(Text, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](artworkimage/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-9jjd4.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](artworkimage/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](artworkimage/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func dragConfiguration(DragConfiguration) -> some View](artworkimage/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, (ItemID) -> Data) -> some View](artworkimage/dragcontainer(for:id:in:_:).md)
  A container with draggable views. The drag payload is based on the current selection.
- [func dragContainer<Item, ItemID>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> ItemID?, (ItemID) -> Item?) -> some View](artworkimage/dragcontainer(for:id:in:selection:_:)-28tuu.md)
  A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (consuming Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> Array<ItemID>, (Array<ItemID>) -> Data) -> some View](artworkimage/dragcontainer(for:id:in:selection:_:)-4yfnp.md)
  A container with multiple selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, (Item.ID) -> Data) -> some View](artworkimage/dragcontainer(for:in:_:).md)
  A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Array<Item.ID>, (Array<Item.ID>) -> Data) -> some View](artworkimage/dragcontainer(for:in:selection:_:)-3xwn0.md)
  A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragContainer<Item>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Item.ID?, (Item.ID) -> Item?) -> some View](artworkimage/dragcontainer(for:in:selection:_:)-6i9mu.md)
  A container with single item selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](artworkimage/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func draggable<T>(@autoclosure () -> T) -> some View](artworkimage/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, @autoclosure () -> Item?) -> some View](artworkimage/draggable(_:_:).md)
  Activates this view as the source of a drag and drop operation. A view can be dragged separately, or as an element of a drag container.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](artworkimage/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<ItemID>(containerItemID: ItemID) -> some View](artworkimage/draggable(containeritemid:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [func draggable<T, ID>(for: T.Type, id: ID, (ID) -> T?) -> some View](artworkimage/draggable(for:id:_:).md)
  Activates this view as the source of a drag-and-drop operation.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](artworkimage/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](artworkimage/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](artworkimage/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](artworkimage/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](artworkimage/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.
- [func dynamicTypeSize(DynamicTypeSize) -> some View](artworkimage/dynamictypesize(_:)-3pwcm.md)
  Sets the Dynamic Type size within the view to the given value.
- [func dynamicTypeSize<T>(T) -> some View](artworkimage/dynamictypesize(_:)-53dul.md)
  Limits the Dynamic Type size within the view to the given range.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](artworkimage/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func environment<T>(T?) -> some View](artworkimage/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](artworkimage/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](artworkimage/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](artworkimage/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](artworkimage/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](artworkimage/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](artworkimage/exportsitemproviders(_:onexport:onedit:).md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](artworkimage/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(LocalizedStringResource) -> some View](artworkimage/filedialogconfirmationlabel(_:)-2crz2.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel<S>(S) -> some View](artworkimage/filedialogconfirmationlabel(_:)-7gd3l.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(Text?) -> some View](artworkimage/filedialogconfirmationlabel(_:)-7xwv7.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringKey) -> some View](artworkimage/filedialogconfirmationlabel(_:)-8fc6w.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](artworkimage/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](artworkimage/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](artworkimage/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage<S>(S) -> some View](artworkimage/filedialogmessage(_:)-45fiz.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringKey) -> some View](artworkimage/filedialogmessage(_:)-76zmp.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringResource) -> some View](artworkimage/filedialogmessage(_:)-98v0r.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(Text?) -> some View](artworkimage/filedialogmessage(_:)-9ooqk.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](artworkimage/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](artworkimage/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-53m72.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](artworkimage/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-61e08.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-1mxgj.md)
  Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-6biqx.md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](artworkimage/fileexporter(ispresented:documents:contenttype:oncompletion:)-154bo.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](artworkimage/fileexporter(ispresented:documents:contenttype:oncompletion:)-4a6wl.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-5qzj8.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-9tsfp.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(LocalizedStringResource) -> some View](artworkimage/fileexporterfilenamelabel(_:)-2m2ky.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(LocalizedStringKey) -> some View](artworkimage/fileexporterfilenamelabel(_:)-2yvip.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel<S>(S) -> some View](artworkimage/fileexporterfilenamelabel(_:)-44k40.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(Text?) -> some View](artworkimage/fileexporterfilenamelabel(_:)-4wsvs.md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](artworkimage/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](artworkimage/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](artworkimage/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](artworkimage/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](artworkimage/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func findDisabled(Bool) -> some View](artworkimage/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func findNavigator(isPresented: Binding<Bool>) -> some View](artworkimage/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func fixedSize() -> some View](artworkimage/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](artworkimage/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](artworkimage/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func focusEffectDisabled(Bool) -> some View](artworkimage/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func focusScope(Namespace.ID) -> some View](artworkimage/focusscope(_:).md)
  Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [func focusSection() -> some View](artworkimage/focussection.md)
  Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [func focusable(Bool) -> some View](artworkimage/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](artworkimage/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](artworkimage/focusable(_:onfocuschange:).md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func focused(FocusState<Bool>.Binding) -> some View](artworkimage/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](artworkimage/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focusedObject<T>(T) -> some View](artworkimage/focusedobject(_:)-3dbxy.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedObject<T>(T?) -> some View](artworkimage/focusedobject(_:)-7gp8g.md)
  Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.
- [func focusedSceneObject<T>(T?) -> some View](artworkimage/focusedsceneobject(_:)-1hr63.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneObject<T>(T) -> some View](artworkimage/focusedsceneobject(_:)-7y6gw.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneValue<T>(T?) -> some View](artworkimage/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some View](artworkimage/focusedscenevalue(_:_:)-2pid0.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some View](artworkimage/focusedscenevalue(_:_:)-35u8d.md)
  Creates a new view that exposes the provided value to other views whose state depends on the active scene.
- [func focusedValue<T>(T?) -> some View](artworkimage/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) -> some View](artworkimage/focusedvalue(_:_:)-23tqt.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) -> some View](artworkimage/focusedvalue(_:_:)-2il2i.md)
  Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.
- [func font(Font?) -> some View](artworkimage/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](artworkimage/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](artworkimage/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](artworkimage/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func foregroundColor(Color?) -> some View](artworkimage/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func foregroundStyle<S>(S) -> some View](artworkimage/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](artworkimage/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](artworkimage/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func formStyle<S>(S) -> some View](artworkimage/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func frame() -> some View](artworkimage/frame.md)
  Positions this view within an invisible frame.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](artworkimage/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](artworkimage/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](artworkimage/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](artworkimage/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](artworkimage/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](artworkimage/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func gaugeStyle<S>(S) -> some View](artworkimage/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func geometryGroup() -> some View](artworkimage/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](artworkimage/gesture(_:)-7j9bs.md)
  Attaches a `UIGestureRecognizerRepresentable` to the view.
- [func gesture(some NSGestureRecognizerRepresentable) -> some View](artworkimage/gesture(_:)-lx5q.md)
  Attaches an `NSGestureRecognizerRepresentable` to the view.
- [func gesture<T>(T, including: GestureMask) -> some View](artworkimage/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](artworkimage/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](artworkimage/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](artworkimage/glassbackgroundeffect(_:displaymode:).md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](artworkimage/glassbackgroundeffect(_:in:displaymode:).md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](artworkimage/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](artworkimage/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](artworkimage/glasseffect(_:in:isenabled:).md)
  Applies a glass effect to this view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](artworkimage/glasseffectid(_:in:).md)
  Associates an identity value to glass effects defined within this view.
- [func glassEffectTransition(GlassEffectTransition, isEnabled: Bool) -> some View](artworkimage/glasseffecttransition(_:isenabled:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](artworkimage/glasseffectunion(id:namespace:).md)
  Associates any glass effects defined within this view to a union with the provided id.
- [func grayscale(Double) -> some View](artworkimage/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func gridCellAnchor(UnitPoint) -> some View](artworkimage/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellColumns(Int) -> some View](artworkimage/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](artworkimage/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](artworkimage/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
- [func groupBoxStyle<S>(S) -> some View](artworkimage/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](artworkimage/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](artworkimage/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](artworkimage/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
- [func headerProminence(Prominence) -> some View](artworkimage/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func help(LocalizedStringResource) -> some View](artworkimage/help(_:)-2m773.md)
  Adds help text to a view using a localized string resource that you provide.
- [func help<S>(S) -> some View](artworkimage/help(_:)-2r45w.md)
  Adds help text to a view using a string that you provide.
- [func help(LocalizedStringKey) -> some View](artworkimage/help(_:)-5bg35.md)
  Adds help text to a view using a localized string that you provide.
- [func help(Text) -> some View](artworkimage/help(_:)-8ltrj.md)
  Adds help text to a view using a text view that you provide.
- [func hidden() -> some View](artworkimage/hidden.md)
  Hides this view unconditionally.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](artworkimage/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](artworkimage/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](artworkimage/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func horizontalRadioGroupLayout() -> some View](artworkimage/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func hoverEffect(HoverEffect) -> some View](artworkimage/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](artworkimage/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a `HoverEffectGroup`.
- [func hoverEffect(HoverEffect, isEnabled: Bool) -> some View](artworkimage/hovereffect(_:isenabled:)-2x6hm.md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, isEnabled: Bool) -> some View](artworkimage/hovereffect(_:isenabled:)-3dk79.md)
  Applies a hover effect to this view, while providing a way to conditionally enable or disable it.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](artworkimage/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectDisabled(Bool) -> some View](artworkimage/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func hoverEffectGroup() -> some View](artworkimage/hovereffectgroup.md)
  Adds an implicit `HoverEffectGroup` to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](artworkimage/hovereffectgroup(_:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](artworkimage/hovereffectgroup(id:in:behavior:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hueRotation(Angle) -> some View](artworkimage/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func id<ID>(ID) -> some View](artworkimage/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](artworkimage/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func imageScale(Image.Scale) -> some View](artworkimage/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](artworkimage/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](artworkimage/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](artworkimage/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func indexViewStyle<S>(S) -> some View](artworkimage/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](artworkimage/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](artworkimage/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](artworkimage/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
- [func interactionActivityTrackingTag(String) -> some View](artworkimage/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func interactiveDismissDisabled(Bool) -> some View](artworkimage/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func invalidatableContent(Bool) -> some View](artworkimage/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
- [func italic(Bool) -> some View](artworkimage/italic(_:).md)
  Applies italics to the text in this view.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](artworkimage/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func kerning(CGFloat) -> some View](artworkimage/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func keyboardShortcut(KeyboardShortcut?) -> some View](artworkimage/keyboardshortcut(_:)-9ycov.md)
  Assigns an optional keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyboardShortcut) -> some View](artworkimage/keyboardshortcut(_:)-tmpd.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](artworkimage/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](artworkimage/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardType(UIKeyboardType) -> some View](artworkimage/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](artworkimage/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](artworkimage/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func labelIconToTitleSpacing(CGFloat) -> some View](artworkimage/labelicontotitlespacing(_:).md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](artworkimage/labelreservediconwidth(_:).md)
  Set the width reserved for icons in labels.
- [func labelStyle<S>(S) -> some View](artworkimage/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func labeledContentStyle<S>(S) -> some View](artworkimage/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsHidden() -> some View](artworkimage/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](artworkimage/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](artworkimage/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](artworkimage/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [func layoutPriority(Double) -> some View](artworkimage/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](artworkimage/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.
- [func lineHeight(AttributedString.LineHeight?) -> some View](artworkimage/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func lineLimit(PartialRangeThrough<Int>) -> some View](artworkimage/linelimit(_:)-3ou1w.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(ClosedRange<Int>) -> some View](artworkimage/linelimit(_:)-7gd2f.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeFrom<Int>) -> some View](artworkimage/linelimit(_:)-94qzc.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(Int?) -> some View](artworkimage/linelimit(_:)-o84s.md)
  Sets the maximum number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](artworkimage/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](artworkimage/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func listItemTint(ListItemTint?) -> some View](artworkimage/listitemtint(_:)-1fak.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](artworkimage/listitemtint(_:)-9nd34.md)
  Sets a fixed tint color for content in a list.
- [func listRowBackground<V>(V?) -> some View](artworkimage/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func listRowHoverEffect(HoverEffect?) -> some View](artworkimage/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](artworkimage/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listRowInsets(EdgeInsets?) -> some View](artworkimage/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](artworkimage/listrowinsets(_:_:).md)
  Sets the insets of rows in a list on the specified edges.
- [func listRowPlatterColor(Color?) -> some View](artworkimage/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](artworkimage/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](artworkimage/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSpacing(CGFloat?) -> some View](artworkimage/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionIndexVisibility(Visibility) -> some View](artworkimage/listsectionindexvisibility(_:).md)
  Changes the visibility of the list section index.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](artworkimage/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](artworkimage/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](artworkimage/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSpacing(ListSectionSpacing) -> some View](artworkimage/listsectionspacing(_:)-2zotm.md)
  Sets the spacing between adjacent sections in a `List`.
- [func listSectionSpacing(CGFloat) -> some View](artworkimage/listsectionspacing(_:)-9gbsy.md)
  Sets the spacing between adjacent sections in a `List` to a custom value.
- [func listStyle<S>(S) -> some View](artworkimage/liststyle(_:).md)
  Sets the style for lists within this view.
- [func luminanceToAlpha() -> some View](artworkimage/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](artworkimage/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](artworkimage/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](artworkimage/manipulable(using:).md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](artworkimage/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
- [func mask<Mask>(Mask) -> some View](artworkimage/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](artworkimage/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](artworkimage/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](artworkimage/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](artworkimage/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](artworkimage/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](artworkimage/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func menuButtonStyle<S>(S) -> some View](artworkimage/menubuttonstyle(_:).md)
  Sets the style for menu buttons within this view.
- [func menuIndicator(Visibility) -> some View](artworkimage/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func menuOrder(MenuOrder) -> some View](artworkimage/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuStyle<S>(S) -> some View](artworkimage/menustyle(_:).md)
  Sets the style for menus within this view.
- [func minimumScaleFactor(CGFloat) -> some View](artworkimage/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](artworkimage/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](artworkimage/modifierkeyalternate(_:_:).md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
- [func monospaced(Bool) -> some View](artworkimage/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](artworkimage/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func moveDisabled(Bool) -> some View](artworkimage/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func multilineTextAlignment(TextAlignment) -> some View](artworkimage/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](artworkimage/multilinetextalignment(strategy:).md)
  A modifier for the default text alignment strategy in the view hierarchy.
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](artworkimage/musicsubscriptionoffer(ispresented:options:onloadcompletion:).md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [func navigationBarBackButtonHidden(Bool) -> some View](artworkimage/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarHidden(Bool) -> some View](artworkimage/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](artworkimage/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](artworkimage/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](artworkimage/navigationbaritems(trailing:).md)
- [func navigationBarTitle<S>(S) -> some View](artworkimage/navigationbartitle(_:)-14v5l.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(Text) -> some View](artworkimage/navigationbartitle(_:)-4ug46.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey) -> some View](artworkimage/navigationbartitle(_:)-gufc.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](artworkimage/navigationbartitle(_:displaymode:)-1l8pn.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](artworkimage/navigationbartitle(_:displaymode:)-509eu.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](artworkimage/navigationbartitle(_:displaymode:)-5bsg8.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](artworkimage/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](artworkimage/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](artworkimage/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](artworkimage/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationDocument<D>(D) -> some View](artworkimage/navigationdocument(_:)-26aqy.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(URL) -> some View](artworkimage/navigationdocument(_:)-2g0d5.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some View](artworkimage/navigationdocument(_:preview:)-22idv.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some View](artworkimage/navigationdocument(_:preview:)-5axcr.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some View](artworkimage/navigationdocument(_:preview:)-6m3ix.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some View](artworkimage/navigationdocument(_:preview:)-73tlo.md)
  Configures the view’s document for purposes of navigation.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](artworkimage/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](artworkimage/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](artworkimage/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationSplitViewStyle<S>(S) -> some View](artworkimage/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSubtitle<S>(S) -> some View](artworkimage/navigationsubtitle(_:)-360g8.md)
  Configures the view’s subtitle for purposes of navigation, using a string.
- [func navigationSubtitle(Text) -> some View](artworkimage/navigationsubtitle(_:)-44y3k.md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationSubtitle(LocalizedStringResource) -> some View](artworkimage/navigationsubtitle(_:)-7z0nx.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [func navigationSubtitle(LocalizedStringKey) -> some View](artworkimage/navigationsubtitle(_:)-7zfa6.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string.
- [func navigationTitle(LocalizedStringResource) -> some View](artworkimage/navigationtitle(_:)-2s7gc.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationTitle<V>(() -> V) -> some View](artworkimage/navigationtitle(_:)-2zhde.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle(LocalizedStringKey) -> some View](artworkimage/navigationtitle(_:)-5e87u.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle(Text) -> some View](artworkimage/navigationtitle(_:)-8sxbv.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTitle(Binding<String>) -> some View](artworkimage/navigationtitle(_:)-910tl.md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationTitle<S>(S) -> some View](artworkimage/navigationtitle(_:)-n1z6.md)
  Configures the view’s title for purposes of navigation, using a string.
- [func navigationTransition(some NavigationTransition) -> some View](artworkimage/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func navigationViewStyle<S>(S) -> some View](artworkimage/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func offset(CGSize) -> some View](artworkimage/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](artworkimage/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](artworkimage/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
- [func onAppear(perform: (() -> Void)?) -> some View](artworkimage/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View](artworkimage/onchange(of:initial:_:)-1j8bx.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, initial: Bool, () -> Void) -> some View](artworkimage/onchange(of:initial:_:)-94iid.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](artworkimage/onchange(of:perform:).md)
  Performs an action when a specified value changes.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](artworkimage/oncommand(_:perform:).md)
  Adds an action to perform in response to the given selector.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](artworkimage/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func onContinuousHover(coordinateSpace: some CoordinateSpaceProtocol, perform: (HoverPhase) -> Void) -> some View](artworkimage/oncontinuoushover(coordinatespace:perform:)-2gl22.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](artworkimage/oncontinuoushover(coordinatespace:perform:)-65nqw.md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](artworkimage/oncopycommand(perform:).md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](artworkimage/oncutcommand(perform:).md)
  Adds an action to perform in response to the system’s Cut command.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](artworkimage/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func onDisappear(perform: (() -> Void)?) -> some View](artworkimage/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onDrag(() -> NSItemProvider) -> some View](artworkimage/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](artworkimage/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](artworkimage/ondragsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](artworkimage/ondrop(of:delegate:)-1b5ra.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](artworkimage/ondrop(of:delegate:)-qijx.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](artworkimage/ondrop(of:istargeted:perform:)-4f7qe.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](artworkimage/ondrop(of:istargeted:perform:)-66rs7.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](artworkimage/ondrop(of:istargeted:perform:)-6sw18.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](artworkimage/ondrop(of:istargeted:perform:)-80ad1.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](artworkimage/ondropsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func onExitCommand(perform: (() -> Void)?) -> some View](artworkimage/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T) -> Void) -> some View](artworkimage/ongeometrychange(for:of:action:)-3qdm4.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T, T) -> Void) -> some View](artworkimage/ongeometrychange(for:of:action:)-9eqgs.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T) -> Void) -> some View](artworkimage/ongeometrychange3d(for:of:action:)-3lxtd.md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T, T) -> Void) -> some View](artworkimage/ongeometrychange3d(for:of:action:)-n9nf.md)
  Returns a new view that arranges to call `action(oldValue, newValue)` whenever the value computed by `value(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onHover(perform: (Bool) -> Void) -> some View](artworkimage/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](artworkimage/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](artworkimage/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](artworkimage/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](artworkimage/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](artworkimage/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](artworkimage/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](artworkimage/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](artworkimage/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](artworkimage/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](artworkimage/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](artworkimage/onlongtouchgesture(minimumduration:perform:ontouchingchanged:).md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](artworkimage/onmodifierkeyschanged(mask:initial:_:).md)
  Performs an action whenever the user presses or releases a hardware modifier key.
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](artworkimage/onmovecommand(perform:).md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onOpenURL(perform: (URL) -> ()) -> some View](artworkimage/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onOpenURL(prefersInApp: Bool) -> some View](artworkimage/onopenurl(prefersinapp:).md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](artworkimage/onpastecommand(of:perform:)-1i1u4.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) -> some View](artworkimage/onpastecommand(of:perform:)-3d6mu.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](artworkimage/onpastecommand(of:validator:perform:)-7p31l.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](artworkimage/onpastecommand(of:validator:perform:)-7pxqd.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](artworkimage/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](artworkimage/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](artworkimage/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](artworkimage/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](artworkimage/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](artworkimage/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase) -> Void) -> some View](artworkimage/onscrollphasechange(_:)-1fbks.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase, ScrollPhaseChangeContext) -> Void) -> some View](artworkimage/onscrollphasechange(_:)-8anlk.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](artworkimage/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](artworkimage/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](artworkimage/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func onTapGesture(count: Int, coordinateSpace: some CoordinateSpaceProtocol, perform: (CGPoint) -> Void) -> some View](artworkimage/ontapgesture(count:coordinatespace:perform:)-2m32l.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](artworkimage/ontapgesture(count:coordinatespace:perform:)-9yk8x.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](artworkimage/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](artworkimage/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func onWorldRecenter(action: (WorldRecenterPhase) -> Void) -> some View](artworkimage/onworldrecenter(action:)-3vlh0.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func onWorldRecenter(action: () -> Void) -> some View](artworkimage/onworldrecenter(action:)-4b7tu.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func opacity(Double) -> some View](artworkimage/opacity(_:).md)
  Sets the transparency of this view.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D, ornament: () -> Content) -> some View](artworkimage/ornament(visibility:attachmentanchor:contentalignment:ornament:)-6vd55.md)
  Presents an ornament.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () -> Content) -> some View](artworkimage/ornament(visibility:attachmentanchor:contentalignment:ornament:)-8cw9y.md)
  Presents an ornament.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](artworkimage/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](artworkimage/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](artworkimage/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](artworkimage/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](artworkimage/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](artworkimage/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func padding(EdgeInsets) -> some View](artworkimage/padding(_:)-61cyo.md)
  Adds a different padding amount to each edge of this view.
- [func padding(CGFloat) -> some View](artworkimage/padding(_:)-91im.md)
  Adds a specific padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](artworkimage/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(EdgeInsets3D) -> some View](artworkimage/padding3d(_:)-5flbz.md)
  Pads this view using the edge insets you specify.
- [func padding3D(CGFloat) -> some View](artworkimage/padding3d(_:)-8oo7j.md)
  Pads this view along all edge insets by the amount you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](artworkimage/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](artworkimage/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](artworkimage/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](artworkimage/pastedestination(for:action:validator:).md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [func persistentSystemOverlays(Visibility) -> some View](artworkimage/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](artworkimage/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](artworkimage/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](artworkimage/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func pickerStyle<S>(S) -> some View](artworkimage/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func pointerStyle(PointerStyle?) -> some View](artworkimage/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
- [func pointerVisibility(Visibility) -> some View](artworkimage/pointervisibility(_:).md)
  Sets the visibility of the pointer when it’s over the view.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](artworkimage/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](artworkimage/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func position(CGPoint) -> some View](artworkimage/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](artworkimage/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func preference<K>(key: K.Type, value: K.Value) -> some View](artworkimage/preference(key:value:).md)
  Sets a value for the given preference.
- [func preferredColorScheme(ColorScheme?) -> some View](artworkimage/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](artworkimage/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [func preferredWindowClippingMargins(Edge3D.Set, CGFloat?) -> some View](artworkimage/preferredwindowclippingmargins(_:_:)-30ihu.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func preferredWindowClippingMargins(Edge3D.Set, EdgeInsets3D) -> some View](artworkimage/preferredwindowclippingmargins(_:_:)-7ohd3.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](artworkimage/prefersdefaultfocus(_:in:).md)
  Indicates that the view should receive focus by default for a given namespace.
- [func presentationBackground<S>(S) -> some View](artworkimage/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](artworkimage/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](artworkimage/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](artworkimage/presentationbreakthrougheffect(_:).md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](artworkimage/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](artworkimage/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](artworkimage/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](artworkimage/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationDetents(Set<PresentationDetent>) -> some View](artworkimage/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](artworkimage/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](artworkimage/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationPreventsAppTermination(Bool?) -> some View](artworkimage/presentationpreventsapptermination(_:).md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [func presentationSizing(some PresentationSizing) -> some View](artworkimage/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func presentedWindowStyle<S>(S) -> some View](artworkimage/presentedwindowstyle(_:).md)
  Sets the style for windows created by interacting with this view.
- [func presentedWindowToolbarStyle<S>(S) -> some View](artworkimage/presentedwindowtoolbarstyle(_:).md)
  Sets the style for the toolbar in windows created by interacting with this view.
- [func previewContext<C>(C) -> some View](artworkimage/previewcontext(_:).md)
  Declares a context for the preview.
- [func previewDevice(PreviewDevice?) -> some View](artworkimage/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](artworkimage/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](artworkimage/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewLayout(PreviewLayout) -> some View](artworkimage/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func privacySensitive(Bool) -> some View](artworkimage/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func progressViewStyle<S>(S) -> some View](artworkimage/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func projectionEffect(ProjectionTransform) -> some View](artworkimage/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func redacted(reason: RedactionReasons) -> some View](artworkimage/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func refreshable(action: () async -> Void) -> some View](artworkimage/refreshable(action:).md)
  Marks this view as refreshable.
- [func renameAction(() -> Void) -> some View](artworkimage/renameaction(_:)-109hq.md)
  Sets a closure to run for the rename action.
- [func renameAction(FocusState<Bool>.Binding) -> some View](artworkimage/renameaction(_:)-44zni.md)
  Sets the rename action in the environment to update focus state.
- [func replaceDisabled(Bool) -> some View](artworkimage/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](artworkimage/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D) -> some View](artworkimage/rotation3deffect(_:axis:anchor:)-1ckxt.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> some View](artworkimage/rotation3deffect(_:axis:anchor:)-5vnb2.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>](artworkimage/rotation3deffect(_:axis:anchor:)-85dwb.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](artworkimage/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DLayout(Rotation3D) -> some View](artworkimage/rotation3dlayout(_:).md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: RotationAxis3D) -> some View](artworkimage/rotation3dlayout(_:axis:)-4vmul.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat)) -> some View](artworkimage/rotation3dlayout(_:axis:)-5o2u0.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](artworkimage/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](artworkimage/safeareabar(edge:alignment:spacing:content:)-7jtv8.md)
  Renders the provided content appropriately to be displayed as a custom bar.
- [func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](artworkimage/safeareabar(edge:alignment:spacing:content:)-utpb.md)
  Renders the provided content appropriate to be displayed as a custom bar.
- [func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> V) -> some View](artworkimage/safeareainset(edge:alignment:spacing:content:)-2d5u1.md)
  Shows the specified content above or below the modified view.
- [func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> V) -> some View](artworkimage/safeareainset(edge:alignment:spacing:content:)-9gojc.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(EdgeInsets) -> some View](artworkimage/safeareapadding(_:)-609ld.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(CGFloat) -> some View](artworkimage/safeareapadding(_:)-8lv51.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](artworkimage/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func saturation(Double) -> some View](artworkimage/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View](artworkimage/scaleeffect(_:anchor:)-158ku.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self, _UniformScaleEffect>](artworkimage/scaleeffect(_:anchor:)-1qadn.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](artworkimage/scaleeffect(_:anchor:)-5qqea.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> some View](artworkimage/scaleeffect(_:anchor:)-7mj03.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View](artworkimage/scaleeffect(_:anchor:)-8z7bx.md)
  Scales this view uniformly by the specified size in each dimension, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](artworkimage/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](artworkimage/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func scaledToFill() -> some View](artworkimage/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](artworkimage/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](artworkimage/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaledToFit3D() -> some View](artworkimage/scaledtofit3d.md)
  Scales this view to fit its parent.
- [func scenePadding(Edge.Set) -> some View](artworkimage/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](artworkimage/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](artworkimage/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollClipDisabled(Bool) -> some View](artworkimage/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func scrollContentBackground(Visibility) -> some View](artworkimage/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollDisabled(Bool) -> some View](artworkimage/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](artworkimage/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](artworkimage/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](artworkimage/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](artworkimage/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](artworkimage/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](artworkimage/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](artworkimage/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](artworkimage/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](artworkimage/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](artworkimage/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](artworkimage/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](artworkimage/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](artworkimage/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func searchCompletion(String) -> some View](artworkimage/searchcompletion(_:)-5izc6.md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchCompletion<T>(T) -> some View](artworkimage/searchcompletion(_:)-9w8s4.md)
  Associates a search token with the value of this view when used as a search suggestion.
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](artworkimage/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](artworkimage/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](artworkimage/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](artworkimage/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](artworkimage/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](artworkimage/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchSuggestions<S>(() -> S) -> some View](artworkimage/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](artworkimage/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](artworkimage/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:ispresented:placement:prompt:token:)-3841o.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:ispresented:placement:prompt:token:)-8mr68.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:ispresented:placement:prompt:token:)-8w6zi.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:ispresented:placement:prompt:token:)-xxu9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:placement:prompt:token:)-2bfg8.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:placement:prompt:token:)-2v7xu.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:placement:prompt:token:)-6wbej.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](artworkimage/searchable(text:editabletokens:placement:prompt:token:)-9f7f1.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S) -> some View](artworkimage/searchable(text:ispresented:placement:prompt:)-3ukza.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](artworkimage/searchable(text:ispresented:placement:prompt:)-9hb5m.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](artworkimage/searchable(text:ispresented:placement:prompt:)-9p3ts.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?) -> some View](artworkimage/searchable(text:ispresented:placement:prompt:)-9wo3o.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](artworkimage/searchable(text:placement:prompt:)-24ctv.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](artworkimage/searchable(text:placement:prompt:)-3xlhz.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](artworkimage/searchable(text:placement:prompt:)-6vuxc.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](artworkimage/searchable(text:placement:prompt:)-7lkzb.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](artworkimage/searchable(text:placement:prompt:suggestions:)-1fcz6.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](artworkimage/searchable(text:placement:prompt:suggestions:)-6fuxk.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](artworkimage/searchable(text:placement:prompt:suggestions:)-7f3re.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:ispresented:placement:prompt:token:)-18g7y.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:ispresented:placement:prompt:token:)-1tp9g.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:ispresented:placement:prompt:token:)-5wedg.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:ispresented:placement:prompt:token:)-9di98.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:placement:prompt:token:)-2x152.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:placement:prompt:token:)-5t4qw.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:placement:prompt:token:)-85vj.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:placement:prompt:token:)-8c1z7.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-2m9id.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-72x4x.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-8ya9y.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-z93u.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-3af7u.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-6yrbx.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-7e39v.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](artworkimage/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-nciy.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func sectionActions<Content>(content: () -> Content) -> some View](artworkimage/sectionactions(content:).md)
  Adds custom actions to a section.
- [func sectionIndexLabel<S>(S?) -> some View](artworkimage/sectionindexlabel(_:)-1v92v.md)
  Sets the title that is used for the section index label pointing to this section, typically only a single character long.
- [func sectionIndexLabel(Text?) -> some View](artworkimage/sectionindexlabel(_:)-1w454.md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
- [func selectionDisabled(Bool) -> some View](artworkimage/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](artworkimage/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](artworkimage/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](artworkimage/sensoryfeedback(trigger:_:)-1j0q6.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, () -> SensoryFeedback?) -> some View](artworkimage/sensoryfeedback(trigger:_:)-4moqt.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](artworkimage/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](artworkimage/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](artworkimage/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](artworkimage/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](artworkimage/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](artworkimage/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](artworkimage/spatialoverlay(alignment:content:).md)
  Adds secondary views within the 3D bounds of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](artworkimage/spatialoverlaypreferencevalue(_:alignment:_:).md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
- [func speechAdjustedPitch(Double) -> some View](artworkimage/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](artworkimage/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](artworkimage/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](artworkimage/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](artworkimage/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [func statusBar(hidden: Bool) -> some View](artworkimage/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func statusBarHidden(Bool) -> some View](artworkimage/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](artworkimage/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func submitLabel(SubmitLabel) -> some View](artworkimage/submitlabel(_:).md)
  Sets the submit label for this view.
- [func submitScope(Bool) -> some View](artworkimage/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](artworkimage/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](artworkimage/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](artworkimage/symbolcolorrenderingmode(_:).md)
  Sets the color rendering mode for symbol images.
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](artworkimage/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](artworkimage/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](artworkimage/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](artworkimage/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](artworkimage/symbolvariablevaluemode(_:).md)
  Sets the variable value mode mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](artworkimage/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](artworkimage/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabItem<V>(() -> V) -> some View](artworkimage/tabitem(_:).md)
  Sets the tab bar item associated with this view.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](artworkimage/tabviewbottomaccessory(content:).md)
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](artworkimage/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](artworkimage/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](artworkimage/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](artworkimage/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewStyle<S>(S) -> some View](artworkimage/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func tableColumnHeaders(Visibility) -> some View](artworkimage/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func tableStyle<S>(S) -> some View](artworkimage/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func tag<V>(V, includeOptional: Bool) -> some View](artworkimage/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](artworkimage/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](artworkimage/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func textCase(Text.Case?) -> some View](artworkimage/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textContentType(UITextContentType?) -> some View](artworkimage/textcontenttype(_:)-517lr.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textContentType(NSTextContentType?) -> some View](artworkimage/textcontenttype(_:)-571aw.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(WKTextContentType?) -> some View](artworkimage/textcontenttype(_:)-n1vc.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [func textEditorStyle(some TextEditorStyle) -> some View](artworkimage/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [func textFieldStyle<S>(S) -> some View](artworkimage/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](artworkimage/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputCompletion(String) -> some View](artworkimage/textinputcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](artworkimage/textinputformattingcontrolvisibility(_:for:).md)
  Define which system text formatting controls are available.
- [func textInputSuggestions<S>(() -> S) -> some View](artworkimage/textinputsuggestions(_:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](artworkimage/textinputsuggestions(_:content:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](artworkimage/textinputsuggestions(_:id:content:).md)
  Configures the text input suggestions for this view.
- [func textRenderer<T>(T) -> some View](artworkimage/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](artworkimage/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textSelection<S>(S) -> some View](artworkimage/textselection(_:).md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](artworkimage/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tint(Color?) -> some View](artworkimage/tint(_:).md)
  Sets the tint color within this view.
- [func toggleStyle<S>(S) -> some View](artworkimage/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](artworkimage/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar<Content>(content: () -> Content) -> some View](artworkimage/toolbar(content:)-5t35o.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(content: () -> Content) -> some View](artworkimage/toolbar(content:)-9pnx2.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](artworkimage/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](artworkimage/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View](artworkimage/toolbarbackground(_:for:)-6u7m0.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View](artworkimage/toolbarbackground(_:for:)-9e65v.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](artworkimage/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](artworkimage/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](artworkimage/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](artworkimage/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func toolbarRole(ToolbarRole) -> some View](artworkimage/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](artworkimage/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](artworkimage/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](artworkimage/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func touchBar<Content>(TouchBar<Content>) -> some View](artworkimage/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBar<Content>(content: () -> Content) -> some View](artworkimage/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBarCustomizationLabel(Text) -> some View](artworkimage/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](artworkimage/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [func touchBarItemPrincipal(Bool) -> some View](artworkimage/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func tracking(CGFloat) -> some View](artworkimage/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func transaction((inout Transaction) -> Void) -> some View](artworkimage/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](artworkimage/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](artworkimage/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transform3DEffect(AffineTransform3D) -> some View](artworkimage/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](artworkimage/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformEffect(CGAffineTransform) -> some View](artworkimage/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](artworkimage/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](artworkimage/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func transition(AnyTransition) -> some View](artworkimage/transition(_:)-2odcc.md)
  Associates a transition with the view.
- [func transition<T>(T) -> some View](artworkimage/transition(_:)-509on.md)
  Associates a transition with the view.
- [func truncationMode(Text.TruncationMode) -> some View](artworkimage/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typeSelectEquivalent<S>(S) -> some View](artworkimage/typeselectequivalent(_:)-1ucf2.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(Text?) -> some View](artworkimage/typeselectequivalent(_:)-2hqf7.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringResource) -> some View](artworkimage/typeselectequivalent(_:)-nvxr.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringKey) -> some View](artworkimage/typeselectequivalent(_:)-ohio.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View](artworkimage/typesettinglanguage(_:isenabled:)-16f0i.md)
  Specifies the language for typesetting.
- [func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View](artworkimage/typesettinglanguage(_:isenabled:)-3i2t1.md)
  Specifies the language for typesetting.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](artworkimage/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func unredacted() -> some View](artworkimage/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func upperLimbVisibility(Visibility) -> some View](artworkimage/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an `ImmersiveSpace` scene is presented.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](artworkimage/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](artworkimage/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](artworkimage/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](artworkimage/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [func volumeBaseplateVisibility(Visibility) -> some View](artworkimage/volumebaseplatevisibility(_:).md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](artworkimage/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](artworkimage/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](artworkimage/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeAnchor(UnitPoint?) -> some View](artworkimage/windowresizeanchor(_:).md)
  Sets the window anchor point used when the size of the view changes such that the window must resize.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](artworkimage/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](artworkimage/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](artworkimage/writingdirection(strategy:).md)
  A modifier for the default text writing direction strategy in the view hierarchy.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](artworkimage/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](artworkimage/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [func zIndex(Double) -> some View](artworkimage/zindex(_:).md)
  Controls the display order of overlapping views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/view-implementations)*