# View Implementations

**Framework**: App Intents

## Topics

### Instance Methods
- [func accentColor(Color?) -> some View](shortcutslink/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(activationpoint:)-4ly8n.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(activationpoint:)-99nld.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(_:intent:).md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](shortcutslink/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I, Label>(intent: I, label: () -> Label) -> some View](shortcutslink/accessibilityaction(intent:label:).md)
  Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:_:)-4fqf2.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringResource, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:_:)-79oau.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:_:)-98uqi.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:_:)-r43d.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S, I>(named: S, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:intent:)-28544.md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(named: LocalizedStringResource, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:intent:)-7q2c6.md)
  Adds an accessibility action labeled with the localized representation of `nameResource` to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(named: LocalizedStringKey, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:intent:)-867fa.md)
  Adds an accessibility action labeled with the localized representation of `nameKey` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(named: Text, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaction(named:intent:)-8jldn.md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityActions<Content>(() -> Content) -> some View](shortcutslink/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](shortcutslink/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityactivationpoint(_:)-17i3o.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityactivationpoint(_:)-2kbzb.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityactivationpoint(_:isenabled:)-77832.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityactivationpoint(_:isenabled:)-8nmj0.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityChartDescriptor<R>(R) -> some View](shortcutslink/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [func accessibilityChildren<V>(children: () -> V) -> some View](shortcutslink/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityCustomContent(LocalizedStringResource, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-2vrla.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-4buwk.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringResource, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-4zyql.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-5fyx4.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-71nyz.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-89s4u.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-8j83c.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-9grq4.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-9pmyq.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-ajnf.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-vryw.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitycustomcontent(_:_:importance:)-z8na.md)
  Add additional accessibility information to the view.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](shortcutslink/accessibilitydefaultfocus(_:_:).md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:)-1leck.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:)-1u5m0.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:)-54hcs.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:)-6u2lh.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:isenabled:)-189u3.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:isenabled:)-5njt8.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:isenabled:)-61zvb.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydragpoint(_:description:isenabled:)-9pt3c.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:)-3lnlt.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:)-3pun2.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:)-7u8dq.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:)-7vnvh.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:isenabled:)-34ftt.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:isenabled:)-4qh8p.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:isenabled:)-4x6lb.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitydroppoint(_:description:isenabled:)-v0xr.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](shortcutslink/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](shortcutslink/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](shortcutslink/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:)-3czqo.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:)-4offr.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:)-61chm.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:)-8b3m.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:isenabled:)-5k00a.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:isenabled:)-5rq02.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:isenabled:)-69wwy.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityhint(_:isenabled:)-6qcf9.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIgnoresInvertColors(Bool) -> some View](shortcutslink/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:)-5l7xv.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:)-63m6f.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:)-9sprg.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:isenabled:)-1d1x8.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:isenabled:)-4wm57.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityinputlabels(_:isenabled:)-5l8e3.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:)-1taf3.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:)-1xc1a.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:)-2vnrg.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:)-4in4z.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:isenabled:)-2m77u.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:isenabled:)-359nu.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:isenabled:)-8na38.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitylabel(_:isenabled:)-9sd8k.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](shortcutslink/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](shortcutslink/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](shortcutslink/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](shortcutslink/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](shortcutslink/accessibilityrotor(_:entries:)-1bbab.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](shortcutslink/accessibilityrotor(_:entries:)-3ztdd.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](shortcutslink/accessibilityrotor(_:entries:)-50h30.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](shortcutslink/accessibilityrotor(_:entries:)-9u08x.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<Content>(LocalizedStringResource, entries: () -> Content) -> some View](shortcutslink/accessibilityrotor(_:entries:)-ktzu.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entryid:entrylabel:)-53k89.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entryid:entrylabel:)-756rn.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entryid:entrylabel:)-7bhaz.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringResource, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entryid:entrylabel:)-8p3ty.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entryid:entrylabel:)-8q75m.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entrylabel:)-10j83.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringResource, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entrylabel:)-617lf.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entrylabel:)-9mth9.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entrylabel:)-9qzuh.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](shortcutslink/accessibilityrotor(_:entries:entrylabel:)-utdt.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](shortcutslink/accessibilityrotor(_:textranges:)-2mep8.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](shortcutslink/accessibilityrotor(_:textranges:)-5l3al.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringResource, textRanges: [Range<String.Index>]) -> some View](shortcutslink/accessibilityrotor(_:textranges:)-8c7ct.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](shortcutslink/accessibilityrotor(_:textranges:)-8gmf2.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](shortcutslink/accessibilityrotor(_:textranges:)-8mglc.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](shortcutslink/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(some StringProtocol, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityscrollstatus(_:isenabled:)-3o5qv.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityscrollstatus(_:isenabled:)-75h5a.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityscrollstatus(_:isenabled:)-8gvyg.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityscrollstatus(_:isenabled:)-8k67.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityShowsLargeContentViewer() -> some View](shortcutslink/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](shortcutslink/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:)-2h1bv.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:)-6jvrt.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:)-8poju.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:)-o1oe.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:isenabled:)-2pg5f.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:isenabled:)-80uvm.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:isenabled:)-8lpmp.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityvalue(_:isenabled:)-9iplr.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](shortcutslink/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](shortcutslink/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](shortcutslink/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](shortcutslink/alert(_:ispresented:actions:)-2dqe4.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](shortcutslink/alert(_:ispresented:actions:)-7wqgn.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<A>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A) -> some View](shortcutslink/alert(_:ispresented:actions:)-9k77j.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](shortcutslink/alert(_:ispresented:actions:)-qr13.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](shortcutslink/alert(_:ispresented:actions:message:)-22eqj.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](shortcutslink/alert(_:ispresented:actions:message:)-2ssu3.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](shortcutslink/alert(_:ispresented:actions:message:)-2yiua.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](shortcutslink/alert(_:ispresented:actions:message:)-7lfei.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:)-13mxn.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:)-36epo.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:)-4ievo.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:)-81nqk.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:message:)-1f51p.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:message:)-1nhxz.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:message:)-2lob.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/alert(_:ispresented:presenting:actions:message:)-81vvt.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](shortcutslink/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](shortcutslink/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](shortcutslink/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](shortcutslink/alert(item:content:).md)
  Presents an alert to the user.
