# View Implementations

**Framework**: FinanceKitUI

## Topics

### Instance Methods
- [func accentColor(Color?) -> some View](transactionpicker/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(activationpoint:)-1dt9u.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(activationpoint:)-4whz8.md)
  Specifies the point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](transactionpicker/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaction(named:_:)-35e7g.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringResource, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaction(named:_:)-4ecgw.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaction(named:_:)-6xtwe.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaction(named:_:)-9pny8.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](transactionpicker/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](transactionpicker/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityactivationpoint(_:)-6rvp8.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityactivationpoint(_:)-8xbgh.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityactivationpoint(_:isenabled:)-3ibuc.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityactivationpoint(_:isenabled:)-4qcwx.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityChartDescriptor<R>(R) -> some View](transactionpicker/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [func accessibilityChildren<V>(children: () -> V) -> some View](transactionpicker/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-13w5f.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-1cy94.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-3jy8n.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-3r7uc.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-3rziz.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-42ms.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-4kzb7.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-4wftr.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringResource, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-7uekk.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-7yc8t.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringResource, LocalizedStringResource, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-7zsty.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitycustomcontent(_:_:importance:)-9lih.md)
  Add additional accessibility information to the view.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](transactionpicker/accessibilitydefaultfocus(_:_:).md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:)-4hiic.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:)-5bzqd.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:)-6q8wi.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:)-9z7qf.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:isenabled:)-1ahis.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:isenabled:)-29ktm.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:isenabled:)-34wjq.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydragpoint(_:description:isenabled:)-4b3sr.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:)-1b8zp.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:)-5uezm.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:)-6mqib.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:)-812wb.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:isenabled:)-2gje4.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:isenabled:)-4me1l.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:isenabled:)-8ihnm.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitydroppoint(_:description:isenabled:)-s8kw.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](transactionpicker/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](transactionpicker/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](transactionpicker/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:)-1coc8.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:)-2uosv.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:)-5j3w.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:)-k4x2.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:isenabled:)-2wbvr.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:isenabled:)-313qo.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:isenabled:)-412vn.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityhint(_:isenabled:)-awa2.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIgnoresInvertColors(Bool) -> some View](transactionpicker/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:)-7hmje.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:)-9dz3d.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:)-9lt7s.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:isenabled:)-3l0lr.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:isenabled:)-7q3p7.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityinputlabels(_:isenabled:)-8vkky.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:)-1gd0h.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:)-52333.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:)-63hc2.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:)-6b5go.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:isenabled:)-1jqpe.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:isenabled:)-6i9zk.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:isenabled:)-7bxce.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitylabel(_:isenabled:)-ebco.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](transactionpicker/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](transactionpicker/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](transactionpicker/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](transactionpicker/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](transactionpicker/accessibilityrotor(_:entries:)-1gid5.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<Content>(LocalizedStringResource, entries: () -> Content) -> some View](transactionpicker/accessibilityrotor(_:entries:)-33p1d.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](transactionpicker/accessibilityrotor(_:entries:)-4oy8u.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](transactionpicker/accessibilityrotor(_:entries:)-810nv.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](transactionpicker/accessibilityrotor(_:entries:)-8e4dq.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entryid:entrylabel:)-3fnfv.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entryid:entrylabel:)-5n4lx.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entryid:entrylabel:)-85l93.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringResource, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entryid:entrylabel:)-9735a.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entryid:entrylabel:)-nr0b.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringResource, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entrylabel:)-16o8m.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entrylabel:)-1onu0.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entrylabel:)-2kahu.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entrylabel:)-4v0hv.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](transactionpicker/accessibilityrotor(_:entries:entrylabel:)-6xh8a.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](transactionpicker/accessibilityrotor(_:textranges:)-2bcct.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](transactionpicker/accessibilityrotor(_:textranges:)-3dxtq.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringResource, textRanges: [Range<String.Index>]) -> some View](transactionpicker/accessibilityrotor(_:textranges:)-4hooa.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](transactionpicker/accessibilityrotor(_:textranges:)-8toaz.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](transactionpicker/accessibilityrotor(_:textranges:)-vug9.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](transactionpicker/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollStatus(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityscrollstatus(_:isenabled:)-2jbos.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityscrollstatus(_:isenabled:)-73b99.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(some StringProtocol, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityscrollstatus(_:isenabled:)-7pj5o.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityScrollStatus(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityscrollstatus(_:isenabled:)-9aqao.md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessibilityShowsLargeContentViewer() -> some View](transactionpicker/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](transactionpicker/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:)-2qmur.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:)-8tyvq.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:)-975pe.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:)-9c555.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:isenabled:)-205ba.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:isenabled:)-5teom.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:isenabled:)-6yohf.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityvalue(_:isenabled:)-71nu7.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](transactionpicker/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](transactionpicker/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](transactionpicker/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](transactionpicker/addordertowalletbuttonstyle(_:).md)
  Sets the button’s style.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](transactionpicker/alert(_:ispresented:actions:)-3aked.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](transactionpicker/alert(_:ispresented:actions:)-65wfu.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](transactionpicker/alert(_:ispresented:actions:)-82bt1.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<A>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A) -> some View](transactionpicker/alert(_:ispresented:actions:)-8smtm.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](transactionpicker/alert(_:ispresented:actions:message:)-11qhp.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](transactionpicker/alert(_:ispresented:actions:message:)-1hzbn.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](transactionpicker/alert(_:ispresented:actions:message:)-3okze.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](transactionpicker/alert(_:ispresented:actions:message:)-592nk.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:)-3hiir.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:)-4i1e4.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:)-5d88n.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:)-6rksr.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:message:)-18bpj.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:message:)-3jpeh.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:message:)-4aidl.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/alert(_:ispresented:presenting:actions:message:)-9yvl4.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](transactionpicker/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](transactionpicker/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](transactionpicker/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](transactionpicker/alert(item:content:).md)
  Presents an alert to the user.
