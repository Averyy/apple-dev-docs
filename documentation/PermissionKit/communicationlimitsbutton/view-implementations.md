# View Implementations

**Framework**: PermissionKit

## Topics

### Instance Methods
- [func accentColor(Color?) -> some View](communicationlimitsbutton/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(activationpoint:)-32gqp.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(activationpoint:)-3z7o.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](communicationlimitsbutton/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaction(named:_:)-5tjyh.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaction(named:_:)-6ycd4.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringResource, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaction(named:_:)-7nyf7.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaction(named:_:)-7xv9g.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](communicationlimitsbutton/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](communicationlimitsbutton/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityactivationpoint(_:)-51bev.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityactivationpoint(_:)-97mna.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityactivationpoint(_:isenabled:)-38zgv.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityactivationpoint(_:isenabled:)-rsok.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityChartDescriptor<R>(R) -> some View](communicationlimitsbutton/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [func accessibilityChildren<V>(children: () -> V) -> some View](communicationlimitsbutton/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityCustomContent<V>(LocalizedStringResource, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-3lqpg.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-3nfio.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-3st29.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-3unfd.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-4cuz2.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-56w2k.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-61gxv.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-6453j.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-8h6e2.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-8pddx.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-8xde1.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitycustomcontent(_:_:importance:)-9qhh.md)
  Add additional accessibility information to the view.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](communicationlimitsbutton/accessibilitydefaultfocus(_:_:).md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:)-6lzcj.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:)-7unte.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:)-8uhni.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:)-okh4.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:isenabled:)-3ujx.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:isenabled:)-5dhse.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:isenabled:)-6ryu3.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydragpoint(_:description:isenabled:)-fbxy.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:)-2j28a.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:)-436s4.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:)-5fl9f.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:)-6o1d7.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:isenabled:)-5korp.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:isenabled:)-69hwv.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:isenabled:)-9eqkh.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitydroppoint(_:description:isenabled:)-9ky0o.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](communicationlimitsbutton/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](communicationlimitsbutton/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](communicationlimitsbutton/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:)-25l3a.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:)-7a7dj.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:)-87zxy.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:)-9hty1.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:isenabled:)-1toqx.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:isenabled:)-6anws.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:isenabled:)-6s6bv.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityhint(_:isenabled:)-7ixj1.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIgnoresInvertColors(Bool) -> some View](communicationlimitsbutton/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:)-1om0h.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:)-3e6yz.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:)-69i03.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:isenabled:)-2p35m.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:isenabled:)-8jf46.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityinputlabels(_:isenabled:)-8wu32.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:)-2pfgt.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:)-6ramt.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:)-72h3r.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:)-9sr7m.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:isenabled:)-31cnb.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:isenabled:)-3tpdo.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:isenabled:)-49mj5.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitylabel(_:isenabled:)-6sbtg.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](communicationlimitsbutton/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](communicationlimitsbutton/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](communicationlimitsbutton/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](communicationlimitsbutton/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:)-1tac8.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:)-38roh.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringResource, entries: () -> Content) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:)-76a4e.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:)-7duqw.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:)-8hh8t.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entryid:entrylabel:)-24nyq.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entryid:entrylabel:)-33kfh.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entryid:entrylabel:)-6rph8.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringResource, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entryid:entrylabel:)-8cqwn.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entryid:entrylabel:)-9w8rp.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringResource, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entrylabel:)-57f9g.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entrylabel:)-5plut.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entrylabel:)-60yam.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entrylabel:)-8184o.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](communicationlimitsbutton/accessibilityrotor(_:entries:entrylabel:)-902kx.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](communicationlimitsbutton/accessibilityrotor(_:textranges:)-3ivsw.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](communicationlimitsbutton/accessibilityrotor(_:textranges:)-67es2.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringResource, textRanges: [Range<String.Index>]) -> some View](communicationlimitsbutton/accessibilityrotor(_:textranges:)-6a5v.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](communicationlimitsbutton/accessibilityrotor(_:textranges:)-7uzts.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](communicationlimitsbutton/accessibilityrotor(_:textranges:)-81u4.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](communicationlimitsbutton/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityscrollstatus(_:isenabled:)-2uxvg.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(some StringProtocol, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityscrollstatus(_:isenabled:)-702e7.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityscrollstatus(_:isenabled:)-87qxc.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityscrollstatus(_:isenabled:)-9au8f.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityShowsLargeContentViewer() -> some View](communicationlimitsbutton/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](communicationlimitsbutton/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:)-69vd0.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:)-9kmyd.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:)-lo83.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:)-v2a4.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:isenabled:)-1p7nh.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:isenabled:)-7ynea.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:isenabled:)-8t71h.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityvalue(_:isenabled:)-8x2kt.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](communicationlimitsbutton/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](communicationlimitsbutton/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](communicationlimitsbutton/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:)-18bj2.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:)-2wl0v.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<A>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:)-6scc8.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:)-7drcq.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:message:)-28v97.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:message:)-2n3k9.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:message:)-3debl.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:actions:message:)-3szxc.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:)-1wurm.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:)-3bxd7.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:)-4o8mw.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:)-6dldq.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:message:)-1d77o.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:message:)-3ou7g.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:message:)-4ogg7.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/alert(_:ispresented:presenting:actions:message:)-8y3rh.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](communicationlimitsbutton/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](communicationlimitsbutton/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](communicationlimitsbutton/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](communicationlimitsbutton/alert(item:content:).md)
  Presents an alert to the user.
- [func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](communicationlimitsbutton/alignmentguide(_:computevalue:)-6id8w.md)
  Sets the view’s horizontal alignment.
- [func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](communicationlimitsbutton/alignmentguide(_:computevalue:)-9kow9.md)
  Sets the view’s vertical alignment.
- [func alignmentGuide(DepthAlignment, computeValue: (ViewDimensions3D) -> CGFloat) -> some View](communicationlimitsbutton/alignmentguide(_:computevalue:)-9wqqw.md)
  Returns a view modified so that its value for the given `guide` is the result of passing the `ViewDimensions` of the underlying element to `computeValue`.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](communicationlimitsbutton/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
- [func allowsHitTesting(Bool) -> some View](communicationlimitsbutton/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func allowsTightening(Bool) -> some View](communicationlimitsbutton/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func allowsWindowActivationEvents() -> some View](communicationlimitsbutton/allowswindowactivationevents.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](communicationlimitsbutton/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](communicationlimitsbutton/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](communicationlimitsbutton/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func animation(Animation?) -> some View](communicationlimitsbutton/animation(_:).md)
  Applies the given animation to all animatable values within this view.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](communicationlimitsbutton/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation<V>(Animation?, value: V) -> some View](communicationlimitsbutton/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](communicationlimitsbutton/aspectratio(_:contentmode:)-1tkoj.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
- [func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View](communicationlimitsbutton/aspectratio(_:contentmode:)-hjp1.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](communicationlimitsbutton/aspectratio3d(_:contentmode:).md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.
- [func assistiveAccessNavigationIcon(Image) -> some View](communicationlimitsbutton/assistiveaccessnavigationicon(_:).md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](communicationlimitsbutton/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.
- [func attributedTextFormattingDefinition<S>(KeyPath<AttributeScopes, S.Type>) -> some View](communicationlimitsbutton/attributedtextformattingdefinition(_:)-7u2zx.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<D>(D) -> some View](communicationlimitsbutton/attributedtextformattingdefinition(_:)-82l9d.md)
  Apply a text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<S>(S.Type) -> some View](communicationlimitsbutton/attributedtextformattingdefinition(_:)-pk9k.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](communicationlimitsbutton/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func autocorrectionDisabled(Bool) -> some View](communicationlimitsbutton/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](communicationlimitsbutton/background(_:alignment:).md)
  Layers the given view behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](communicationlimitsbutton/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](communicationlimitsbutton/background(_:in:fillstyle:)-193ha.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](communicationlimitsbutton/background(_:in:fillstyle:)-59p96.md)
  Sets the view’s background to a shape filled with a style.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](communicationlimitsbutton/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](communicationlimitsbutton/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](communicationlimitsbutton/background(in:fillstyle:)-3l6us.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](communicationlimitsbutton/background(in:fillstyle:)-5n1g6.md)
  Sets the view’s background to a shape filled with the default background style.