- [func alignmentGuide(DepthAlignment, computeValue: (ViewDimensions3D) -> CGFloat) -> some View](shortcutslink/alignmentguide(_:computevalue:)-3r1ji.md)
  Returns a view modified so that its value for the given `guide` is the result of passing the `ViewDimensions` of the underlying element to `computeValue`.
- [func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](shortcutslink/alignmentguide(_:computevalue:)-55stq.md)
  Sets the view’s horizontal alignment.
- [func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](shortcutslink/alignmentguide(_:computevalue:)-r8ti.md)
  Sets the view’s vertical alignment.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](shortcutslink/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
- [func allowsHitTesting(Bool) -> some View](shortcutslink/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func allowsTightening(Bool) -> some View](shortcutslink/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func allowsWindowActivationEvents() -> some View](shortcutslink/allowswindowactivationevents.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](shortcutslink/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](shortcutslink/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func animation(Animation?) -> some View](shortcutslink/animation(_:).md)
  Applies the given animation to all animatable values within this view.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](shortcutslink/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation<V>(Animation?, value: V) -> some View](shortcutslink/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View](shortcutslink/aspectratio(_:contentmode:)-5ybt2.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](shortcutslink/aspectratio(_:contentmode:)-xqmx.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](shortcutslink/aspectratio3d(_:contentmode:).md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.
- [func assistiveAccessNavigationIcon(Image) -> some View](shortcutslink/assistiveaccessnavigationicon(_:).md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](shortcutslink/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.
- [func attributedTextFormattingDefinition<S>(KeyPath<AttributeScopes, S.Type>) -> some View](shortcutslink/attributedtextformattingdefinition(_:)-1jxdl.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<D>(D) -> some View](shortcutslink/attributedtextformattingdefinition(_:)-34d0f.md)
  Apply a text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<S>(S.Type) -> some View](shortcutslink/attributedtextformattingdefinition(_:)-8b03.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](shortcutslink/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func autocorrectionDisabled(Bool) -> some View](shortcutslink/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](shortcutslink/background(_:alignment:).md)
  Layers the given view behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](shortcutslink/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](shortcutslink/background(_:in:fillstyle:)-42iz8.md)
  Sets the view’s background to a shape filled with a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](shortcutslink/background(_:in:fillstyle:)-7zq0c.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](shortcutslink/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](shortcutslink/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](shortcutslink/background(in:fillstyle:)-3rged.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](shortcutslink/background(in:fillstyle:)-94liv.md)
  Sets the view’s background to a shape filled with the default background style.
- [func backgroundExtensionEffect() -> some View](shortcutslink/backgroundextensioneffect.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](shortcutslink/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](shortcutslink/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundStyle<S>(S) -> some View](shortcutslink/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func badge(LocalizedStringResource?) -> some View](shortcutslink/badge(_:)-2jgpc.md)
  Generates a badge for the view from a localized string resource.
- [func badge(LocalizedStringKey?) -> some View](shortcutslink/badge(_:)-43zjv.md)
  Generates a badge for the view from a localized string key.
- [func badge(Int) -> some View](shortcutslink/badge(_:)-5hnb.md)
  Generates a badge for the view from an integer value.
- [func badge<S>(S?) -> some View](shortcutslink/badge(_:)-7uk2g.md)
  Generates a badge for the view from a string.
- [func badge(Text?) -> some View](shortcutslink/badge(_:)-9mvc6.md)
  Generates a badge for the view from a text view.
- [func badgeProminence(BadgeProminence) -> some View](shortcutslink/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [func baselineOffset(CGFloat) -> some View](shortcutslink/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func blendMode(BlendMode) -> some View](shortcutslink/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func blur(radius: CGFloat, opaque: Bool) -> some View](shortcutslink/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func bold(Bool) -> some View](shortcutslink/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func border<S>(S, width: CGFloat) -> some View](shortcutslink/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func breakthroughEffect(BreakthroughEffect) -> some View](shortcutslink/breakthrougheffect(_:).md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [func brightness(Double) -> some View](shortcutslink/brightness(_:).md)
  Brightens this view by the specified amount.
- [func buttonBorderShape(ButtonBorderShape) -> some View](shortcutslink/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](shortcutslink/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func buttonSizing(ButtonSizing) -> some View](shortcutslink/buttonsizing(_:).md)
- [func buttonStyle<S>(S) -> some View](shortcutslink/buttonstyle(_:)-4zdrd.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonStyle<S>(S) -> some View](shortcutslink/buttonstyle(_:)-5qmbr.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func clipShape<S>(S, style: FillStyle) -> some View](shortcutslink/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func clipped(antialiased: Bool) -> some View](shortcutslink/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func colorEffect(Shader, isEnabled: Bool) -> some View](shortcutslink/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func colorInvert() -> some View](shortcutslink/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](shortcutslink/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func colorScheme(ColorScheme) -> some View](shortcutslink/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func compositingGroup() -> some View](shortcutslink/compositinggroup.md)
  Wraps this view in a compositing group.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:)-2xa9k.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:)-4tqxw.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:)-540w9.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:)-q22q.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-33psm.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-3gca1.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-67tv0.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-j261.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-1eroa.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-25f3t.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-2vszn.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func confirmationDialog<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-53t7a.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-1lq0n.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-6kt07.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-87b6i.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](shortcutslink/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-9ijow.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](shortcutslink/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](shortcutslink/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](shortcutslink/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](shortcutslink/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](shortcutslink/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerShape<T>(T) -> some View](shortcutslink/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](shortcutslink/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentCaptureProtected(Bool) -> some View](shortcutslink/contentcaptureprotected(_:).md)
- [func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) -> some View](shortcutslink/contentmargins(_:_:for:)-3g4op.md)
  Configures the content margin for a provided placement.