- [func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](transactionpicker/alignmentguide(_:computevalue:)-19z1d.md)
  Sets the view’s horizontal alignment.
- [func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](transactionpicker/alignmentguide(_:computevalue:)-819ap.md)
  Sets the view’s vertical alignment.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](transactionpicker/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
- [func allowsHitTesting(Bool) -> some View](transactionpicker/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func allowsTightening(Bool) -> some View](transactionpicker/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func allowsWindowActivationEvents() -> some View](transactionpicker/allowswindowactivationevents.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func allowsWindowActivationEvents(Bool?) -> some View](transactionpicker/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](transactionpicker/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func animation(Animation?) -> some View](transactionpicker/animation(_:).md)
  Applies the given animation to all animatable values within this view.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](transactionpicker/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation<V>(Animation?, value: V) -> some View](transactionpicker/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View](transactionpicker/aspectratio(_:contentmode:)-9gkd9.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](transactionpicker/aspectratio(_:contentmode:)-9trjk.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
- [func assistiveAccessNavigationIcon(Image) -> some View](transactionpicker/assistiveaccessnavigationicon(_:).md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](transactionpicker/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.
- [func attributedTextFormattingDefinition<S>(S.Type) -> some View](transactionpicker/attributedtextformattingdefinition(_:)-2n4zh.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<D>(D) -> some View](transactionpicker/attributedtextformattingdefinition(_:)-38u1p.md)
  Apply a text formatting definition to all nested editor views.
- [func attributedTextFormattingDefinition<S>(KeyPath<AttributeScopes, S.Type>) -> some View](transactionpicker/attributedtextformattingdefinition(_:)-9t29x.md)
  Apply an attribute-only text formatting definition to all nested editor views.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](transactionpicker/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func autocorrectionDisabled(Bool) -> some View](transactionpicker/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](transactionpicker/background(_:alignment:).md)
  Layers the given view behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](transactionpicker/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](transactionpicker/background(_:in:fillstyle:)-1gc9e.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](transactionpicker/background(_:in:fillstyle:)-6n5qv.md)
  Sets the view’s background to a shape filled with a style.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](transactionpicker/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](transactionpicker/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](transactionpicker/background(in:fillstyle:)-7kzlw.md)
  Sets the view’s background to a shape filled with the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](transactionpicker/background(in:fillstyle:)-e3rs.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func backgroundExtensionEffect() -> some View](transactionpicker/backgroundextensioneffect.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](transactionpicker/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](transactionpicker/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundStyle<S>(S) -> some View](transactionpicker/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func badge(LocalizedStringKey?) -> some View](transactionpicker/badge(_:)-1ft0b.md)
  Generates a badge for the view from a localized string key.
- [func badge(LocalizedStringResource?) -> some View](transactionpicker/badge(_:)-37wwo.md)
  Generates a badge for the view from a localized string resource.
- [func badge(Text?) -> some View](transactionpicker/badge(_:)-4sh96.md)
  Generates a badge for the view from a text view.
- [func badge(Int) -> some View](transactionpicker/badge(_:)-5eaf5.md)
  Generates a badge for the view from an integer value.
- [func badge<S>(S?) -> some View](transactionpicker/badge(_:)-9yvv2.md)
  Generates a badge for the view from a string.
- [func badgeProminence(BadgeProminence) -> some View](transactionpicker/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [func baselineOffset(CGFloat) -> some View](transactionpicker/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func blendMode(BlendMode) -> some View](transactionpicker/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func blur(radius: CGFloat, opaque: Bool) -> some View](transactionpicker/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func bold(Bool) -> some View](transactionpicker/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func border<S>(S, width: CGFloat) -> some View](transactionpicker/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func brightness(Double) -> some View](transactionpicker/brightness(_:).md)
  Brightens this view by the specified amount.
- [func buttonBorderShape(ButtonBorderShape) -> some View](transactionpicker/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](transactionpicker/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func buttonSizing(ButtonSizing) -> some View](transactionpicker/buttonsizing(_:).md)
- [func buttonStyle<S>(S) -> some View](transactionpicker/buttonstyle(_:)-13i92.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonStyle<S>(S) -> some View](transactionpicker/buttonstyle(_:)-6nr7z.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func clipShape<S>(S, style: FillStyle) -> some View](transactionpicker/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func clipped(antialiased: Bool) -> some View](transactionpicker/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func colorEffect(Shader, isEnabled: Bool) -> some View](transactionpicker/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func colorInvert() -> some View](transactionpicker/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](transactionpicker/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func colorScheme(ColorScheme) -> some View](transactionpicker/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func compositingGroup() -> some View](transactionpicker/compositinggroup.md)
  Wraps this view in a compositing group.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-2d53j.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-3og0v.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-49ufj.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<A>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-99lcq.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-2ct9s.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-2wlda.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-497jx.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<A, M>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-50b0x.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-3g9dd.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-463t6.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-6cyzb.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-7ywl3.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-2a5rf.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-7qudj.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-8q245.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringResource, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](transactionpicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-9h1kc.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](transactionpicker/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](transactionpicker/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](transactionpicker/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](transactionpicker/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](transactionpicker/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerShape<T>(T) -> some View](transactionpicker/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](transactionpicker/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some View](transactionpicker/contentmargins(_:_:for:)-4364o.md)
  Configures the content margin for a provided placement.