- [func backgroundExtensionEffect() -> some View](communicationlimitsbutton/backgroundextensioneffect.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](communicationlimitsbutton/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](communicationlimitsbutton/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundStyle<S>(S) -> some View](communicationlimitsbutton/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func badge(Text?) -> some View](communicationlimitsbutton/badge(_:)-1kz7x.md)
  Generates a badge for the view from a text view.
- [func badge(LocalizedStringResource?) -> some View](communicationlimitsbutton/badge(_:)-5yiso.md)
  Generates a badge for the view from a localized string resource.
- [func badge(Int) -> some View](communicationlimitsbutton/badge(_:)-6ywz5.md)
  Generates a badge for the view from an integer value.
- [func badge(LocalizedStringKey?) -> some View](communicationlimitsbutton/badge(_:)-7wx9l.md)
  Generates a badge for the view from a localized string key.
- [func badge<S>(S?) -> some View](communicationlimitsbutton/badge(_:)-9lte7.md)
  Generates a badge for the view from a string.
- [func badgeProminence(BadgeProminence) -> some View](communicationlimitsbutton/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [func baselineOffset(CGFloat) -> some View](communicationlimitsbutton/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func blendMode(BlendMode) -> some View](communicationlimitsbutton/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func blur(radius: CGFloat, opaque: Bool) -> some View](communicationlimitsbutton/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func bold(Bool) -> some View](communicationlimitsbutton/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func border<S>(S, width: CGFloat) -> some View](communicationlimitsbutton/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func breakthroughEffect(BreakthroughEffect) -> some View](communicationlimitsbutton/breakthrougheffect(_:).md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [func brightness(Double) -> some View](communicationlimitsbutton/brightness(_:).md)
  Brightens this view by the specified amount.
- [func buttonBorderShape(ButtonBorderShape) -> some View](communicationlimitsbutton/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](communicationlimitsbutton/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func buttonSizing(ButtonSizing) -> some View](communicationlimitsbutton/buttonsizing(_:).md)
- [func buttonStyle<S>(S) -> some View](communicationlimitsbutton/buttonstyle(_:)-26os7.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func buttonStyle<S>(S) -> some View](communicationlimitsbutton/buttonstyle(_:)-9ovyi.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func clipShape<S>(S, style: FillStyle) -> some View](communicationlimitsbutton/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func clipped(antialiased: Bool) -> some View](communicationlimitsbutton/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func colorEffect(Shader, isEnabled: Bool) -> some View](communicationlimitsbutton/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func colorInvert() -> some View](communicationlimitsbutton/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](communicationlimitsbutton/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func colorScheme(ColorScheme) -> some View](communicationlimitsbutton/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func compositingGroup() -> some View](communicationlimitsbutton/compositinggroup.md)
  Wraps this view in a compositing group.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:)-2wfp4.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:)-2zadi.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:)-568z5.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:)-8rdlr.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-17gug.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-1syet.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-23kjr.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-6hcpo.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-1m1wo.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-5uibz.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-6h1qb.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-79f63.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-4wio6.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-5u1bj.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-7rugb.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](communicationlimitsbutton/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-8aesa.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](communicationlimitsbutton/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](communicationlimitsbutton/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](communicationlimitsbutton/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](communicationlimitsbutton/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](communicationlimitsbutton/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerShape<T>(T) -> some View](communicationlimitsbutton/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](communicationlimitsbutton/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentCaptureProtected(Bool) -> some View](communicationlimitsbutton/contentcaptureprotected(_:).md)
- [func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) -> some View](communicationlimitsbutton/contentmargins(_:_:for:)-4mqqu.md)
  Configures the content margin for a provided placement.
- [func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some View](communicationlimitsbutton/contentmargins(_:_:for:)-60b37.md)
  Configures the content margin for a provided placement.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](communicationlimitsbutton/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](communicationlimitsbutton/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [func contentShape<S>(S, eoFill: Bool) -> some View](communicationlimitsbutton/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](communicationlimitsbutton/contenttoolbar(for:content:)-7t3zk.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](communicationlimitsbutton/contenttoolbar(for:content:)-9lbpr.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentTransition(ContentTransition) -> some View](communicationlimitsbutton/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](communicationlimitsbutton/contextmenu(_:).md)
  Adds a context menu to the view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](communicationlimitsbutton/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](communicationlimitsbutton/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](communicationlimitsbutton/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contrast(Double) -> some View](communicationlimitsbutton/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func controlGroupStyle<S>(S) -> some View](communicationlimitsbutton/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func controlSize<T>(T) -> some View](communicationlimitsbutton/controlsize(_:)-69aig.md)
  Limits the control size within the view to the given range.
- [func controlSize(ControlSize) -> some View](communicationlimitsbutton/controlsize(_:)-9kmns.md)
  Sets the size for controls within this view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](communicationlimitsbutton/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func coordinateSpace<T>(name: T) -> some View](communicationlimitsbutton/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func copyable<T>(@autoclosure () -> [T]) -> some View](communicationlimitsbutton/copyable(_:).md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](communicationlimitsbutton/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](communicationlimitsbutton/cuttable(for:action:).md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func datePickerStyle<S>(S) -> some View](communicationlimitsbutton/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](communicationlimitsbutton/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultAppStorage(UserDefaults) -> some View](communicationlimitsbutton/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](communicationlimitsbutton/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func defaultHoverEffect(some CustomHoverEffect) -> some View](communicationlimitsbutton/defaulthovereffect(_:)-3pznj.md)
  Sets the default hover effect to use within this view hierarchy.
- [func defaultHoverEffect(HoverEffect?) -> some View](communicationlimitsbutton/defaulthovereffect(_:)-3ylms.md)
  Sets the default hover effect to use for views within this view.