- [func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some View](shortcutslink/contentmargins(_:_:for:)-4dp7d.md)
  Configures the content margin for a provided placement.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](shortcutslink/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](shortcutslink/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [func contentShape<S>(S, eoFill: Bool) -> some View](shortcutslink/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](shortcutslink/contenttoolbar(for:content:)-5ero8.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](shortcutslink/contenttoolbar(for:content:)-6tr4t.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentTransition(ContentTransition) -> some View](shortcutslink/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](shortcutslink/contextmenu(_:).md)
  Adds a context menu to the view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](shortcutslink/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](shortcutslink/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](shortcutslink/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contrast(Double) -> some View](shortcutslink/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func controlGroupStyle<S>(S) -> some View](shortcutslink/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func controlSize(ControlSize) -> some View](shortcutslink/controlsize(_:)-2srh8.md)
  Sets the size for controls within this view.
- [func controlSize<T>(T) -> some View](shortcutslink/controlsize(_:)-jxy2.md)
  Limits the control size within the view to the given range.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](shortcutslink/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func coordinateSpace<T>(name: T) -> some View](shortcutslink/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](shortcutslink/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func datePickerStyle<S>(S) -> some View](shortcutslink/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](shortcutslink/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultAppStorage(UserDefaults) -> some View](shortcutslink/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](shortcutslink/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func defaultHoverEffect(HoverEffect?) -> some View](shortcutslink/defaulthovereffect(_:)-82imt.md)
  Sets the default hover effect to use for views within this view.
- [func defaultHoverEffect(some CustomHoverEffect) -> some View](shortcutslink/defaulthovereffect(_:)-rkad.md)
  Sets the default hover effect to use within this view hierarchy.
- [func defaultScrollAnchor(UnitPoint?) -> some View](shortcutslink/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](shortcutslink/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func defersSystemGestures(on: Edge.Set) -> some View](shortcutslink/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func deleteDisabled(Bool) -> some View](shortcutslink/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [func dialogIcon(Image?) -> some View](shortcutslink/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View](shortcutslink/dialogsuppressiontoggle(_:issuppressed:)-32772.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringResource, isSuppressed: Binding<Bool>) -> some View](shortcutslink/dialogsuppressiontoggle(_:issuppressed:)-3ct68.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>) -> some View](shortcutslink/dialogsuppressiontoggle(_:issuppressed:)-7nloy.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View](shortcutslink/dialogsuppressiontoggle(_:issuppressed:)-96cc4.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](shortcutslink/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func disableAutocorrection(Bool?) -> some View](shortcutslink/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func disabled(Bool) -> some View](shortcutslink/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func disclosureGroupStyle<S>(S) -> some View](shortcutslink/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](shortcutslink/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](shortcutslink/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func dragConfiguration(DragConfiguration) -> some View](shortcutslink/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, (ItemID) -> Data) -> some View](shortcutslink/dragcontainer(for:id:in:_:).md)
  A container with draggable views. The drag payload is based on the current selection.
- [func dragContainer<Item, ItemID>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> ItemID?, (ItemID) -> Item?) -> some View](shortcutslink/dragcontainer(for:id:in:selection:_:)-9jwhg.md)
  A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (consuming Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> Array<ItemID>, (Array<ItemID>) -> Data) -> some View](shortcutslink/dragcontainer(for:id:in:selection:_:)-s7ng.md)
  A container with multiple selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, (Item.ID) -> Data) -> some View](shortcutslink/dragcontainer(for:in:_:).md)
  A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Array<Item.ID>, (Array<Item.ID>) -> Data) -> some View](shortcutslink/dragcontainer(for:in:selection:_:)-99s7d.md)
  A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragContainer<Item>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Item.ID?, (Item.ID) -> Item?) -> some View](shortcutslink/dragcontainer(for:in:selection:_:)-9ys9u.md)
  A container with single item selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func draggable<T>(@autoclosure () -> T) -> some View](shortcutslink/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](shortcutslink/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<T, ID>(for: T.Type, id: ID, (ID) -> T?) -> some View](shortcutslink/draggable(for:id:_:).md)
  Activates this view as the source of a drag-and-drop operation.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](shortcutslink/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](shortcutslink/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](shortcutslink/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](shortcutslink/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dynamicTypeSize(DynamicTypeSize) -> some View](shortcutslink/dynamictypesize(_:)-3r6u6.md)
  Sets the Dynamic Type size within the view to the given value.