- [func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) -> some View](transactionpicker/contentmargins(_:_:for:)-4wla.md)
  Configures the content margin for a provided placement.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](transactionpicker/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](transactionpicker/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [func contentShape<S>(S, eoFill: Bool) -> some View](transactionpicker/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](transactionpicker/contenttoolbar(for:content:)-1yt38.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](transactionpicker/contenttoolbar(for:content:)-8tblo.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentTransition(ContentTransition) -> some View](transactionpicker/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](transactionpicker/contextmenu(_:).md)
  Adds a context menu to the view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](transactionpicker/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](transactionpicker/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](transactionpicker/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contrast(Double) -> some View](transactionpicker/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func controlGroupStyle<S>(S) -> some View](transactionpicker/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func controlSize<T>(T) -> some View](transactionpicker/controlsize(_:)-5hkrg.md)
  Limits the control size within the view to the given range.
- [func controlSize(ControlSize) -> some View](transactionpicker/controlsize(_:)-8e1p9.md)
  Sets the size for controls within this view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](transactionpicker/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func coordinateSpace<T>(name: T) -> some View](transactionpicker/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](transactionpicker/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func datePickerStyle<S>(S) -> some View](transactionpicker/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](transactionpicker/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultAppStorage(UserDefaults) -> some View](transactionpicker/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](transactionpicker/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func defaultHoverEffect(HoverEffect?) -> some View](transactionpicker/defaulthovereffect(_:)-6lxtf.md)
  Sets the default hover effect to use for views within this view.
- [func defaultHoverEffect(some CustomHoverEffect) -> some View](transactionpicker/defaulthovereffect(_:)-70tst.md)
  Sets the default hover effect to use within this view hierarchy.
- [func defaultScrollAnchor(UnitPoint?) -> some View](transactionpicker/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](transactionpicker/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func defersSystemGestures(on: Edge.Set) -> some View](transactionpicker/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func deleteDisabled(Bool) -> some View](transactionpicker/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [func dialogIcon(Image?) -> some View](transactionpicker/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View](transactionpicker/dialogsuppressiontoggle(_:issuppressed:)-46c0c.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringResource, isSuppressed: Binding<Bool>) -> some View](transactionpicker/dialogsuppressiontoggle(_:issuppressed:)-4dh1b.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>) -> some View](transactionpicker/dialogsuppressiontoggle(_:issuppressed:)-5zsme.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View](transactionpicker/dialogsuppressiontoggle(_:issuppressed:)-8ooyf.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](transactionpicker/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func disableAutocorrection(Bool?) -> some View](transactionpicker/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func disabled(Bool) -> some View](transactionpicker/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func disclosureGroupStyle<S>(S) -> some View](transactionpicker/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](transactionpicker/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](transactionpicker/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func dragConfiguration(DragConfiguration) -> some View](transactionpicker/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, (ItemID) -> Data) -> some View](transactionpicker/dragcontainer(for:id:in:_:).md)
  A container with draggable views. The drag payload is based on the current selection.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (consuming Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> Array<ItemID>, (Array<ItemID>) -> Data) -> some View](transactionpicker/dragcontainer(for:id:in:selection:_:)-1j646.md)
  A container with multiple selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, ItemID>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, selection: @autoclosure () -> ItemID?, (ItemID) -> Item?) -> some View](transactionpicker/dragcontainer(for:id:in:selection:_:)-43uih.md)
  A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, (Item.ID) -> Data) -> some View](transactionpicker/dragcontainer(for:in:_:).md)
  A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.
- [func dragContainer<Item>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Item.ID?, (Item.ID) -> Item?) -> some View](transactionpicker/dragcontainer(for:in:selection:_:)-522v0.md)
  A container with single item selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, selection: @autoclosure () -> Array<Item.ID>, (Array<Item.ID>) -> Data) -> some View](transactionpicker/dragcontainer(for:in:selection:_:)-7i82n.md)
  A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func draggable<T>(@autoclosure () -> T) -> some View](transactionpicker/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](transactionpicker/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<T, ID>(for: T.Type, id: ID, (ID) -> T?) -> some View](transactionpicker/draggable(for:id:_:).md)
  Activates this view as the source of a drag-and-drop operation.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](transactionpicker/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](transactionpicker/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](transactionpicker/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](transactionpicker/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dynamicTypeSize(DynamicTypeSize) -> some View](transactionpicker/dynamictypesize(_:)-26ln1.md)
  Sets the Dynamic Type size within the view to the given value.