- [func defaultScrollAnchor(UnitPoint?) -> some View](communicationlimitsbutton/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](communicationlimitsbutton/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func defersSystemGestures(on: Edge.Set) -> some View](communicationlimitsbutton/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func deleteDisabled(Bool) -> some View](communicationlimitsbutton/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [func dialogIcon(Image?) -> some View](communicationlimitsbutton/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogPreventsAppTermination(Bool?) -> some View](communicationlimitsbutton/dialogpreventsapptermination(_:).md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
- [func dialogSeverity(DialogSeverity) -> some View](communicationlimitsbutton/dialogseverity(_:).md)
- [func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View](communicationlimitsbutton/dialogsuppressiontoggle(_:issuppressed:)-2t4ov.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View](communicationlimitsbutton/dialogsuppressiontoggle(_:issuppressed:)-77i0f.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>) -> some View](communicationlimitsbutton/dialogsuppressiontoggle(_:issuppressed:)-86t26.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringResource, isSuppressed: Binding<Bool>) -> some View](communicationlimitsbutton/dialogsuppressiontoggle(_:issuppressed:)-95qdl.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](communicationlimitsbutton/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func disableAutocorrection(Bool?) -> some View](communicationlimitsbutton/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func disabled(Bool) -> some View](communicationlimitsbutton/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func disclosureGroupStyle<S>(S) -> some View](communicationlimitsbutton/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [func dismissalConfirmationDialog<A>(LocalizedStringResource, shouldPresent: Bool, actions: () -> A) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:)-1dmf.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<S, A>(S, shouldPresent: Bool, actions: () -> A) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:)-1ixhd.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(Text, shouldPresent: Bool, actions: () -> A) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:)-8xmsn.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:)-fayw.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(LocalizedStringResource, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-13xme.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-2taa8.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(Text, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-7hgm9.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<S, A, M>(S, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](communicationlimitsbutton/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-e4wj.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](communicationlimitsbutton/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](communicationlimitsbutton/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func dragConfiguration(DragConfiguration) -> some View](communicationlimitsbutton/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, (ItemID) -> Data) -> some View](communicationlimitsbutton/dragcontainer(for:id:in:_:).md)
  A container with draggable views. The drag payload is based on the current selection.
- [func dragContainer<Item, ItemID>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> ItemID?, (ItemID) -> Item?) -> some View](communicationlimitsbutton/dragcontainer(for:id:in:selection:_:)-2orct.md)
  A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (consuming Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> Array<ItemID>, (Array<ItemID>) -> Data) -> some View](communicationlimitsbutton/dragcontainer(for:id:in:selection:_:)-9hcjw.md)
  A container with multiple selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, (Item.ID) -> Data) -> some View](communicationlimitsbutton/dragcontainer(for:in:_:).md)
  A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.
- [func dragContainer<Item>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Item.ID?, (Item.ID) -> Item?) -> some View](communicationlimitsbutton/dragcontainer(for:in:selection:_:)-4oayu.md)
  A container with single item selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Array<Item.ID>, (Array<Item.ID>) -> Data) -> some View](communicationlimitsbutton/dragcontainer(for:in:selection:_:)-9xtxb.md)
  A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](communicationlimitsbutton/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func draggable<T>(@autoclosure () -> T) -> some View](communicationlimitsbutton/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<Item>(Item.Type, @autoclosure () -> Item?) -> some View](communicationlimitsbutton/draggable(_:_:).md)
  Activates this view as the source of a drag and drop operation. A view can be dragged separately, or as an element of a drag container.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](communicationlimitsbutton/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<ItemID>(containerItemID: ItemID) -> some View](communicationlimitsbutton/draggable(containeritemid:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [func draggable<T, ID>(for: T.Type, id: ID, (ID) -> T?) -> some View](communicationlimitsbutton/draggable(for:id:_:).md)
  Activates this view as the source of a drag-and-drop operation.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](communicationlimitsbutton/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](communicationlimitsbutton/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](communicationlimitsbutton/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](communicationlimitsbutton/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](communicationlimitsbutton/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.
- [func dynamicTypeSize(DynamicTypeSize) -> some View](communicationlimitsbutton/dynamictypesize(_:)-6las0.md)
  Sets the Dynamic Type size within the view to the given value.
- [func dynamicTypeSize<T>(T) -> some View](communicationlimitsbutton/dynamictypesize(_:)-z15u.md)
  Limits the Dynamic Type size within the view to the given range.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](communicationlimitsbutton/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func environment<T>(T?) -> some View](communicationlimitsbutton/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](communicationlimitsbutton/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](communicationlimitsbutton/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](communicationlimitsbutton/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](communicationlimitsbutton/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](communicationlimitsbutton/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](communicationlimitsbutton/exportsitemproviders(_:onexport:onedit:).md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](communicationlimitsbutton/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel<S>(S) -> some View](communicationlimitsbutton/filedialogconfirmationlabel(_:)-1s4d3.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(Text?) -> some View](communicationlimitsbutton/filedialogconfirmationlabel(_:)-8xnx1.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringResource) -> some View](communicationlimitsbutton/filedialogconfirmationlabel(_:)-9220d.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringKey) -> some View](communicationlimitsbutton/filedialogconfirmationlabel(_:)-9xixl.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](communicationlimitsbutton/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](communicationlimitsbutton/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](communicationlimitsbutton/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(LocalizedStringKey) -> some View](communicationlimitsbutton/filedialogmessage(_:)-1tsle.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(Text?) -> some View](communicationlimitsbutton/filedialogmessage(_:)-6shr7.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogMessage<S>(S) -> some View](communicationlimitsbutton/filedialogmessage(_:)-6u7bp.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringResource) -> some View](communicationlimitsbutton/filedialogmessage(_:)-7580h.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](communicationlimitsbutton/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-2degw.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-892wr.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-19ovk.md)
  Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-6qdwk.md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:documents:contenttype:oncompletion:)-3gsrd.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:documents:contenttype:oncompletion:)-6c7j.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-5prpf.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-7uts5.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(LocalizedStringKey) -> some View](communicationlimitsbutton/fileexporterfilenamelabel(_:)-3p2i5.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel<S>(S) -> some View](communicationlimitsbutton/fileexporterfilenamelabel(_:)-5n6e6.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(Text?) -> some View](communicationlimitsbutton/fileexporterfilenamelabel(_:)-5omet.md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.
- [func fileExporterFilenameLabel(LocalizedStringResource) -> some View](communicationlimitsbutton/fileexporterfilenamelabel(_:)-9fn75.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](communicationlimitsbutton/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](communicationlimitsbutton/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](communicationlimitsbutton/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](communicationlimitsbutton/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](communicationlimitsbutton/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func findDisabled(Bool) -> some View](communicationlimitsbutton/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func findNavigator(isPresented: Binding<Bool>) -> some View](communicationlimitsbutton/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func fixedSize() -> some View](communicationlimitsbutton/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](communicationlimitsbutton/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](communicationlimitsbutton/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func focusEffectDisabled(Bool) -> some View](communicationlimitsbutton/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func focusScope(Namespace.ID) -> some View](communicationlimitsbutton/focusscope(_:).md)
  Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [func focusSection() -> some View](communicationlimitsbutton/focussection.md)
  Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [func focusable(Bool) -> some View](communicationlimitsbutton/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](communicationlimitsbutton/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](communicationlimitsbutton/focusable(_:onfocuschange:).md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func focused(FocusState<Bool>.Binding) -> some View](communicationlimitsbutton/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](communicationlimitsbutton/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focusedObject<T>(T) -> some View](communicationlimitsbutton/focusedobject(_:)-346av.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedObject<T>(T?) -> some View](communicationlimitsbutton/focusedobject(_:)-6c97t.md)
  Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.
- [func focusedSceneObject<T>(T) -> some View](communicationlimitsbutton/focusedsceneobject(_:)-3sz3u.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneObject<T>(T?) -> some View](communicationlimitsbutton/focusedsceneobject(_:)-5ajpt.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneValue<T>(T?) -> some View](communicationlimitsbutton/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some View](communicationlimitsbutton/focusedscenevalue(_:_:)-1w61b.md)
  Creates a new view that exposes the provided value to other views whose state depends on the active scene.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some View](communicationlimitsbutton/focusedscenevalue(_:_:)-qc4z.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedValue<T>(T?) -> some View](communicationlimitsbutton/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) -> some View](communicationlimitsbutton/focusedvalue(_:_:)-6sa4l.md)
  Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) -> some View](communicationlimitsbutton/focusedvalue(_:_:)-7e11j.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func font(Font?) -> some View](communicationlimitsbutton/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](communicationlimitsbutton/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](communicationlimitsbutton/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](communicationlimitsbutton/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func foregroundColor(Color?) -> some View](communicationlimitsbutton/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func foregroundStyle<S>(S) -> some View](communicationlimitsbutton/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](communicationlimitsbutton/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](communicationlimitsbutton/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func formStyle<S>(S) -> some View](communicationlimitsbutton/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func frame() -> some View](communicationlimitsbutton/frame.md)
  Positions this view within an invisible frame.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](communicationlimitsbutton/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](communicationlimitsbutton/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](communicationlimitsbutton/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](communicationlimitsbutton/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](communicationlimitsbutton/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](communicationlimitsbutton/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func gaugeStyle<S>(S) -> some View](communicationlimitsbutton/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func geometryGroup() -> some View](communicationlimitsbutton/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](communicationlimitsbutton/gesture(_:)-13hwr.md)
  Attaches a `UIGestureRecognizerRepresentable` to the view.