- [func dynamicTypeSize<T>(T) -> some View](shortcutslink/dynamictypesize(_:)-7xnnn.md)
  Limits the Dynamic Type size within the view to the given range.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](shortcutslink/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func environment<T>(T?) -> some View](shortcutslink/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](shortcutslink/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](shortcutslink/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](shortcutslink/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(Text?) -> some View](shortcutslink/filedialogconfirmationlabel(_:)-5act7.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringResource) -> some View](shortcutslink/filedialogconfirmationlabel(_:)-6ebrx.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringKey) -> some View](shortcutslink/filedialogconfirmationlabel(_:)-6mdrq.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel<S>(S) -> some View](shortcutslink/filedialogconfirmationlabel(_:)-7sc2z.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](shortcutslink/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](shortcutslink/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](shortcutslink/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(Text?) -> some View](shortcutslink/filedialogmessage(_:)-2sh0y.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogMessage<S>(S) -> some View](shortcutslink/filedialogmessage(_:)-8eir2.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringKey) -> some View](shortcutslink/filedialogmessage(_:)-98muc.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringResource) -> some View](shortcutslink/filedialogmessage(_:)-ozz3.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](shortcutslink/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](shortcutslink/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-4l7yk.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](shortcutslink/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-5aiwm.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-4xyn2.md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-6utak.md)
  Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](shortcutslink/fileexporter(ispresented:documents:contenttype:oncompletion:)-4inyk.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](shortcutslink/fileexporter(ispresented:documents:contenttype:oncompletion:)-8m68r.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-6urmh.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-99rsk.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(LocalizedStringKey) -> some View](shortcutslink/fileexporterfilenamelabel(_:)-27d72.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(Text?) -> some View](shortcutslink/fileexporterfilenamelabel(_:)-39eov.md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.
- [func fileExporterFilenameLabel(LocalizedStringResource) -> some View](shortcutslink/fileexporterfilenamelabel(_:)-7b9ka.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel<S>(S) -> some View](shortcutslink/fileexporterfilenamelabel(_:)-9kgi8.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](shortcutslink/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](shortcutslink/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](shortcutslink/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](shortcutslink/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](shortcutslink/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func findDisabled(Bool) -> some View](shortcutslink/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func findNavigator(isPresented: Binding<Bool>) -> some View](shortcutslink/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func fixedSize() -> some View](shortcutslink/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](shortcutslink/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](shortcutslink/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func focusEffectDisabled(Bool) -> some View](shortcutslink/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func focusable(Bool) -> some View](shortcutslink/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](shortcutslink/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focused(FocusState<Bool>.Binding) -> some View](shortcutslink/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](shortcutslink/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focusedObject<T>(T?) -> some View](shortcutslink/focusedobject(_:)-4daun.md)
  Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.
- [func focusedObject<T>(T) -> some View](shortcutslink/focusedobject(_:)-8wa6k.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedSceneObject<T>(T?) -> some View](shortcutslink/focusedsceneobject(_:)-137ih.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneObject<T>(T) -> some View](shortcutslink/focusedsceneobject(_:)-62y1b.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneValue<T>(T?) -> some View](shortcutslink/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some View](shortcutslink/focusedscenevalue(_:_:)-6e6bm.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some View](shortcutslink/focusedscenevalue(_:_:)-atdb.md)
  Creates a new view that exposes the provided value to other views whose state depends on the active scene.
- [func focusedValue<T>(T?) -> some View](shortcutslink/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) -> some View](shortcutslink/focusedvalue(_:_:)-2n168.md)
  Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) -> some View](shortcutslink/focusedvalue(_:_:)-6wuqk.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func font(Font?) -> some View](shortcutslink/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](shortcutslink/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](shortcutslink/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](shortcutslink/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func foregroundColor(Color?) -> some View](shortcutslink/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func foregroundStyle<S>(S) -> some View](shortcutslink/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](shortcutslink/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](shortcutslink/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func formStyle<S>(S) -> some View](shortcutslink/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func frame() -> some View](shortcutslink/frame.md)
  Positions this view within an invisible frame.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](shortcutslink/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](shortcutslink/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](shortcutslink/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](shortcutslink/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](shortcutslink/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](shortcutslink/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func gaugeStyle<S>(S) -> some View](shortcutslink/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func geometryGroup() -> some View](shortcutslink/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](shortcutslink/gesture(_:).md)
  Attaches a `UIGestureRecognizerRepresentable` to the view.
- [func gesture<T>(T, including: GestureMask) -> some View](shortcutslink/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](shortcutslink/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](shortcutslink/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](shortcutslink/glassbackgroundeffect(_:displaymode:).md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](shortcutslink/glassbackgroundeffect(_:in:displaymode:).md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](shortcutslink/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](shortcutslink/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](shortcutslink/glasseffect(_:in:isenabled:).md)
  Applies a glass effect to this view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](shortcutslink/glasseffectid(_:in:).md)
  Associates an identity value to glass effects defined within this view.
- [func glassEffectTransition(GlassEffectTransition, isEnabled: Bool) -> some View](shortcutslink/glasseffecttransition(_:isenabled:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](shortcutslink/glasseffectunion(id:namespace:).md)
  Associates any glass effects defined within this view to a union with the provided id.
- [func grayscale(Double) -> some View](shortcutslink/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func gridCellAnchor(UnitPoint) -> some View](shortcutslink/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellColumns(Int) -> some View](shortcutslink/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](shortcutslink/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](shortcutslink/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
- [func groupBoxStyle<S>(S) -> some View](shortcutslink/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](shortcutslink/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](shortcutslink/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](shortcutslink/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
- [func headerProminence(Prominence) -> some View](shortcutslink/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func help(LocalizedStringKey) -> some View](shortcutslink/help(_:)-3m9wt.md)
  Adds help text to a view using a localized string that you provide.
- [func help(LocalizedStringResource) -> some View](shortcutslink/help(_:)-677x6.md)
  Adds help text to a view using a localized string resource that you provide.
- [func help(Text) -> some View](shortcutslink/help(_:)-807cb.md)
  Adds help text to a view using a text view that you provide.
- [func help<S>(S) -> some View](shortcutslink/help(_:)-8u2lm.md)
  Adds help text to a view using a string that you provide.
- [func hidden() -> some View](shortcutslink/hidden.md)
  Hides this view unconditionally.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](shortcutslink/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](shortcutslink/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](shortcutslink/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func hoverEffect(HoverEffect) -> some View](shortcutslink/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](shortcutslink/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a `HoverEffectGroup`.
- [func hoverEffect(some CustomHoverEffect, isEnabled: Bool) -> some View](shortcutslink/hovereffect(_:isenabled:)-3l8m2.md)
  Applies a hover effect to this view, while providing a way to conditionally enable or disable it.
- [func hoverEffect(HoverEffect, isEnabled: Bool) -> some View](shortcutslink/hovereffect(_:isenabled:)-9g8bw.md)
  Applies a hover effect to this view.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](shortcutslink/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectDisabled(Bool) -> some View](shortcutslink/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func hoverEffectGroup() -> some View](shortcutslink/hovereffectgroup.md)
  Adds an implicit `HoverEffectGroup` to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](shortcutslink/hovereffectgroup(_:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](shortcutslink/hovereffectgroup(id:in:behavior:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hueRotation(Angle) -> some View](shortcutslink/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func id<ID>(ID) -> some View](shortcutslink/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](shortcutslink/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func imageScale(Image.Scale) -> some View](shortcutslink/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](shortcutslink/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.
- [func indexViewStyle<S>(S) -> some View](shortcutslink/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](shortcutslink/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](shortcutslink/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](shortcutslink/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
- [func interactionActivityTrackingTag(String) -> some View](shortcutslink/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func interactiveDismissDisabled(Bool) -> some View](shortcutslink/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func invalidatableContent(Bool) -> some View](shortcutslink/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
- [func italic(Bool) -> some View](shortcutslink/italic(_:).md)
  Applies italics to the text in this view.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](shortcutslink/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func kerning(CGFloat) -> some View](shortcutslink/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func keyboardShortcut(KeyboardShortcut?) -> some View](shortcutslink/keyboardshortcut(_:)-1sld.md)
  Assigns an optional keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyboardShortcut) -> some View](shortcutslink/keyboardshortcut(_:)-po3s.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](shortcutslink/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](shortcutslink/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardType(UIKeyboardType) -> some View](shortcutslink/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](shortcutslink/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](shortcutslink/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func labelIconToTitleSpacing(CGFloat) -> some View](shortcutslink/labelicontotitlespacing(_:).md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](shortcutslink/labelreservediconwidth(_:).md)
  Set the width reserved for icons in labels.
- [func labelStyle<S>(S) -> some View](shortcutslink/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func labeledContentStyle<S>(S) -> some View](shortcutslink/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsHidden() -> some View](shortcutslink/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](shortcutslink/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](shortcutslink/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](shortcutslink/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [func layoutPriority(Double) -> some View](shortcutslink/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](shortcutslink/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.
- [func lineHeight(AttributedString.LineHeight?) -> some View](shortcutslink/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func lineLimit(PartialRangeThrough<Int>) -> some View](shortcutslink/linelimit(_:)-4cfsc.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(ClosedRange<Int>) -> some View](shortcutslink/linelimit(_:)-4jmf9.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int?) -> some View](shortcutslink/linelimit(_:)-7ebhg.md)
  Sets the maximum number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeFrom<Int>) -> some View](shortcutslink/linelimit(_:)-7g99k.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](shortcutslink/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](shortcutslink/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func listItemTint(Color?) -> some View](shortcutslink/listitemtint(_:)-5n9fv.md)
  Sets a fixed tint color for content in a list.
- [func listItemTint(ListItemTint?) -> some View](shortcutslink/listitemtint(_:)-7glxq.md)
  Sets the tint effect for content in a list.
- [func listRowBackground<V>(V?) -> some View](shortcutslink/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func listRowHoverEffect(HoverEffect?) -> some View](shortcutslink/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](shortcutslink/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listRowInsets(EdgeInsets?) -> some View](shortcutslink/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](shortcutslink/listrowinsets(_:_:).md)
  Sets the insets of rows in a list on the specified edges.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](shortcutslink/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](shortcutslink/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSpacing(CGFloat?) -> some View](shortcutslink/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionIndexVisibility(Visibility) -> some View](shortcutslink/listsectionindexvisibility(_:).md)
  Changes the visibility of the list section index.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](shortcutslink/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](shortcutslink/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](shortcutslink/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSpacing(CGFloat) -> some View](shortcutslink/listsectionspacing(_:)-20vex.md)
  Sets the spacing between adjacent sections in a `List` to a custom value.