- [func dynamicTypeSize<T>(T) -> some View](transactionpicker/dynamictypesize(_:)-8rviw.md)
  Limits the Dynamic Type size within the view to the given range.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](transactionpicker/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func environment<T>(T?) -> some View](transactionpicker/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](transactionpicker/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](transactionpicker/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](transactionpicker/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(LocalizedStringKey) -> some View](transactionpicker/filedialogconfirmationlabel(_:)-202g4.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(LocalizedStringResource) -> some View](transactionpicker/filedialogconfirmationlabel(_:)-7vyl5.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel<S>(S) -> some View](transactionpicker/filedialogconfirmationlabel(_:)-9rpzp.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(Text?) -> some View](transactionpicker/filedialogconfirmationlabel(_:)-yu26.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](transactionpicker/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](transactionpicker/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](transactionpicker/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(LocalizedStringKey) -> some View](transactionpicker/filedialogmessage(_:)-1bsmp.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(Text?) -> some View](transactionpicker/filedialogmessage(_:)-3cpbn.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringResource) -> some View](transactionpicker/filedialogmessage(_:)-5iu0.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage<S>(S) -> some View](transactionpicker/filedialogmessage(_:)-7ssra.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](transactionpicker/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](transactionpicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-4i4w7.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](transactionpicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-4who3.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-5793c.md)
  Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-8q4p8.md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](transactionpicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-1evpe.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](transactionpicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-5w9vn.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-1g3pz.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-63ij6.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel<S>(S) -> some View](transactionpicker/fileexporterfilenamelabel(_:)-27rij.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(Text?) -> some View](transactionpicker/fileexporterfilenamelabel(_:)-4q656.md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.
- [func fileExporterFilenameLabel(LocalizedStringResource) -> some View](transactionpicker/fileexporterfilenamelabel(_:)-9jnb9.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(LocalizedStringKey) -> some View](transactionpicker/fileexporterfilenamelabel(_:)-s3oo.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](transactionpicker/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](transactionpicker/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](transactionpicker/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](transactionpicker/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](transactionpicker/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func findDisabled(Bool) -> some View](transactionpicker/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func findNavigator(isPresented: Binding<Bool>) -> some View](transactionpicker/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func fixedSize() -> some View](transactionpicker/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](transactionpicker/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](transactionpicker/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func focusEffectDisabled(Bool) -> some View](transactionpicker/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func focusable(Bool) -> some View](transactionpicker/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](transactionpicker/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focused(FocusState<Bool>.Binding) -> some View](transactionpicker/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](transactionpicker/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focusedObject<T>(T) -> some View](transactionpicker/focusedobject(_:)-13e2k.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedObject<T>(T?) -> some View](transactionpicker/focusedobject(_:)-4xno4.md)
  Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.
- [func focusedSceneObject<T>(T) -> some View](transactionpicker/focusedsceneobject(_:)-82xz7.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneObject<T>(T?) -> some View](transactionpicker/focusedsceneobject(_:)-puxs.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneValue<T>(T?) -> some View](transactionpicker/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some View](transactionpicker/focusedscenevalue(_:_:)-3pgh6.md)
  Creates a new view that exposes the provided value to other views whose state depends on the active scene.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some View](transactionpicker/focusedscenevalue(_:_:)-69u3b.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedValue<T>(T?) -> some View](transactionpicker/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) -> some View](transactionpicker/focusedvalue(_:_:)-448ex.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) -> some View](transactionpicker/focusedvalue(_:_:)-92x0o.md)
  Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.
- [func font(Font?) -> some View](transactionpicker/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](transactionpicker/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](transactionpicker/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](transactionpicker/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func foregroundColor(Color?) -> some View](transactionpicker/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func foregroundStyle<S>(S) -> some View](transactionpicker/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](transactionpicker/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](transactionpicker/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func formStyle<S>(S) -> some View](transactionpicker/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func frame() -> some View](transactionpicker/frame.md)
  Positions this view within an invisible frame.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](transactionpicker/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](transactionpicker/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](transactionpicker/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](transactionpicker/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func gaugeStyle<S>(S) -> some View](transactionpicker/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func geometryGroup() -> some View](transactionpicker/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](transactionpicker/gesture(_:).md)
  Attaches a `UIGestureRecognizerRepresentable` to the view.
- [func gesture<T>(T, including: GestureMask) -> some View](transactionpicker/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](transactionpicker/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](transactionpicker/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](transactionpicker/glasseffect(_:in:isenabled:).md)
  Applies a glass effect to this view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](transactionpicker/glasseffectid(_:in:).md)
  Associates an identity value to glass effects defined within this view.