- [func gesture(some NSGestureRecognizerRepresentable) -> some View](communicationlimitsbutton/gesture(_:)-8uygw.md)
  Attaches an `NSGestureRecognizerRepresentable` to the view.
- [func gesture<T>(T, including: GestureMask) -> some View](communicationlimitsbutton/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](communicationlimitsbutton/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](communicationlimitsbutton/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](communicationlimitsbutton/glassbackgroundeffect(_:displaymode:).md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](communicationlimitsbutton/glassbackgroundeffect(_:in:displaymode:).md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](communicationlimitsbutton/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](communicationlimitsbutton/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](communicationlimitsbutton/glasseffect(_:in:isenabled:).md)
  Applies a glass effect to this view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](communicationlimitsbutton/glasseffectid(_:in:).md)
  Associates an identity value to glass effects defined within this view.
- [func glassEffectTransition(GlassEffectTransition, isEnabled: Bool) -> some View](communicationlimitsbutton/glasseffecttransition(_:isenabled:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](communicationlimitsbutton/glasseffectunion(id:namespace:).md)
  Associates any glass effects defined within this view to a union with the provided id.
- [func grayscale(Double) -> some View](communicationlimitsbutton/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func gridCellAnchor(UnitPoint) -> some View](communicationlimitsbutton/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellColumns(Int) -> some View](communicationlimitsbutton/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](communicationlimitsbutton/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](communicationlimitsbutton/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
- [func groupBoxStyle<S>(S) -> some View](communicationlimitsbutton/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](communicationlimitsbutton/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](communicationlimitsbutton/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](communicationlimitsbutton/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
- [func headerProminence(Prominence) -> some View](communicationlimitsbutton/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func help<S>(S) -> some View](communicationlimitsbutton/help(_:)-5smfs.md)
  Adds help text to a view using a string that you provide.
- [func help(LocalizedStringKey) -> some View](communicationlimitsbutton/help(_:)-7cyn8.md)
  Adds help text to a view using a localized string that you provide.
- [func help(LocalizedStringResource) -> some View](communicationlimitsbutton/help(_:)-8l1ld.md)
  Adds help text to a view using a localized string resource that you provide.
- [func help(Text) -> some View](communicationlimitsbutton/help(_:)-9aogu.md)
  Adds help text to a view using a text view that you provide.
- [func hidden() -> some View](communicationlimitsbutton/hidden.md)
  Hides this view unconditionally.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](communicationlimitsbutton/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](communicationlimitsbutton/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](communicationlimitsbutton/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func horizontalRadioGroupLayout() -> some View](communicationlimitsbutton/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func hoverEffect(HoverEffect) -> some View](communicationlimitsbutton/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](communicationlimitsbutton/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a `HoverEffectGroup`.
- [func hoverEffect(HoverEffect, isEnabled: Bool) -> some View](communicationlimitsbutton/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](communicationlimitsbutton/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectDisabled(Bool) -> some View](communicationlimitsbutton/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func hoverEffectGroup() -> some View](communicationlimitsbutton/hovereffectgroup.md)
  Adds an implicit `HoverEffectGroup` to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](communicationlimitsbutton/hovereffectgroup(_:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](communicationlimitsbutton/hovereffectgroup(id:in:behavior:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hueRotation(Angle) -> some View](communicationlimitsbutton/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func id<ID>(ID) -> some View](communicationlimitsbutton/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](communicationlimitsbutton/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func imageScale(Image.Scale) -> some View](communicationlimitsbutton/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](communicationlimitsbutton/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](communicationlimitsbutton/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](communicationlimitsbutton/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func indexViewStyle<S>(S) -> some View](communicationlimitsbutton/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](communicationlimitsbutton/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](communicationlimitsbutton/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](communicationlimitsbutton/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
- [func interactionActivityTrackingTag(String) -> some View](communicationlimitsbutton/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func interactiveDismissDisabled(Bool) -> some View](communicationlimitsbutton/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func invalidatableContent(Bool) -> some View](communicationlimitsbutton/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
- [func italic(Bool) -> some View](communicationlimitsbutton/italic(_:).md)
  Applies italics to the text in this view.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](communicationlimitsbutton/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func kerning(CGFloat) -> some View](communicationlimitsbutton/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func keyboardShortcut(KeyboardShortcut) -> some View](communicationlimitsbutton/keyboardshortcut(_:)-89s5j.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyboardShortcut?) -> some View](communicationlimitsbutton/keyboardshortcut(_:)-9z25v.md)
  Assigns an optional keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](communicationlimitsbutton/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](communicationlimitsbutton/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardType(UIKeyboardType) -> some View](communicationlimitsbutton/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](communicationlimitsbutton/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](communicationlimitsbutton/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func labelIconToTitleSpacing(CGFloat) -> some View](communicationlimitsbutton/labelicontotitlespacing(_:).md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](communicationlimitsbutton/labelreservediconwidth(_:).md)
  Set the width reserved for icons in labels.
- [func labelStyle<S>(S) -> some View](communicationlimitsbutton/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func labeledContentStyle<S>(S) -> some View](communicationlimitsbutton/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsHidden() -> some View](communicationlimitsbutton/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](communicationlimitsbutton/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](communicationlimitsbutton/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](communicationlimitsbutton/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [func layoutPriority(Double) -> some View](communicationlimitsbutton/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](communicationlimitsbutton/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.
- [func lineHeight(AttributedString.LineHeight?) -> some View](communicationlimitsbutton/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func lineLimit(ClosedRange<Int>) -> some View](communicationlimitsbutton/linelimit(_:)-3a78l.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeFrom<Int>) -> some View](communicationlimitsbutton/linelimit(_:)-5tiuo.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeThrough<Int>) -> some View](communicationlimitsbutton/linelimit(_:)-6a6sk.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(Int?) -> some View](communicationlimitsbutton/linelimit(_:)-8575u.md)
  Sets the maximum number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](communicationlimitsbutton/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](communicationlimitsbutton/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func listItemTint(ListItemTint?) -> some View](communicationlimitsbutton/listitemtint(_:)-19155.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](communicationlimitsbutton/listitemtint(_:)-4j1u9.md)
  Sets a fixed tint color for content in a list.
- [func listRowBackground<V>(V?) -> some View](communicationlimitsbutton/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func listRowHoverEffect(HoverEffect?) -> some View](communicationlimitsbutton/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](communicationlimitsbutton/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listRowInsets(EdgeInsets?) -> some View](communicationlimitsbutton/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](communicationlimitsbutton/listrowinsets(_:_:).md)
  Sets the insets of rows in a list on the specified edges.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](communicationlimitsbutton/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](communicationlimitsbutton/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSpacing(CGFloat?) -> some View](communicationlimitsbutton/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionIndexVisibility(Visibility) -> some View](communicationlimitsbutton/listsectionindexvisibility(_:).md)
  Changes the visibility of the list section index.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](communicationlimitsbutton/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](communicationlimitsbutton/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](communicationlimitsbutton/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSpacing(CGFloat) -> some View](communicationlimitsbutton/listsectionspacing(_:)-1sh4h.md)
  Sets the spacing between adjacent sections in a `List` to a custom value.