- [func listSectionSpacing(ListSectionSpacing) -> some View](shortcutslink/listsectionspacing(_:)-4agg7.md)
  Sets the spacing between adjacent sections in a `List`.
- [func listStyle<S>(S) -> some View](shortcutslink/liststyle(_:).md)
  Sets the style for lists within this view.
- [func luminanceToAlpha() -> some View](shortcutslink/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](shortcutslink/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](shortcutslink/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](shortcutslink/manipulable(using:).md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](shortcutslink/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
- [func mask<Mask>(Mask) -> some View](shortcutslink/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](shortcutslink/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](shortcutslink/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](shortcutslink/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](shortcutslink/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](shortcutslink/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](shortcutslink/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func menuIndicator(Visibility) -> some View](shortcutslink/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func menuOrder(MenuOrder) -> some View](shortcutslink/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuStyle<S>(S) -> some View](shortcutslink/menustyle(_:).md)
  Sets the style for menus within this view.
- [func minimumScaleFactor(CGFloat) -> some View](shortcutslink/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](shortcutslink/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [func monospaced(Bool) -> some View](shortcutslink/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](shortcutslink/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func moveDisabled(Bool) -> some View](shortcutslink/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func multilineTextAlignment(TextAlignment) -> some View](shortcutslink/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](shortcutslink/multilinetextalignment(strategy:).md)
  A modifier for the default text alignment strategy in the view hierarchy.
- [func navigationBarBackButtonHidden(Bool) -> some View](shortcutslink/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarHidden(Bool) -> some View](shortcutslink/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](shortcutslink/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](shortcutslink/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](shortcutslink/navigationbaritems(trailing:).md)
- [func navigationBarTitle<S>(S) -> some View](shortcutslink/navigationbartitle(_:)-1e70n.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey) -> some View](shortcutslink/navigationbartitle(_:)-7nncu.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](shortcutslink/navigationbartitle(_:)-7o2yr.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](shortcutslink/navigationbartitle(_:displaymode:)-58k2c.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](shortcutslink/navigationbartitle(_:displaymode:)-93ls3.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](shortcutslink/navigationbartitle(_:displaymode:)-9oqo6.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](shortcutslink/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](shortcutslink/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](shortcutslink/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](shortcutslink/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationDocument(URL) -> some View](shortcutslink/navigationdocument(_:)-14bum.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D) -> some View](shortcutslink/navigationdocument(_:)-9no2r.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some View](shortcutslink/navigationdocument(_:preview:)-4f45p.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some View](shortcutslink/navigationdocument(_:preview:)-7dya8.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some View](shortcutslink/navigationdocument(_:preview:)-88h4.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some View](shortcutslink/navigationdocument(_:preview:)-92z3x.md)
  Configures the view’s document for purposes of navigation.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](shortcutslink/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](shortcutslink/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](shortcutslink/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationSplitViewStyle<S>(S) -> some View](shortcutslink/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSubtitle(LocalizedStringKey) -> some View](shortcutslink/navigationsubtitle(_:)-1829l.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string.
- [func navigationSubtitle(Text) -> some View](shortcutslink/navigationsubtitle(_:)-4r25d.md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationSubtitle<S>(S) -> some View](shortcutslink/navigationsubtitle(_:)-7na9z.md)
  Configures the view’s subtitle for purposes of navigation, using a string.
- [func navigationSubtitle(LocalizedStringResource) -> some View](shortcutslink/navigationsubtitle(_:)-8q4tb.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [func navigationTitle<S>(S) -> some View](shortcutslink/navigationtitle(_:)-2acge.md)
  Configures the view’s title for purposes of navigation, using a string.
- [func navigationTitle(LocalizedStringKey) -> some View](shortcutslink/navigationtitle(_:)-4gj5y.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle(LocalizedStringResource) -> some View](shortcutslink/navigationtitle(_:)-7hn96.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationTitle(Binding<String>) -> some View](shortcutslink/navigationtitle(_:)-7s101.md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationTitle<V>(() -> V) -> some View](shortcutslink/navigationtitle(_:)-hbeh.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle(Text) -> some View](shortcutslink/navigationtitle(_:)-rylp.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTransition(some NavigationTransition) -> some View](shortcutslink/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func navigationViewStyle<S>(S) -> some View](shortcutslink/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func offset(CGSize) -> some View](shortcutslink/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](shortcutslink/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](shortcutslink/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](shortcutslink/onappintentexecution(_:perform:).md)
  Registers a handler to invoke in response to the specified app intent that your app receives.
- [func onAppear(perform: (() -> Void)?) -> some View](shortcutslink/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View](shortcutslink/onchange(of:initial:_:)-1e0we.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, initial: Bool, () -> Void) -> some View](shortcutslink/onchange(of:initial:_:)-7c77b.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](shortcutslink/onchange(of:perform:).md)
  Performs an action when a specified value changes.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](shortcutslink/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](shortcutslink/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onDisappear(perform: (() -> Void)?) -> some View](shortcutslink/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onDrag(() -> NSItemProvider) -> some View](shortcutslink/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](shortcutslink/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](shortcutslink/ondragsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](shortcutslink/ondrop(of:delegate:)-1avh7.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](shortcutslink/ondrop(of:delegate:)-fehu.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](shortcutslink/ondrop(of:istargeted:perform:)-1cxi1.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](shortcutslink/ondrop(of:istargeted:perform:)-236pu.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](shortcutslink/ondrop(of:istargeted:perform:)-7jjcb.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](shortcutslink/ondrop(of:istargeted:perform:)-9n9jj.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](shortcutslink/ondropsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T, T) -> Void) -> some View](shortcutslink/ongeometrychange(for:of:action:)-3naw6.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T) -> Void) -> some View](shortcutslink/ongeometrychange(for:of:action:)-84iqq.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T) -> Void) -> some View](shortcutslink/ongeometrychange3d(for:of:action:)-2oocu.md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T, T) -> Void) -> some View](shortcutslink/ongeometrychange3d(for:of:action:)-73eng.md)
  Returns a new view that arranges to call `action(oldValue, newValue)` whenever the value computed by `value(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onHover(perform: (Bool) -> Void) -> some View](shortcutslink/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](shortcutslink/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](shortcutslink/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](shortcutslink/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](shortcutslink/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](shortcutslink/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](shortcutslink/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](shortcutslink/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](shortcutslink/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](shortcutslink/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](shortcutslink/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onOpenURL(perform: (URL) -> ()) -> some View](shortcutslink/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onOpenURL(prefersInApp: Bool) -> some View](shortcutslink/onopenurl(prefersinapp:).md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](shortcutslink/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](shortcutslink/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](shortcutslink/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](shortcutslink/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](shortcutslink/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase, ScrollPhaseChangeContext) -> Void) -> some View](shortcutslink/onscrollphasechange(_:)-8bojk.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase) -> Void) -> some View](shortcutslink/onscrollphasechange(_:)-9umqa.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](shortcutslink/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](shortcutslink/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](shortcutslink/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](shortcutslink/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](shortcutslink/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](shortcutslink/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func onWorldRecenter(action: () -> Void) -> some View](shortcutslink/onworldrecenter(action:)-3kpw8.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func onWorldRecenter(action: (WorldRecenterPhase) -> Void) -> some View](shortcutslink/onworldrecenter(action:)-46mc4.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func opacity(Double) -> some View](shortcutslink/opacity(_:).md)
  Sets the transparency of this view.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () -> Content) -> some View](shortcutslink/ornament(visibility:attachmentanchor:contentalignment:ornament:)-6mhi9.md)
  Presents an ornament.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D, ornament: () -> Content) -> some View](shortcutslink/ornament(visibility:attachmentanchor:contentalignment:ornament:)-f1iv.md)
  Presents an ornament.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](shortcutslink/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](shortcutslink/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](shortcutslink/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](shortcutslink/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](shortcutslink/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](shortcutslink/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func padding(CGFloat) -> some View](shortcutslink/padding(_:)-48yxg.md)
  Adds a specific padding amount to each edge of this view.
- [func padding(EdgeInsets) -> some View](shortcutslink/padding(_:)-5ydfq.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](shortcutslink/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(CGFloat) -> some View](shortcutslink/padding3d(_:)-4xflc.md)
  Pads this view along all edge insets by the amount you specify.
- [func padding3D(EdgeInsets3D) -> some View](shortcutslink/padding3d(_:)-940i2.md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](shortcutslink/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](shortcutslink/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func persistentSystemOverlays(Visibility) -> some View](shortcutslink/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](shortcutslink/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](shortcutslink/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](shortcutslink/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func pickerStyle<S>(S) -> some View](shortcutslink/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func pointerStyle(PointerStyle?) -> some View](shortcutslink/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](shortcutslink/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](shortcutslink/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func position(CGPoint) -> some View](shortcutslink/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](shortcutslink/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func preference<K>(key: K.Type, value: K.Value) -> some View](shortcutslink/preference(key:value:).md)
  Sets a value for the given preference.
- [func preferredColorScheme(ColorScheme?) -> some View](shortcutslink/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](shortcutslink/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [func preferredWindowClippingMargins(Edge3D.Set, EdgeInsets3D) -> some View](shortcutslink/preferredwindowclippingmargins(_:_:)-5rzfi.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func preferredWindowClippingMargins(Edge3D.Set, CGFloat?) -> some View](shortcutslink/preferredwindowclippingmargins(_:_:)-ijji.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func presentationBackground<S>(S) -> some View](shortcutslink/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](shortcutslink/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](shortcutslink/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](shortcutslink/presentationbreakthrougheffect(_:).md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](shortcutslink/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](shortcutslink/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](shortcutslink/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](shortcutslink/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationDetents(Set<PresentationDetent>) -> some View](shortcutslink/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](shortcutslink/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](shortcutslink/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationSizing(some PresentationSizing) -> some View](shortcutslink/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func previewContext<C>(C) -> some View](shortcutslink/previewcontext(_:).md)
  Declares a context for the preview.
- [func previewDevice(PreviewDevice?) -> some View](shortcutslink/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](shortcutslink/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](shortcutslink/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewLayout(PreviewLayout) -> some View](shortcutslink/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func privacySensitive(Bool) -> some View](shortcutslink/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func progressViewStyle<S>(S) -> some View](shortcutslink/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func projectionEffect(ProjectionTransform) -> some View](shortcutslink/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func redacted(reason: RedactionReasons) -> some View](shortcutslink/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func refreshable(action: () async -> Void) -> some View](shortcutslink/refreshable(action:).md)
  Marks this view as refreshable.
- [func renameAction(FocusState<Bool>.Binding) -> some View](shortcutslink/renameaction(_:)-3tes8.md)
  Sets the rename action in the environment to update focus state.
- [func renameAction(() -> Void) -> some View](shortcutslink/renameaction(_:)-72t9.md)
  Sets a closure to run for the rename action.
- [func replaceDisabled(Bool) -> some View](shortcutslink/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](shortcutslink/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>](shortcutslink/rotation3deffect(_:axis:anchor:)-20vol.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> some View](shortcutslink/rotation3deffect(_:axis:anchor:)-3h1u6.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D) -> some View](shortcutslink/rotation3deffect(_:axis:anchor:)-7otsf.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](shortcutslink/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DLayout(Rotation3D) -> some View](shortcutslink/rotation3dlayout(_:).md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: RotationAxis3D) -> some View](shortcutslink/rotation3dlayout(_:axis:)-3q2kd.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat)) -> some View](shortcutslink/rotation3dlayout(_:axis:)-x1m1.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](shortcutslink/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](shortcutslink/safeareabar(edge:alignment:spacing:content:)-60y25.md)
  Renders the provided content appropriately to be displayed as a custom bar.
- [func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](shortcutslink/safeareabar(edge:alignment:spacing:content:)-9emp.md)
  Renders the provided content appropriate to be displayed as a custom bar.
- [func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> V) -> some View](shortcutslink/safeareainset(edge:alignment:spacing:content:)-75000.md)
  Shows the specified content above or below the modified view.
- [func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> V) -> some View](shortcutslink/safeareainset(edge:alignment:spacing:content:)-9g4qs.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(EdgeInsets) -> some View](shortcutslink/safeareapadding(_:)-246i2.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(CGFloat) -> some View](shortcutslink/safeareapadding(_:)-8p65q.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](shortcutslink/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func saturation(Double) -> some View](shortcutslink/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self, _UniformScaleEffect>](shortcutslink/scaleeffect(_:anchor:)-1jou8.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View](shortcutslink/scaleeffect(_:anchor:)-1xcxp.md)
  Scales this view uniformly by the specified size in each dimension, relative to an anchor point.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](shortcutslink/scaleeffect(_:anchor:)-1yzmo.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View](shortcutslink/scaleeffect(_:anchor:)-6t3ck.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> some View](shortcutslink/scaleeffect(_:anchor:)-k4jy.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](shortcutslink/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](shortcutslink/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func scaledToFill() -> some View](shortcutslink/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](shortcutslink/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](shortcutslink/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaledToFit3D() -> some View](shortcutslink/scaledtofit3d.md)
  Scales this view to fit its parent.
- [func scenePadding(Edge.Set) -> some View](shortcutslink/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](shortcutslink/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](shortcutslink/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollClipDisabled(Bool) -> some View](shortcutslink/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func scrollContentBackground(Visibility) -> some View](shortcutslink/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollDisabled(Bool) -> some View](shortcutslink/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](shortcutslink/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](shortcutslink/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](shortcutslink/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](shortcutslink/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](shortcutslink/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](shortcutslink/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](shortcutslink/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](shortcutslink/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](shortcutslink/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](shortcutslink/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](shortcutslink/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](shortcutslink/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](shortcutslink/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func searchCompletion(String) -> some View](shortcutslink/searchcompletion(_:)-5n903.md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchCompletion<T>(T) -> some View](shortcutslink/searchcompletion(_:)-6nwe9.md)
  Associates a search token with the value of this view when used as a search suggestion.
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](shortcutslink/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](shortcutslink/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](shortcutslink/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](shortcutslink/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](shortcutslink/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](shortcutslink/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchSuggestions<S>(() -> S) -> some View](shortcutslink/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](shortcutslink/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](shortcutslink/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:ispresented:placement:prompt:token:)-10wu3.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:ispresented:placement:prompt:token:)-1neod.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:ispresented:placement:prompt:token:)-4jcl9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:ispresented:placement:prompt:token:)-9es06.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:placement:prompt:token:)-2duxb.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:placement:prompt:token:)-3k0zl.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:placement:prompt:token:)-5d0yb.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](shortcutslink/searchable(text:editabletokens:placement:prompt:token:)-xf4n.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](shortcutslink/searchable(text:ispresented:placement:prompt:)-1dnc7.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](shortcutslink/searchable(text:ispresented:placement:prompt:)-62ebm.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S) -> some View](shortcutslink/searchable(text:ispresented:placement:prompt:)-8hj5.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?) -> some View](shortcutslink/searchable(text:ispresented:placement:prompt:)-9cf6.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](shortcutslink/searchable(text:placement:prompt:)-31st3.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](shortcutslink/searchable(text:placement:prompt:)-54j2m.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](shortcutslink/searchable(text:placement:prompt:)-7uayx.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](shortcutslink/searchable(text:placement:prompt:)-wu2x.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](shortcutslink/searchable(text:placement:prompt:suggestions:)-7h41d.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](shortcutslink/searchable(text:placement:prompt:suggestions:)-932nr.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](shortcutslink/searchable(text:placement:prompt:suggestions:)-rijc.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:ispresented:placement:prompt:token:)-1ev2h.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:ispresented:placement:prompt:token:)-44lnk.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:ispresented:placement:prompt:token:)-5kn7.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:ispresented:placement:prompt:token:)-xw71.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:placement:prompt:token:)-1nlm8.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:placement:prompt:token:)-2flqz.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:placement:prompt:token:)-36bu2.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:placement:prompt:token:)-85odk.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-1jw9n.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-3a5k0.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-6juq0.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-80mta.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-2gi76.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-3yglt.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-4v6zu.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](shortcutslink/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-59z0d.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func sectionActions<Content>(content: () -> Content) -> some View](shortcutslink/sectionactions(content:).md)
  Adds custom actions to a section.
- [func sectionIndexLabel<S>(S?) -> some View](shortcutslink/sectionindexlabel(_:)-5khqi.md)
  Sets the title that is used for the section index label pointing to this section, typically only a single character long.
- [func sectionIndexLabel(Text?) -> some View](shortcutslink/sectionindexlabel(_:)-8dqi3.md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
- [func selectionDisabled(Bool) -> some View](shortcutslink/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](shortcutslink/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](shortcutslink/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [func sensoryFeedback<T>(trigger: T, () -> SensoryFeedback?) -> some View](shortcutslink/sensoryfeedback(trigger:_:)-1uibv.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](shortcutslink/sensoryfeedback(trigger:_:)-8yoc0.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](shortcutslink/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](shortcutslink/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](shortcutslink/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](shortcutslink/shortcutslinkstyle(_:).md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](shortcutslink/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](shortcutslink/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](shortcutslink/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](shortcutslink/siritipviewstyle(_:).md)
  Sets the given style for SiriTipView within the view hierarchy
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](shortcutslink/spatialoverlay(alignment:content:).md)
  Adds secondary views within the 3D bounds of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](shortcutslink/spatialoverlaypreferencevalue(_:alignment:_:).md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
- [func speechAdjustedPitch(Double) -> some View](shortcutslink/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](shortcutslink/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](shortcutslink/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](shortcutslink/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](shortcutslink/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [func statusBar(hidden: Bool) -> some View](shortcutslink/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func statusBarHidden(Bool) -> some View](shortcutslink/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](shortcutslink/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func submitLabel(SubmitLabel) -> some View](shortcutslink/submitlabel(_:).md)
  Sets the submit label for this view.
- [func submitScope(Bool) -> some View](shortcutslink/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](shortcutslink/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](shortcutslink/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](shortcutslink/symbolcolorrenderingmode(_:).md)
  Sets the color rendering mode for symbol images.
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](shortcutslink/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](shortcutslink/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](shortcutslink/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](shortcutslink/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](shortcutslink/symbolvariablevaluemode(_:).md)
  Sets the variable value mode mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](shortcutslink/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](shortcutslink/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabItem<V>(() -> V) -> some View](shortcutslink/tabitem(_:).md)
  Sets the tab bar item associated with this view.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](shortcutslink/tabviewbottomaccessory(content:).md)
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](shortcutslink/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](shortcutslink/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](shortcutslink/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](shortcutslink/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewStyle<S>(S) -> some View](shortcutslink/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func tableColumnHeaders(Visibility) -> some View](shortcutslink/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func tableStyle<S>(S) -> some View](shortcutslink/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func tag<V>(V, includeOptional: Bool) -> some View](shortcutslink/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](shortcutslink/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](shortcutslink/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func textCase(Text.Case?) -> some View](shortcutslink/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textContentType(UITextContentType?) -> some View](shortcutslink/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textEditorStyle(some TextEditorStyle) -> some View](shortcutslink/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [func textFieldStyle<S>(S) -> some View](shortcutslink/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](shortcutslink/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](shortcutslink/textinputformattingcontrolvisibility(_:for:).md)
  Define which system text formatting controls are available.
- [func textRenderer<T>(T) -> some View](shortcutslink/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](shortcutslink/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textSelection<S>(S) -> some View](shortcutslink/textselection(_:).md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](shortcutslink/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tint(Color?) -> some View](shortcutslink/tint(_:).md)
  Sets the tint color within this view.
- [func toggleStyle<S>(S) -> some View](shortcutslink/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](shortcutslink/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar<Content>(content: () -> Content) -> some View](shortcutslink/toolbar(content:)-69fd.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(content: () -> Content) -> some View](shortcutslink/toolbar(content:)-9fw5h.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](shortcutslink/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](shortcutslink/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarbackground(_:for:)-18pda.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarbackground(_:for:)-6rm7m.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarRole(ToolbarRole) -> some View](shortcutslink/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](shortcutslink/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](shortcutslink/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](shortcutslink/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func tracking(CGFloat) -> some View](shortcutslink/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func transaction((inout Transaction) -> Void) -> some View](shortcutslink/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](shortcutslink/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](shortcutslink/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transform3DEffect(AffineTransform3D) -> some View](shortcutslink/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](shortcutslink/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformEffect(CGAffineTransform) -> some View](shortcutslink/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](shortcutslink/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](shortcutslink/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func transition<T>(T) -> some View](shortcutslink/transition(_:)-1tubp.md)
  Associates a transition with the view.
- [func transition(AnyTransition) -> some View](shortcutslink/transition(_:)-liit.md)
  Associates a transition with the view.
- [func truncationMode(Text.TruncationMode) -> some View](shortcutslink/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typeSelectEquivalent(LocalizedStringKey) -> some View](shortcutslink/typeselectequivalent(_:)-4sxmv.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(Text?) -> some View](shortcutslink/typeselectequivalent(_:)-70bjn.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringResource) -> some View](shortcutslink/typeselectequivalent(_:)-84yjd.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent<S>(S) -> some View](shortcutslink/typeselectequivalent(_:)-9yj03.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View](shortcutslink/typesettinglanguage(_:isenabled:)-3jeo9.md)
  Specifies the language for typesetting.
- [func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View](shortcutslink/typesettinglanguage(_:isenabled:)-6wwem.md)
  Specifies the language for typesetting.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](shortcutslink/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func unredacted() -> some View](shortcutslink/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func upperLimbVisibility(Visibility) -> some View](shortcutslink/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an `ImmersiveSpace` scene is presented.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](shortcutslink/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](shortcutslink/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](shortcutslink/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](shortcutslink/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [func volumeBaseplateVisibility(Visibility) -> some View](shortcutslink/volumebaseplatevisibility(_:).md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](shortcutslink/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](shortcutslink/writingdirection(strategy:).md)
  A modifier for the default text writing direction strategy in the view hierarchy.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](shortcutslink/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](shortcutslink/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [func zIndex(Double) -> some View](shortcutslink/zindex(_:).md)
  Controls the display order of overlapping views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/view-implementations)*