- [func glassEffectTransition(GlassEffectTransition, isEnabled: Bool) -> some View](transactionpicker/glasseffecttransition(_:isenabled:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](transactionpicker/glasseffectunion(id:namespace:).md)
  Associates any glass effects defined within this view to a union with the provided id.
- [func grayscale(Double) -> some View](transactionpicker/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func gridCellAnchor(UnitPoint) -> some View](transactionpicker/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellColumns(Int) -> some View](transactionpicker/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](transactionpicker/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](transactionpicker/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
- [func groupBoxStyle<S>(S) -> some View](transactionpicker/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](transactionpicker/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](transactionpicker/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
- [func headerProminence(Prominence) -> some View](transactionpicker/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func help<S>(S) -> some View](transactionpicker/help(_:)-2kh8m.md)
  Adds help text to a view using a string that you provide.
- [func help(LocalizedStringKey) -> some View](transactionpicker/help(_:)-3pen9.md)
  Adds help text to a view using a localized string that you provide.
- [func help(Text) -> some View](transactionpicker/help(_:)-4wcrs.md)
  Adds help text to a view using a text view that you provide.
- [func help(LocalizedStringResource) -> some View](transactionpicker/help(_:)-66ito.md)
  Adds help text to a view using a localized string resource that you provide.
- [func hidden() -> some View](transactionpicker/hidden.md)
  Hides this view unconditionally.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](transactionpicker/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](transactionpicker/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](transactionpicker/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func hoverEffect(HoverEffect) -> some View](transactionpicker/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(HoverEffect, isEnabled: Bool) -> some View](transactionpicker/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffectDisabled(Bool) -> some View](transactionpicker/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func hueRotation(Angle) -> some View](transactionpicker/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func id<ID>(ID) -> some View](transactionpicker/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](transactionpicker/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func imageScale(Image.Scale) -> some View](transactionpicker/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func indexViewStyle<S>(S) -> some View](transactionpicker/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](transactionpicker/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](transactionpicker/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](transactionpicker/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
- [func interactionActivityTrackingTag(String) -> some View](transactionpicker/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func interactiveDismissDisabled(Bool) -> some View](transactionpicker/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func invalidatableContent(Bool) -> some View](transactionpicker/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
- [func italic(Bool) -> some View](transactionpicker/italic(_:).md)
  Applies italics to the text in this view.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](transactionpicker/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func kerning(CGFloat) -> some View](transactionpicker/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func keyboardShortcut(KeyboardShortcut?) -> some View](transactionpicker/keyboardshortcut(_:)-7ay99.md)
  Assigns an optional keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyboardShortcut) -> some View](transactionpicker/keyboardshortcut(_:)-8ja68.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](transactionpicker/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](transactionpicker/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardType(UIKeyboardType) -> some View](transactionpicker/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](transactionpicker/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](transactionpicker/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func labelIconToTitleSpacing(CGFloat) -> some View](transactionpicker/labelicontotitlespacing(_:).md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](transactionpicker/labelreservediconwidth(_:).md)
  Set the width reserved for icons in labels.
- [func labelStyle<S>(S) -> some View](transactionpicker/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func labeledContentStyle<S>(S) -> some View](transactionpicker/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsHidden() -> some View](transactionpicker/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](transactionpicker/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](transactionpicker/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](transactionpicker/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [func layoutPriority(Double) -> some View](transactionpicker/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](transactionpicker/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.
- [func lineHeight(AttributedString.LineHeight?) -> some View](transactionpicker/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func lineLimit(PartialRangeThrough<Int>) -> some View](transactionpicker/linelimit(_:)-10yss.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeFrom<Int>) -> some View](transactionpicker/linelimit(_:)-7kdgf.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(Int?) -> some View](transactionpicker/linelimit(_:)-80f4v.md)
  Sets the maximum number of lines that text can occupy in this view.
- [func lineLimit(ClosedRange<Int>) -> some View](transactionpicker/linelimit(_:)-t14n.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](transactionpicker/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](transactionpicker/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func listItemTint(ListItemTint?) -> some View](transactionpicker/listitemtint(_:)-2l1qu.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](transactionpicker/listitemtint(_:)-4hb55.md)
  Sets a fixed tint color for content in a list.
- [func listRowBackground<V>(V?) -> some View](transactionpicker/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func listRowInsets(EdgeInsets?) -> some View](transactionpicker/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](transactionpicker/listrowinsets(_:_:).md)
  Sets the insets of rows in a list on the specified edges.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](transactionpicker/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](transactionpicker/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSpacing(CGFloat?) -> some View](transactionpicker/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionIndexVisibility(Visibility) -> some View](transactionpicker/listsectionindexvisibility(_:).md)
  Changes the visibility of the list section index.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](transactionpicker/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](transactionpicker/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](transactionpicker/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSpacing(ListSectionSpacing) -> some View](transactionpicker/listsectionspacing(_:)-7djx6.md)
  Sets the spacing between adjacent sections in a `List`.
- [func listSectionSpacing(CGFloat) -> some View](transactionpicker/listsectionspacing(_:)-9waf2.md)
  Sets the spacing between adjacent sections in a `List` to a custom value.
- [func listStyle<S>(S) -> some View](transactionpicker/liststyle(_:).md)
  Sets the style for lists within this view.
- [func luminanceToAlpha() -> some View](transactionpicker/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func mask<Mask>(Mask) -> some View](transactionpicker/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](transactionpicker/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](transactionpicker/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](transactionpicker/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](transactionpicker/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](transactionpicker/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](transactionpicker/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func menuIndicator(Visibility) -> some View](transactionpicker/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func menuOrder(MenuOrder) -> some View](transactionpicker/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuStyle<S>(S) -> some View](transactionpicker/menustyle(_:).md)
  Sets the style for menus within this view.