- [func listSectionSpacing(ListSectionSpacing) -> some View](communicationlimitsbutton/listsectionspacing(_:)-4dmna.md)
  Sets the spacing between adjacent sections in a `List`.
- [func listStyle<S>(S) -> some View](communicationlimitsbutton/liststyle(_:).md)
  Sets the style for lists within this view.
- [func luminanceToAlpha() -> some View](communicationlimitsbutton/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](communicationlimitsbutton/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](communicationlimitsbutton/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](communicationlimitsbutton/manipulable(using:).md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](communicationlimitsbutton/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
- [func mask<Mask>(Mask) -> some View](communicationlimitsbutton/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](communicationlimitsbutton/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](communicationlimitsbutton/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](communicationlimitsbutton/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](communicationlimitsbutton/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](communicationlimitsbutton/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](communicationlimitsbutton/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func menuButtonStyle<S>(S) -> some View](communicationlimitsbutton/menubuttonstyle(_:).md)
  Sets the style for menu buttons within this view.
- [func menuIndicator(Visibility) -> some View](communicationlimitsbutton/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func menuOrder(MenuOrder) -> some View](communicationlimitsbutton/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuStyle<S>(S) -> some View](communicationlimitsbutton/menustyle(_:).md)
  Sets the style for menus within this view.
- [func minimumScaleFactor(CGFloat) -> some View](communicationlimitsbutton/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](communicationlimitsbutton/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](communicationlimitsbutton/modifierkeyalternate(_:_:).md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
- [func monospaced(Bool) -> some View](communicationlimitsbutton/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](communicationlimitsbutton/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func moveDisabled(Bool) -> some View](communicationlimitsbutton/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func multilineTextAlignment(TextAlignment) -> some View](communicationlimitsbutton/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](communicationlimitsbutton/multilinetextalignment(strategy:).md)
  A modifier for the default text alignment strategy in the view hierarchy.
- [func navigationBarBackButtonHidden(Bool) -> some View](communicationlimitsbutton/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarHidden(Bool) -> some View](communicationlimitsbutton/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](communicationlimitsbutton/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](communicationlimitsbutton/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](communicationlimitsbutton/navigationbaritems(trailing:).md)
- [func navigationBarTitle(LocalizedStringKey) -> some View](communicationlimitsbutton/navigationbartitle(_:)-17o3w.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](communicationlimitsbutton/navigationbartitle(_:)-1kl9i.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle<S>(S) -> some View](communicationlimitsbutton/navigationbartitle(_:)-3l2xc.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](communicationlimitsbutton/navigationbartitle(_:displaymode:)-2gvi3.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](communicationlimitsbutton/navigationbartitle(_:displaymode:)-3d2de.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](communicationlimitsbutton/navigationbartitle(_:displaymode:)-8nst6.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](communicationlimitsbutton/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](communicationlimitsbutton/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](communicationlimitsbutton/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](communicationlimitsbutton/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationDocument(URL) -> some View](communicationlimitsbutton/navigationdocument(_:)-99x1x.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D) -> some View](communicationlimitsbutton/navigationdocument(_:)-9ie3u.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some View](communicationlimitsbutton/navigationdocument(_:preview:)-21xff.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some View](communicationlimitsbutton/navigationdocument(_:preview:)-6mo99.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some View](communicationlimitsbutton/navigationdocument(_:preview:)-896v6.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some View](communicationlimitsbutton/navigationdocument(_:preview:)-o06z.md)
  Configures the view’s document for purposes of navigation.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](communicationlimitsbutton/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](communicationlimitsbutton/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](communicationlimitsbutton/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationSplitViewStyle<S>(S) -> some View](communicationlimitsbutton/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSubtitle(LocalizedStringKey) -> some View](communicationlimitsbutton/navigationsubtitle(_:)-40pvy.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string.
- [func navigationSubtitle<S>(S) -> some View](communicationlimitsbutton/navigationsubtitle(_:)-672x8.md)
  Configures the view’s subtitle for purposes of navigation, using a string.
- [func navigationSubtitle(Text) -> some View](communicationlimitsbutton/navigationsubtitle(_:)-8mgh2.md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationSubtitle(LocalizedStringResource) -> some View](communicationlimitsbutton/navigationsubtitle(_:)-9rd2q.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [func navigationTitle<V>(() -> V) -> some View](communicationlimitsbutton/navigationtitle(_:)-18nut.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle(LocalizedStringResource) -> some View](communicationlimitsbutton/navigationtitle(_:)-2c24l.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationTitle<S>(S) -> some View](communicationlimitsbutton/navigationtitle(_:)-5h4w0.md)
  Configures the view’s title for purposes of navigation, using a string.
- [func navigationTitle(Text) -> some View](communicationlimitsbutton/navigationtitle(_:)-7vvlz.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTitle(LocalizedStringKey) -> some View](communicationlimitsbutton/navigationtitle(_:)-7z2wy.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle(Binding<String>) -> some View](communicationlimitsbutton/navigationtitle(_:)-fhka.md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationTransition(some NavigationTransition) -> some View](communicationlimitsbutton/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func navigationViewStyle<S>(S) -> some View](communicationlimitsbutton/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func offset(CGSize) -> some View](communicationlimitsbutton/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](communicationlimitsbutton/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](communicationlimitsbutton/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
- [func onAppear(perform: (() -> Void)?) -> some View](communicationlimitsbutton/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View](communicationlimitsbutton/onchange(of:initial:_:)-4w9ul.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, initial: Bool, () -> Void) -> some View](communicationlimitsbutton/onchange(of:initial:_:)-5oh12.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](communicationlimitsbutton/onchange(of:perform:).md)
  Performs an action when a specified value changes.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](communicationlimitsbutton/oncommand(_:perform:).md)
  Adds an action to perform in response to the given selector.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](communicationlimitsbutton/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](communicationlimitsbutton/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](communicationlimitsbutton/oncopycommand(perform:).md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](communicationlimitsbutton/oncutcommand(perform:).md)
  Adds an action to perform in response to the system’s Cut command.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](communicationlimitsbutton/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func onDisappear(perform: (() -> Void)?) -> some View](communicationlimitsbutton/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onDrag(() -> NSItemProvider) -> some View](communicationlimitsbutton/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](communicationlimitsbutton/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](communicationlimitsbutton/ondragsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](communicationlimitsbutton/ondrop(of:delegate:)-4lx45.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](communicationlimitsbutton/ondrop(of:delegate:)-9t0rx.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](communicationlimitsbutton/ondrop(of:istargeted:perform:)-1gbdd.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](communicationlimitsbutton/ondrop(of:istargeted:perform:)-2wqed.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](communicationlimitsbutton/ondrop(of:istargeted:perform:)-6rr55.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](communicationlimitsbutton/ondrop(of:istargeted:perform:)-73wet.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](communicationlimitsbutton/ondropsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func onExitCommand(perform: (() -> Void)?) -> some View](communicationlimitsbutton/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T) -> Void) -> some View](communicationlimitsbutton/ongeometrychange(for:of:action:)-4gyg7.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T, T) -> Void) -> some View](communicationlimitsbutton/ongeometrychange(for:of:action:)-5umxe.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T, T) -> Void) -> some View](communicationlimitsbutton/ongeometrychange3d(for:of:action:)-27mqk.md)
  Returns a new view that arranges to call `action(oldValue, newValue)` whenever the value computed by `value(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T) -> Void) -> some View](communicationlimitsbutton/ongeometrychange3d(for:of:action:)-7o33q.md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onHover(perform: (Bool) -> Void) -> some View](communicationlimitsbutton/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](communicationlimitsbutton/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](communicationlimitsbutton/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](communicationlimitsbutton/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](communicationlimitsbutton/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](communicationlimitsbutton/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](communicationlimitsbutton/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](communicationlimitsbutton/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](communicationlimitsbutton/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](communicationlimitsbutton/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](communicationlimitsbutton/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](communicationlimitsbutton/onmodifierkeyschanged(mask:initial:_:).md)
  Performs an action whenever the user presses or releases a hardware modifier key.
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](communicationlimitsbutton/onmovecommand(perform:).md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onOpenURL(perform: (URL) -> ()) -> some View](communicationlimitsbutton/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onOpenURL(prefersInApp: Bool) -> some View](communicationlimitsbutton/onopenurl(prefersinapp:).md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](communicationlimitsbutton/onpastecommand(of:perform:)-57zh1.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) -> some View](communicationlimitsbutton/onpastecommand(of:perform:)-7m2rg.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](communicationlimitsbutton/onpastecommand(of:validator:perform:)-16mh6.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](communicationlimitsbutton/onpastecommand(of:validator:perform:)-5zunh.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](communicationlimitsbutton/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](communicationlimitsbutton/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](communicationlimitsbutton/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](communicationlimitsbutton/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](communicationlimitsbutton/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](communicationlimitsbutton/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase, ScrollPhaseChangeContext) -> Void) -> some View](communicationlimitsbutton/onscrollphasechange(_:)-7ky15.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase) -> Void) -> some View](communicationlimitsbutton/onscrollphasechange(_:)-ts8e.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](communicationlimitsbutton/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](communicationlimitsbutton/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](communicationlimitsbutton/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](communicationlimitsbutton/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](communicationlimitsbutton/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](communicationlimitsbutton/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func onWorldRecenter(action: () -> Void) -> some View](communicationlimitsbutton/onworldrecenter(action:)-7z869.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func onWorldRecenter(action: (WorldRecenterPhase) -> Void) -> some View](communicationlimitsbutton/onworldrecenter(action:)-89zju.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func opacity(Double) -> some View](communicationlimitsbutton/opacity(_:).md)
  Sets the transparency of this view.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () -> Content) -> some View](communicationlimitsbutton/ornament(visibility:attachmentanchor:contentalignment:ornament:)-8alcp.md)
  Presents an ornament.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D, ornament: () -> Content) -> some View](communicationlimitsbutton/ornament(visibility:attachmentanchor:contentalignment:ornament:)-8qfv6.md)
  Presents an ornament.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](communicationlimitsbutton/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](communicationlimitsbutton/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](communicationlimitsbutton/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](communicationlimitsbutton/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](communicationlimitsbutton/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](communicationlimitsbutton/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func padding(CGFloat) -> some View](communicationlimitsbutton/padding(_:)-3xcm6.md)
  Adds a specific padding amount to each edge of this view.
- [func padding(EdgeInsets) -> some View](communicationlimitsbutton/padding(_:)-7yfqh.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](communicationlimitsbutton/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(EdgeInsets3D) -> some View](communicationlimitsbutton/padding3d(_:)-4pei3.md)
  Pads this view using the edge insets you specify.
- [func padding3D(CGFloat) -> some View](communicationlimitsbutton/padding3d(_:)-4rxuz.md)
  Pads this view along all edge insets by the amount you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](communicationlimitsbutton/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](communicationlimitsbutton/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](communicationlimitsbutton/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](communicationlimitsbutton/pastedestination(for:action:validator:).md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [func persistentSystemOverlays(Visibility) -> some View](communicationlimitsbutton/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](communicationlimitsbutton/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](communicationlimitsbutton/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](communicationlimitsbutton/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func pickerStyle<S>(S) -> some View](communicationlimitsbutton/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func pointerStyle(PointerStyle?) -> some View](communicationlimitsbutton/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
- [func pointerVisibility(Visibility) -> some View](communicationlimitsbutton/pointervisibility(_:).md)
  Sets the visibility of the pointer when it’s over the view.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](communicationlimitsbutton/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](communicationlimitsbutton/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func position(CGPoint) -> some View](communicationlimitsbutton/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](communicationlimitsbutton/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func preference<K>(key: K.Type, value: K.Value) -> some View](communicationlimitsbutton/preference(key:value:).md)
  Sets a value for the given preference.
- [func preferredColorScheme(ColorScheme?) -> some View](communicationlimitsbutton/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](communicationlimitsbutton/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [func preferredWindowClippingMargins(Edge3D.Set, CGFloat?) -> some View](communicationlimitsbutton/preferredwindowclippingmargins(_:_:)-42sc7.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func preferredWindowClippingMargins(Edge3D.Set, EdgeInsets3D) -> some View](communicationlimitsbutton/preferredwindowclippingmargins(_:_:)-93raa.md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](communicationlimitsbutton/prefersdefaultfocus(_:in:).md)
  Indicates that the view should receive focus by default for a given namespace.
- [func presentationBackground<S>(S) -> some View](communicationlimitsbutton/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](communicationlimitsbutton/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](communicationlimitsbutton/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](communicationlimitsbutton/presentationbreakthrougheffect(_:).md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](communicationlimitsbutton/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](communicationlimitsbutton/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](communicationlimitsbutton/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](communicationlimitsbutton/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationDetents(Set<PresentationDetent>) -> some View](communicationlimitsbutton/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](communicationlimitsbutton/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](communicationlimitsbutton/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationPreventsAppTermination(Bool?) -> some View](communicationlimitsbutton/presentationpreventsapptermination(_:).md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [func presentationSizing(some PresentationSizing) -> some View](communicationlimitsbutton/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func presentedWindowStyle<S>(S) -> some View](communicationlimitsbutton/presentedwindowstyle(_:).md)
  Sets the style for windows created by interacting with this view.
- [func presentedWindowToolbarStyle<S>(S) -> some View](communicationlimitsbutton/presentedwindowtoolbarstyle(_:).md)
  Sets the style for the toolbar in windows created by interacting with this view.
- [func previewContext<C>(C) -> some View](communicationlimitsbutton/previewcontext(_:).md)
  Declares a context for the preview.
- [func previewDevice(PreviewDevice?) -> some View](communicationlimitsbutton/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](communicationlimitsbutton/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](communicationlimitsbutton/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewLayout(PreviewLayout) -> some View](communicationlimitsbutton/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func privacySensitive(Bool) -> some View](communicationlimitsbutton/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func progressViewStyle<S>(S) -> some View](communicationlimitsbutton/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func projectionEffect(ProjectionTransform) -> some View](communicationlimitsbutton/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func redacted(reason: RedactionReasons) -> some View](communicationlimitsbutton/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func refreshable(action: () async -> Void) -> some View](communicationlimitsbutton/refreshable(action:).md)
  Marks this view as refreshable.
- [func renameAction(FocusState<Bool>.Binding) -> some View](communicationlimitsbutton/renameaction(_:)-4oi5e.md)
  Sets the rename action in the environment to update focus state.
- [func renameAction(() -> Void) -> some View](communicationlimitsbutton/renameaction(_:)-59h35.md)
  Sets a closure to run for the rename action.
- [func replaceDisabled(Bool) -> some View](communicationlimitsbutton/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](communicationlimitsbutton/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> some View](communicationlimitsbutton/rotation3deffect(_:axis:anchor:)-256j5.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D) -> some View](communicationlimitsbutton/rotation3deffect(_:axis:anchor:)-7o95m.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>](communicationlimitsbutton/rotation3deffect(_:axis:anchor:)-7vkkl.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](communicationlimitsbutton/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotation3DLayout(Rotation3D) -> some View](communicationlimitsbutton/rotation3dlayout(_:).md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat)) -> some View](communicationlimitsbutton/rotation3dlayout(_:axis:)-8h22r.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(Angle, axis: RotationAxis3D) -> some View](communicationlimitsbutton/rotation3dlayout(_:axis:)-9cb1x.md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](communicationlimitsbutton/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](communicationlimitsbutton/safeareabar(edge:alignment:spacing:content:)-3fot.md)
  Renders the provided content appropriate to be displayed as a custom bar.
- [func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](communicationlimitsbutton/safeareabar(edge:alignment:spacing:content:)-8o6wn.md)
  Renders the provided content appropriately to be displayed as a custom bar.
- [func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> V) -> some View](communicationlimitsbutton/safeareainset(edge:alignment:spacing:content:)-16c3h.md)
  Shows the specified content above or below the modified view.
- [func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> V) -> some View](communicationlimitsbutton/safeareainset(edge:alignment:spacing:content:)-gy17.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(CGFloat) -> some View](communicationlimitsbutton/safeareapadding(_:)-44lcf.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(EdgeInsets) -> some View](communicationlimitsbutton/safeareapadding(_:)-7l9st.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](communicationlimitsbutton/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func saturation(Double) -> some View](communicationlimitsbutton/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](communicationlimitsbutton/scaleeffect(_:anchor:)-18h79.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self, _UniformScaleEffect>](communicationlimitsbutton/scaleeffect(_:anchor:)-190b2.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> some View](communicationlimitsbutton/scaleeffect(_:anchor:)-2krym.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View](communicationlimitsbutton/scaleeffect(_:anchor:)-50lqo.md)
  Scales this view uniformly by the specified factor, relative to an anchor point.
- [func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View](communicationlimitsbutton/scaleeffect(_:anchor:)-9c3v1.md)
  Scales this view uniformly by the specified size in each dimension, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](communicationlimitsbutton/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](communicationlimitsbutton/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [func scaledToFill() -> some View](communicationlimitsbutton/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFill3D() -> some View](communicationlimitsbutton/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](communicationlimitsbutton/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaledToFit3D() -> some View](communicationlimitsbutton/scaledtofit3d.md)
  Scales this view to fit its parent.
- [func scenePadding(Edge.Set) -> some View](communicationlimitsbutton/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](communicationlimitsbutton/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](communicationlimitsbutton/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollClipDisabled(Bool) -> some View](communicationlimitsbutton/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func scrollContentBackground(Visibility) -> some View](communicationlimitsbutton/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollDisabled(Bool) -> some View](communicationlimitsbutton/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](communicationlimitsbutton/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](communicationlimitsbutton/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](communicationlimitsbutton/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](communicationlimitsbutton/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](communicationlimitsbutton/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](communicationlimitsbutton/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](communicationlimitsbutton/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](communicationlimitsbutton/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](communicationlimitsbutton/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](communicationlimitsbutton/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](communicationlimitsbutton/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](communicationlimitsbutton/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](communicationlimitsbutton/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func searchCompletion<T>(T) -> some View](communicationlimitsbutton/searchcompletion(_:)-1gi3d.md)
  Associates a search token with the value of this view when used as a search suggestion.
- [func searchCompletion(String) -> some View](communicationlimitsbutton/searchcompletion(_:)-7kqxz.md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](communicationlimitsbutton/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](communicationlimitsbutton/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](communicationlimitsbutton/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](communicationlimitsbutton/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](communicationlimitsbutton/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](communicationlimitsbutton/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchSelection(Binding<TextSelection?>) -> some View](communicationlimitsbutton/searchselection(_:).md)
  Binds the selection of the search field associated with the nearest searchable modifier to the given `TextSelection` value.
- [func searchSuggestions<S>(() -> S) -> some View](communicationlimitsbutton/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](communicationlimitsbutton/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](communicationlimitsbutton/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:ispresented:placement:prompt:token:)-1bkbl.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:ispresented:placement:prompt:token:)-1oyf9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:ispresented:placement:prompt:token:)-7sf4k.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:ispresented:placement:prompt:token:)-91a7l.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:placement:prompt:token:)-38vqe.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:placement:prompt:token:)-4987y.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:placement:prompt:token:)-6mxwg.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](communicationlimitsbutton/searchable(text:editabletokens:placement:prompt:token:)-7dfm4.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](communicationlimitsbutton/searchable(text:ispresented:placement:prompt:)-1bl5h.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](communicationlimitsbutton/searchable(text:ispresented:placement:prompt:)-26wvt.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?) -> some View](communicationlimitsbutton/searchable(text:ispresented:placement:prompt:)-4omt2.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S) -> some View](communicationlimitsbutton/searchable(text:ispresented:placement:prompt:)-obnd.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:)-5c281.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:)-75q77.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:)-9endt.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:)-ypcp.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:suggestions:)-1r217.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:suggestions:)-7qz0w.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](communicationlimitsbutton/searchable(text:placement:prompt:suggestions:)-p32i.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:ispresented:placement:prompt:token:)-1jf5f.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:ispresented:placement:prompt:token:)-67ffb.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:ispresented:placement:prompt:token:)-7a4o9.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:ispresented:placement:prompt:token:)-7qk6p.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:placement:prompt:token:)-1mtbs.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:placement:prompt:token:)-3t274.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:placement:prompt:token:)-6lfle.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:placement:prompt:token:)-9e4ks.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-61h3f.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-8swdo.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-95nmh.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-e6a5.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-47b6n.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-4btlo.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-66aqz.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](communicationlimitsbutton/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-9r7yj.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func sectionActions<Content>(content: () -> Content) -> some View](communicationlimitsbutton/sectionactions(content:).md)
  Adds custom actions to a section.
- [func sectionIndexLabel(Text?) -> some View](communicationlimitsbutton/sectionindexlabel(_:)-2u89r.md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
- [func sectionIndexLabel<S>(S?) -> some View](communicationlimitsbutton/sectionindexlabel(_:)-7j3hw.md)
  Sets the title that is used for the section index label pointing to this section, typically only a single character long.
- [func selectionDisabled(Bool) -> some View](communicationlimitsbutton/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](communicationlimitsbutton/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](communicationlimitsbutton/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](communicationlimitsbutton/sensoryfeedback(trigger:_:)-241g0.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, () -> SensoryFeedback?) -> some View](communicationlimitsbutton/sensoryfeedback(trigger:_:)-4zl6q.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](communicationlimitsbutton/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](communicationlimitsbutton/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](communicationlimitsbutton/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](communicationlimitsbutton/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](communicationlimitsbutton/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](communicationlimitsbutton/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](communicationlimitsbutton/spatialoverlay(alignment:content:).md)
  Adds secondary views within the 3D bounds of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](communicationlimitsbutton/spatialoverlaypreferencevalue(_:alignment:_:).md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
- [func speechAdjustedPitch(Double) -> some View](communicationlimitsbutton/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](communicationlimitsbutton/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](communicationlimitsbutton/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](communicationlimitsbutton/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](communicationlimitsbutton/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [func statusBar(hidden: Bool) -> some View](communicationlimitsbutton/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func statusBarHidden(Bool) -> some View](communicationlimitsbutton/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](communicationlimitsbutton/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func submitLabel(SubmitLabel) -> some View](communicationlimitsbutton/submitlabel(_:).md)
  Sets the submit label for this view.
- [func submitScope(Bool) -> some View](communicationlimitsbutton/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](communicationlimitsbutton/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](communicationlimitsbutton/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](communicationlimitsbutton/symbolcolorrenderingmode(_:).md)
  Sets the color rendering mode for symbol images.
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](communicationlimitsbutton/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](communicationlimitsbutton/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](communicationlimitsbutton/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](communicationlimitsbutton/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](communicationlimitsbutton/symbolvariablevaluemode(_:).md)
  Sets the variable value mode mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](communicationlimitsbutton/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](communicationlimitsbutton/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabItem<V>(() -> V) -> some View](communicationlimitsbutton/tabitem(_:).md)
  Sets the tab bar item associated with this view.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](communicationlimitsbutton/tabviewbottomaccessory(content:).md)
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](communicationlimitsbutton/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](communicationlimitsbutton/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](communicationlimitsbutton/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](communicationlimitsbutton/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewStyle<S>(S) -> some View](communicationlimitsbutton/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func tableColumnHeaders(Visibility) -> some View](communicationlimitsbutton/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func tableStyle<S>(S) -> some View](communicationlimitsbutton/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func tag<V>(V, includeOptional: Bool) -> some View](communicationlimitsbutton/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](communicationlimitsbutton/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](communicationlimitsbutton/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func textCase(Text.Case?) -> some View](communicationlimitsbutton/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textContentType(NSTextContentType?) -> some View](communicationlimitsbutton/textcontenttype(_:)-3k252.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textContentType(UITextContentType?) -> some View](communicationlimitsbutton/textcontenttype(_:)-ukxt.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textEditorStyle(some TextEditorStyle) -> some View](communicationlimitsbutton/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [func textFieldStyle<S>(S) -> some View](communicationlimitsbutton/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](communicationlimitsbutton/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputCompletion(String) -> some View](communicationlimitsbutton/textinputcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](communicationlimitsbutton/textinputformattingcontrolvisibility(_:for:).md)
  Define which system text formatting controls are available.
- [func textInputSuggestions<S>(() -> S) -> some View](communicationlimitsbutton/textinputsuggestions(_:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](communicationlimitsbutton/textinputsuggestions(_:content:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](communicationlimitsbutton/textinputsuggestions(_:id:content:).md)
  Configures the text input suggestions for this view.
- [func textRenderer<T>(T) -> some View](communicationlimitsbutton/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](communicationlimitsbutton/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textSelection<S>(S) -> some View](communicationlimitsbutton/textselection(_:).md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](communicationlimitsbutton/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tint(Color?) -> some View](communicationlimitsbutton/tint(_:).md)
  Sets the tint color within this view.
- [func toggleStyle<S>(S) -> some View](communicationlimitsbutton/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar<Content>(content: () -> Content) -> some View](communicationlimitsbutton/toolbar(content:)-4sbvg.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(content: () -> Content) -> some View](communicationlimitsbutton/toolbar(content:)-8h78.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](communicationlimitsbutton/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](communicationlimitsbutton/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarbackground(_:for:)-3dayy.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarbackground(_:for:)-4gnv9.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](communicationlimitsbutton/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func toolbarRole(ToolbarRole) -> some View](communicationlimitsbutton/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](communicationlimitsbutton/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](communicationlimitsbutton/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](communicationlimitsbutton/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func touchBar<Content>(TouchBar<Content>) -> some View](communicationlimitsbutton/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBar<Content>(content: () -> Content) -> some View](communicationlimitsbutton/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBarCustomizationLabel(Text) -> some View](communicationlimitsbutton/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](communicationlimitsbutton/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [func touchBarItemPrincipal(Bool) -> some View](communicationlimitsbutton/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func tracking(CGFloat) -> some View](communicationlimitsbutton/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func transaction((inout Transaction) -> Void) -> some View](communicationlimitsbutton/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](communicationlimitsbutton/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](communicationlimitsbutton/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transform3DEffect(AffineTransform3D) -> some View](communicationlimitsbutton/transform3deffect(_:).md)
  Applies a 3D transformation to this view’s rendered output.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](communicationlimitsbutton/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformEffect(CGAffineTransform) -> some View](communicationlimitsbutton/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](communicationlimitsbutton/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](communicationlimitsbutton/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func transition<T>(T) -> some View](communicationlimitsbutton/transition(_:)-7sbwq.md)
  Associates a transition with the view.
- [func transition(AnyTransition) -> some View](communicationlimitsbutton/transition(_:)-9zbzd.md)
  Associates a transition with the view.
- [func truncationMode(Text.TruncationMode) -> some View](communicationlimitsbutton/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typeSelectEquivalent(LocalizedStringKey) -> some View](communicationlimitsbutton/typeselectequivalent(_:)-3qzid.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(Text?) -> some View](communicationlimitsbutton/typeselectequivalent(_:)-4fmi7.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent<S>(S) -> some View](communicationlimitsbutton/typeselectequivalent(_:)-4kp75.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringResource) -> some View](communicationlimitsbutton/typeselectequivalent(_:)-7nlr.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View](communicationlimitsbutton/typesettinglanguage(_:isenabled:)-205bc.md)
  Specifies the language for typesetting.
- [func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View](communicationlimitsbutton/typesettinglanguage(_:isenabled:)-2b6gf.md)
  Specifies the language for typesetting.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](communicationlimitsbutton/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func unredacted() -> some View](communicationlimitsbutton/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func upperLimbVisibility(Visibility) -> some View](communicationlimitsbutton/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an `ImmersiveSpace` scene is presented.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](communicationlimitsbutton/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](communicationlimitsbutton/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](communicationlimitsbutton/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](communicationlimitsbutton/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [func volumeBaseplateVisibility(Visibility) -> some View](communicationlimitsbutton/volumebaseplatevisibility(_:).md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](communicationlimitsbutton/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](communicationlimitsbutton/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](communicationlimitsbutton/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeAnchor(UnitPoint?) -> some View](communicationlimitsbutton/windowresizeanchor(_:).md)
  Sets the window anchor point used when the size of the view changes such that the window must resize.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](communicationlimitsbutton/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](communicationlimitsbutton/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](communicationlimitsbutton/writingdirection(strategy:).md)
  A modifier for the default text writing direction strategy in the view hierarchy.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](communicationlimitsbutton/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](communicationlimitsbutton/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [func zIndex(Double) -> some View](communicationlimitsbutton/zindex(_:).md)
  Controls the display order of overlapping views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/view-implementations)*