- [func minimumScaleFactor(CGFloat) -> some View](transactionpicker/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](transactionpicker/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [func monospaced(Bool) -> some View](transactionpicker/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](transactionpicker/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func moveDisabled(Bool) -> some View](transactionpicker/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func multilineTextAlignment(TextAlignment) -> some View](transactionpicker/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](transactionpicker/multilinetextalignment(strategy:).md)
  A modifier for the default text alignment strategy in the view hierarchy.
- [func navigationBarBackButtonHidden(Bool) -> some View](transactionpicker/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarHidden(Bool) -> some View](transactionpicker/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](transactionpicker/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](transactionpicker/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](transactionpicker/navigationbaritems(trailing:).md)
- [func navigationBarTitle(LocalizedStringKey) -> some View](transactionpicker/navigationbartitle(_:)-3h9gc.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](transactionpicker/navigationbartitle(_:)-74oai.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle<S>(S) -> some View](transactionpicker/navigationbartitle(_:)-ozd5.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](transactionpicker/navigationbartitle(_:displaymode:)-1inzk.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](transactionpicker/navigationbartitle(_:displaymode:)-6b296.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](transactionpicker/navigationbartitle(_:displaymode:)-mczc.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](transactionpicker/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](transactionpicker/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](transactionpicker/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](transactionpicker/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationDocument<D>(D) -> some View](transactionpicker/navigationdocument(_:)-6y0hh.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(URL) -> some View](transactionpicker/navigationdocument(_:)-9s762.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some View](transactionpicker/navigationdocument(_:preview:)-190vc.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some View](transactionpicker/navigationdocument(_:preview:)-3ctki.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some View](transactionpicker/navigationdocument(_:preview:)-6xpy6.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some View](transactionpicker/navigationdocument(_:preview:)-7008j.md)
  Configures the view’s document for purposes of navigation.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](transactionpicker/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](transactionpicker/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](transactionpicker/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationSplitViewStyle<S>(S) -> some View](transactionpicker/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSubtitle(Text) -> some View](transactionpicker/navigationsubtitle(_:)-49pcz.md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationSubtitle(LocalizedStringResource) -> some View](transactionpicker/navigationsubtitle(_:)-7rw24.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
- [func navigationSubtitle(LocalizedStringKey) -> some View](transactionpicker/navigationsubtitle(_:)-8gcqy.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string.
- [func navigationSubtitle<S>(S) -> some View](transactionpicker/navigationsubtitle(_:)-9vd0y.md)
  Configures the view’s subtitle for purposes of navigation, using a string.
- [func navigationTitle(LocalizedStringKey) -> some View](transactionpicker/navigationtitle(_:)-1n86s.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle(Text) -> some View](transactionpicker/navigationtitle(_:)-4eepc.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTitle(LocalizedStringResource) -> some View](transactionpicker/navigationtitle(_:)-53k92.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationTitle<V>(() -> V) -> some View](transactionpicker/navigationtitle(_:)-567cb.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle<S>(S) -> some View](transactionpicker/navigationtitle(_:)-68829.md)
  Configures the view’s title for purposes of navigation, using a string.
- [func navigationTitle(Binding<String>) -> some View](transactionpicker/navigationtitle(_:)-ao1q.md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationTransition(some NavigationTransition) -> some View](transactionpicker/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func navigationViewStyle<S>(S) -> some View](transactionpicker/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func offset(CGSize) -> some View](transactionpicker/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](transactionpicker/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func onAppear(perform: (() -> Void)?) -> some View](transactionpicker/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, initial: Bool, () -> Void) -> some View](transactionpicker/onchange(of:initial:_:)-6ovdr.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View](transactionpicker/onchange(of:initial:_:)-80ra6.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](transactionpicker/onchange(of:perform:).md)
  Performs an action when a specified value changes.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](transactionpicker/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](transactionpicker/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onDisappear(perform: (() -> Void)?) -> some View](transactionpicker/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onDrag(() -> NSItemProvider) -> some View](transactionpicker/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](transactionpicker/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](transactionpicker/ondragsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](transactionpicker/ondrop(of:delegate:)-3ldpm.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](transactionpicker/ondrop(of:delegate:)-8tbcp.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](transactionpicker/ondrop(of:istargeted:perform:)-1tgco.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](transactionpicker/ondrop(of:istargeted:perform:)-2u8ak.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](transactionpicker/ondrop(of:istargeted:perform:)-4yite.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](transactionpicker/ondrop(of:istargeted:perform:)-c4w9.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](transactionpicker/ondropsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T, T) -> Void) -> some View](transactionpicker/ongeometrychange(for:of:action:)-5p9h7.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T) -> Void) -> some View](transactionpicker/ongeometrychange(for:of:action:)-95s2f.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onHover(perform: (Bool) -> Void) -> some View](transactionpicker/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](transactionpicker/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](transactionpicker/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](transactionpicker/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](transactionpicker/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](transactionpicker/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](transactionpicker/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](transactionpicker/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](transactionpicker/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](transactionpicker/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onOpenURL(perform: (URL) -> ()) -> some View](transactionpicker/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onOpenURL(prefersInApp: Bool) -> some View](transactionpicker/onopenurl(prefersinapp:).md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](transactionpicker/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](transactionpicker/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](transactionpicker/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](transactionpicker/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](transactionpicker/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase) -> Void) -> some View](transactionpicker/onscrollphasechange(_:)-9d11u.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase, ScrollPhaseChangeContext) -> Void) -> some View](transactionpicker/onscrollphasechange(_:)-9jw5q.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](transactionpicker/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](transactionpicker/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](transactionpicker/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](transactionpicker/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](transactionpicker/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func opacity(Double) -> some View](transactionpicker/opacity(_:).md)
  Sets the transparency of this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](transactionpicker/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](transactionpicker/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](transactionpicker/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](transactionpicker/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](transactionpicker/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](transactionpicker/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func padding(CGFloat) -> some View](transactionpicker/padding(_:)-1wrn.md)
  Adds a specific padding amount to each edge of this view.
- [func padding(EdgeInsets) -> some View](transactionpicker/padding(_:)-3rez6.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](transactionpicker/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](transactionpicker/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func persistentSystemOverlays(Visibility) -> some View](transactionpicker/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](transactionpicker/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](transactionpicker/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func pickerStyle<S>(S) -> some View](transactionpicker/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](transactionpicker/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](transactionpicker/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func position(CGPoint) -> some View](transactionpicker/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](transactionpicker/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func preference<K>(key: K.Type, value: K.Value) -> some View](transactionpicker/preference(key:value:).md)
  Sets a value for the given preference.
- [func preferredColorScheme(ColorScheme?) -> some View](transactionpicker/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func presentationBackground<S>(S) -> some View](transactionpicker/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](transactionpicker/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](transactionpicker/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](transactionpicker/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](transactionpicker/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](transactionpicker/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](transactionpicker/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationDetents(Set<PresentationDetent>) -> some View](transactionpicker/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](transactionpicker/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](transactionpicker/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationSizing(some PresentationSizing) -> some View](transactionpicker/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func previewContext<C>(C) -> some View](transactionpicker/previewcontext(_:).md)
  Declares a context for the preview.
- [func previewDevice(PreviewDevice?) -> some View](transactionpicker/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](transactionpicker/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](transactionpicker/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewLayout(PreviewLayout) -> some View](transactionpicker/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func privacySensitive(Bool) -> some View](transactionpicker/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func progressViewStyle<S>(S) -> some View](transactionpicker/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func projectionEffect(ProjectionTransform) -> some View](transactionpicker/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func redacted(reason: RedactionReasons) -> some View](transactionpicker/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func refreshable(action: () async -> Void) -> some View](transactionpicker/refreshable(action:).md)
  Marks this view as refreshable.
- [func renameAction(FocusState<Bool>.Binding) -> some View](transactionpicker/renameaction(_:)-2lqep.md)
  Sets the rename action in the environment to update focus state.
- [func renameAction(() -> Void) -> some View](transactionpicker/renameaction(_:)-7tfki.md)
  Sets a closure to run for the rename action.
- [func replaceDisabled(Bool) -> some View](transactionpicker/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](transactionpicker/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](transactionpicker/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](transactionpicker/safeareabar(edge:alignment:spacing:content:)-8qn43.md)
  Renders the provided content appropriate to be displayed as a custom bar.
- [func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> some View) -> some View](transactionpicker/safeareabar(edge:alignment:spacing:content:)-dst3.md)
  Renders the provided content appropriately to be displayed as a custom bar.
- [func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> V) -> some View](transactionpicker/safeareainset(edge:alignment:spacing:content:)-53edo.md)
  Shows the specified content above or below the modified view.
- [func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> V) -> some View](transactionpicker/safeareainset(edge:alignment:spacing:content:)-7rxp4.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(CGFloat) -> some View](transactionpicker/safeareapadding(_:)-1fucm.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(EdgeInsets) -> some View](transactionpicker/safeareapadding(_:)-7h4zf.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](transactionpicker/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func saturation(Double) -> some View](transactionpicker/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> some View](transactionpicker/scaleeffect(_:anchor:)-1795l.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](transactionpicker/scaleeffect(_:anchor:)-1ou4i.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](transactionpicker/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaledToFill() -> some View](transactionpicker/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](transactionpicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scenePadding(Edge.Set) -> some View](transactionpicker/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](transactionpicker/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](transactionpicker/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollClipDisabled(Bool) -> some View](transactionpicker/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func scrollContentBackground(Visibility) -> some View](transactionpicker/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollDisabled(Bool) -> some View](transactionpicker/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](transactionpicker/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](transactionpicker/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](transactionpicker/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](transactionpicker/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](transactionpicker/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](transactionpicker/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](transactionpicker/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](transactionpicker/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](transactionpicker/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](transactionpicker/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](transactionpicker/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](transactionpicker/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](transactionpicker/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [func searchCompletion(String) -> some View](transactionpicker/searchcompletion(_:)-62ljl.md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchCompletion<T>(T) -> some View](transactionpicker/searchcompletion(_:)-swh3.md)
  Associates a search token with the value of this view when used as a search suggestion.
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](transactionpicker/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](transactionpicker/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](transactionpicker/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](transactionpicker/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](transactionpicker/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](transactionpicker/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchSuggestions<S>(() -> S) -> some View](transactionpicker/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](transactionpicker/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](transactionpicker/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:ispresented:placement:prompt:token:)-5jgue.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:ispresented:placement:prompt:token:)-6y0ds.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:ispresented:placement:prompt:token:)-8j4tf.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:ispresented:placement:prompt:token:)-95hgj.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:placement:prompt:token:)-5d22c.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:placement:prompt:token:)-7bfh0.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:placement:prompt:token:)-7vdmb.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](transactionpicker/searchable(text:editabletokens:placement:prompt:token:)-s67r.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?) -> some View](transactionpicker/searchable(text:ispresented:placement:prompt:)-6q8t1.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S) -> some View](transactionpicker/searchable(text:ispresented:placement:prompt:)-6uzzy.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](transactionpicker/searchable(text:ispresented:placement:prompt:)-8x7p7.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](transactionpicker/searchable(text:ispresented:placement:prompt:)-yl3l.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](transactionpicker/searchable(text:placement:prompt:)-2jhjk.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](transactionpicker/searchable(text:placement:prompt:)-6i7wh.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](transactionpicker/searchable(text:placement:prompt:)-9ah5h.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringResource) -> some View](transactionpicker/searchable(text:placement:prompt:)-m0b0.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](transactionpicker/searchable(text:placement:prompt:suggestions:)-4o9uq.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](transactionpicker/searchable(text:placement:prompt:suggestions:)-6cnu9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](transactionpicker/searchable(text:placement:prompt:suggestions:)-8vz0i.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:ispresented:placement:prompt:token:)-17de.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:ispresented:placement:prompt:token:)-2dbkj.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:ispresented:placement:prompt:token:)-38uvw.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:ispresented:placement:prompt:token:)-7jomd.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:placement:prompt:token:)-6mwax.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:placement:prompt:token:)-72nmt.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:placement:prompt:token:)-82f69.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:placement:prompt:token:)-9hf60.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-3vi2t.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-42k77.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-7sf2e.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-88abu.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringResource, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-267gf.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-303vh.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-5a6rn.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](transactionpicker/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-7v2hs.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func sectionActions<Content>(content: () -> Content) -> some View](transactionpicker/sectionactions(content:).md)
  Adds custom actions to a section.
- [func sectionIndexLabel<S>(S?) -> some View](transactionpicker/sectionindexlabel(_:)-3q9pk.md)
  Sets the title that is used for the section index label pointing to this section, typically only a single character long.
- [func sectionIndexLabel(Text?) -> some View](transactionpicker/sectionindexlabel(_:)-6imtk.md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
- [func selectionDisabled(Bool) -> some View](transactionpicker/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](transactionpicker/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](transactionpicker/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [func sensoryFeedback<T>(trigger: T, () -> SensoryFeedback?) -> some View](transactionpicker/sensoryfeedback(trigger:_:)-4jhfw.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](transactionpicker/sensoryfeedback(trigger:_:)-8glfd.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](transactionpicker/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](transactionpicker/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](transactionpicker/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](transactionpicker/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](transactionpicker/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](transactionpicker/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func speechAdjustedPitch(Double) -> some View](transactionpicker/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](transactionpicker/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](transactionpicker/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](transactionpicker/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](transactionpicker/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [func statusBar(hidden: Bool) -> some View](transactionpicker/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func statusBarHidden(Bool) -> some View](transactionpicker/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](transactionpicker/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func submitLabel(SubmitLabel) -> some View](transactionpicker/submitlabel(_:).md)
  Sets the submit label for this view.
- [func submitScope(Bool) -> some View](transactionpicker/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](transactionpicker/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](transactionpicker/symbolcolorrenderingmode(_:).md)
  Sets the color rendering mode for symbol images.
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](transactionpicker/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](transactionpicker/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](transactionpicker/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](transactionpicker/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](transactionpicker/symbolvariablevaluemode(_:).md)
  Sets the variable value mode mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](transactionpicker/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](transactionpicker/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabItem<V>(() -> V) -> some View](transactionpicker/tabitem(_:).md)
  Sets the tab bar item associated with this view.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](transactionpicker/tabviewbottomaccessory(content:).md)
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](transactionpicker/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](transactionpicker/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](transactionpicker/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](transactionpicker/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewStyle<S>(S) -> some View](transactionpicker/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func tableColumnHeaders(Visibility) -> some View](transactionpicker/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func tableStyle<S>(S) -> some View](transactionpicker/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func tag<V>(V, includeOptional: Bool) -> some View](transactionpicker/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](transactionpicker/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](transactionpicker/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func textCase(Text.Case?) -> some View](transactionpicker/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textContentType(UITextContentType?) -> some View](transactionpicker/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textEditorStyle(some TextEditorStyle) -> some View](transactionpicker/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [func textFieldStyle<S>(S) -> some View](transactionpicker/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](transactionpicker/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](transactionpicker/textinputformattingcontrolvisibility(_:for:).md)
  Define which system text formatting controls are available.
- [func textRenderer<T>(T) -> some View](transactionpicker/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](transactionpicker/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textSelection<S>(S) -> some View](transactionpicker/textselection(_:).md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](transactionpicker/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tint(Color?) -> some View](transactionpicker/tint(_:).md)
  Sets the tint color within this view.
- [func toggleStyle<S>(S) -> some View](transactionpicker/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](transactionpicker/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar<Content>(content: () -> Content) -> some View](transactionpicker/toolbar(content:)-4jlsr.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(content: () -> Content) -> some View](transactionpicker/toolbar(content:)-7o3wz.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](transactionpicker/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](transactionpicker/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarbackground(_:for:)-9kgct.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarbackground(_:for:)-9xs98.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarRole(ToolbarRole) -> some View](transactionpicker/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](transactionpicker/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](transactionpicker/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](transactionpicker/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func tracking(CGFloat) -> some View](transactionpicker/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func transaction((inout Transaction) -> Void) -> some View](transactionpicker/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](transactionpicker/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](transactionpicker/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View](transactionpicker/transactionpicker(ispresented:selection:).md)
  Presents a picker that selects a collection of transactions.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](transactionpicker/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformEffect(CGAffineTransform) -> some View](transactionpicker/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](transactionpicker/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](transactionpicker/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func transition(AnyTransition) -> some View](transactionpicker/transition(_:)-b00.md)
  Associates a transition with the view.
- [func transition<T>(T) -> some View](transactionpicker/transition(_:)-lr3o.md)
  Associates a transition with the view.
- [func truncationMode(Text.TruncationMode) -> some View](transactionpicker/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typeSelectEquivalent(LocalizedStringResource) -> some View](transactionpicker/typeselectequivalent(_:)-2k5ll.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(Text?) -> some View](transactionpicker/typeselectequivalent(_:)-5bb5t.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent<S>(S) -> some View](transactionpicker/typeselectequivalent(_:)-64gw7.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringKey) -> some View](transactionpicker/typeselectequivalent(_:)-8e4zl.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View](transactionpicker/typesettinglanguage(_:isenabled:)-1tc5r.md)
  Specifies the language for typesetting.
- [func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View](transactionpicker/typesettinglanguage(_:isenabled:)-8z8e0.md)
  Specifies the language for typesetting.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](transactionpicker/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func unredacted() -> some View](transactionpicker/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](transactionpicker/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](transactionpicker/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](transactionpicker/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](transactionpicker/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](transactionpicker/writingdirection(strategy:).md)
  A modifier for the default text writing direction strategy in the view hierarchy.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](transactionpicker/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](transactionpicker/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [func zIndex(Double) -> some View](transactionpicker/zindex(_:).md)
  Controls the display order of overlapping views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/view-implementations)*