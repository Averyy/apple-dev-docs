# View Implementations

**Framework**: RealityKit

## Topics

### Instance Methods
- [func accentColor(Color?) -> some View](realityviewdefaultplaceholder/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(activationpoint:)-67zog.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(activationpoint:)-8asv2.md)
  Specifies the point where activations occur in the view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](realityviewdefaultplaceholder/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityaction(named:_:)-3cz2b.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityaction(named:_:)-3m3k3.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityaction(named:_:)-9nawr.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(() -> Content) -> some View](realityviewdefaultplaceholder/accessibilityactions(_:).md)
  Adds multiple accessibility actions to the view.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](realityviewdefaultplaceholder/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityactivationpoint(_:)-1rzlj.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityactivationpoint(_:)-9oqjp.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityactivationpoint(_:isenabled:)-46rm6.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityactivationpoint(_:isenabled:)-8peig.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityChartDescriptor<R>(R) -> some View](realityviewdefaultplaceholder/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
- [func accessibilityChildren<V>(children: () -> V) -> some View](realityviewdefaultplaceholder/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-23yxi.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-3cdxx.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-4s54s.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-5n6nh.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-5u90e.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-6mcy1.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-6z076.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitycustomcontent(_:_:importance:)-8fs26.md)
  Add additional accessibility information to the view.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:)-1hk4y.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:)-6ou72.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:)-7w9qg.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:isenabled:)-2npbn.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:isenabled:)-7zk9y.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydragpoint(_:description:isenabled:)-dtmi.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:)-10ydl.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:)-4d7gt.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:)-7tes.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint<S>(UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:isenabled:)-5lgxn.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:isenabled:)-8lvz8.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(UnitPoint, description: LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitydroppoint(_:description:isenabled:)-8xkr0.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](realityviewdefaultplaceholder/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](realityviewdefaultplaceholder/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](realityviewdefaultplaceholder/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHidden(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhidden(_:isenabled:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:)-252jq.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:)-3nlir.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:)-8o2l7.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:isenabled:)-2awy4.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:isenabled:)-5txqr.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityhint(_:isenabled:)-l1dx.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view.
- [func accessibilityIgnoresInvertColors(Bool) -> some View](realityviewdefaultplaceholder/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:)-3gr07.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:)-4owjc.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:)-83pfs.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:isenabled:)-9vhp8.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:isenabled:)-m3uu.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityinputlabels(_:isenabled:)-mxr3.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:)-4ddzg.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:)-4qzw1.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:)-7imqq.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:isenabled:)-13pk5.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:isenabled:)-2i3qj.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitylabel(_:isenabled:)-vdbv.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel<V>(content: (PlaceholderContentView<Self>) -> V) -> some View](realityviewdefaultplaceholder/accessibilitylabel(content:).md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](realityviewdefaultplaceholder/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](realityviewdefaultplaceholder/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](realityviewdefaultplaceholder/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRespondsToUserInteraction(Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityrespondstouserinteraction(_:isenabled:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:)-1edbf.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:)-1gl6b.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:)-3wb4f.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:)-5aohd.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entryid:entrylabel:)-4va8r.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entryid:entrylabel:)-57w8u.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entryid:entrylabel:)-5myem.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entryid:entrylabel:)-825xv.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entrylabel:)-2ffg6.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entrylabel:)-7j8nd.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entrylabel:)-97532.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:entries:entrylabel:)-9dp82.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:textranges:)-2bily.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:textranges:)-8cxlo.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:textranges:)-9e8br.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](realityviewdefaultplaceholder/accessibilityrotor(_:textranges:)-9rbqp.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](realityviewdefaultplaceholder/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityShowsLargeContentViewer() -> some View](realityviewdefaultplaceholder/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](realityviewdefaultplaceholder/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:)-1ge5b.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:)-7k73e.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:)-838tf.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue<S>(S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:isenabled:)-803fu.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:isenabled:)-81y8m.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityvalue(_:isenabled:)-950ra.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](realityviewdefaultplaceholder/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](realityviewdefaultplaceholder/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](realityviewdefaultplaceholder/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:)-7ow58.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:)-8zb6v.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:)-9jube.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:message:)-4cn6a.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:message:)-6a5lg.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:actions:message:)-6riyg.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:)-1r36n.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:)-3skv1.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:)-5vedj.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:message:)-4e30b.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:message:)-6nwqp.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/alert(_:ispresented:presenting:actions:message:)-9eai9.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](realityviewdefaultplaceholder/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](realityviewdefaultplaceholder/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](realityviewdefaultplaceholder/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](realityviewdefaultplaceholder/alert(item:content:).md)
  Presents an alert to the user.
- [func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](realityviewdefaultplaceholder/alignmentguide(_:computevalue:)-1b3dw.md)
  Sets the view’s horizontal alignment.
- [func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) -> CGFloat) -> some View](realityviewdefaultplaceholder/alignmentguide(_:computevalue:)-9n2i6.md)
  Sets the view’s vertical alignment.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](realityviewdefaultplaceholder/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
- [func allowsHitTesting(Bool) -> some View](realityviewdefaultplaceholder/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func allowsTightening(Bool) -> some View](realityviewdefaultplaceholder/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func allowsWindowActivationEvents(Bool?) -> some View](realityviewdefaultplaceholder/allowswindowactivationevents(_:).md)
  Configures whether gestures in this view hierarchy can handle events that activate the containing window.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](realityviewdefaultplaceholder/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](realityviewdefaultplaceholder/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func animation(Animation?) -> some View](realityviewdefaultplaceholder/animation(_:).md)
  Applies the given animation to all animatable values within this view.
- [func animation<V>(Animation?, body: (PlaceholderContentView<Self>) -> V) -> some View](realityviewdefaultplaceholder/animation(_:body:).md)
  Applies the given animation to all animatable values within the `body` closure.
- [func animation<V>(Animation?, value: V) -> some View](realityviewdefaultplaceholder/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func aspectRatio(CGFloat?, contentMode: ContentMode) -> some View](realityviewdefaultplaceholder/aspectratio(_:contentmode:)-2po6a.md)
  Constrains this view’s dimensions to the specified aspect ratio.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](realityviewdefaultplaceholder/aspectratio(_:contentmode:)-7uq0a.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](realityviewdefaultplaceholder/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func autocorrectionDisabled(Bool) -> some View](realityviewdefaultplaceholder/autocorrectiondisabled(_:).md)
  Sets whether to disable autocorrection for this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](realityviewdefaultplaceholder/background(_:alignment:).md)
  Layers the given view behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](realityviewdefaultplaceholder/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](realityviewdefaultplaceholder/background(_:in:fillstyle:)-30vt.md)
  Sets the view’s background to a shape filled with a style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](realityviewdefaultplaceholder/background(_:in:fillstyle:)-8dp8v.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](realityviewdefaultplaceholder/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](realityviewdefaultplaceholder/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](realityviewdefaultplaceholder/background(in:fillstyle:)-2qb0d.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](realityviewdefaultplaceholder/background(in:fillstyle:)-6xqqg.md)
  Sets the view’s background to a shape filled with the default background style.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](realityviewdefaultplaceholder/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](realityviewdefaultplaceholder/backgroundpreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func backgroundStyle<S>(S) -> some View](realityviewdefaultplaceholder/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func badge(Int) -> some View](realityviewdefaultplaceholder/badge(_:)-2oain.md)
  Generates a badge for the view from an integer value.
- [func badge<S>(S?) -> some View](realityviewdefaultplaceholder/badge(_:)-5b59a.md)
  Generates a badge for the view from a string.
- [func badge(LocalizedStringKey?) -> some View](realityviewdefaultplaceholder/badge(_:)-6j8f0.md)
  Generates a badge for the view from a localized string key.
- [func badge(Text?) -> some View](realityviewdefaultplaceholder/badge(_:)-eb98.md)
  Generates a badge for the view from a text view.
- [func badgeProminence(BadgeProminence) -> some View](realityviewdefaultplaceholder/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [func baselineOffset(CGFloat) -> some View](realityviewdefaultplaceholder/baselineoffset(_:).md)
  Sets the vertical offset for the text relative to its baseline in this view.
- [func blendMode(BlendMode) -> some View](realityviewdefaultplaceholder/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func blur(radius: CGFloat, opaque: Bool) -> some View](realityviewdefaultplaceholder/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func bold(Bool) -> some View](realityviewdefaultplaceholder/bold(_:).md)
  Applies a bold font weight to the text in this view.
- [func border<S>(S, width: CGFloat) -> some View](realityviewdefaultplaceholder/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func brightness(Double) -> some View](realityviewdefaultplaceholder/brightness(_:).md)
  Brightens this view by the specified amount.
- [func buttonBorderShape(ButtonBorderShape) -> some View](realityviewdefaultplaceholder/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](realityviewdefaultplaceholder/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func buttonStyle<S>(S) -> some View](realityviewdefaultplaceholder/buttonstyle(_:)-12pa7.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonStyle<S>(S) -> some View](realityviewdefaultplaceholder/buttonstyle(_:)-69ub6.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func clipShape<S>(S, style: FillStyle) -> some View](realityviewdefaultplaceholder/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func clipped(antialiased: Bool) -> some View](realityviewdefaultplaceholder/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func colorEffect(Shader, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/coloreffect(_:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [func colorInvert() -> some View](realityviewdefaultplaceholder/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](realityviewdefaultplaceholder/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func colorScheme(ColorScheme) -> some View](realityviewdefaultplaceholder/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func compositingGroup() -> some View](realityviewdefaultplaceholder/compositinggroup.md)
  Wraps this view in a compositing group.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:)-1v48z.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:)-5uccq.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:)-66nvt.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-4qcxk.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-9fy2e.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-uy4z.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-7se5b.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-9nqux.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-n01y.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-3jfkm.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-7k8gq.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](realityviewdefaultplaceholder/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-9jayd.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](realityviewdefaultplaceholder/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](realityviewdefaultplaceholder/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](realityviewdefaultplaceholder/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](realityviewdefaultplaceholder/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](realityviewdefaultplaceholder/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerShape<T>(T) -> some View](realityviewdefaultplaceholder/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](realityviewdefaultplaceholder/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some View](realityviewdefaultplaceholder/contentmargins(_:_:for:)-60oqw.md)
  Configures the content margin for a provided placement.
- [func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) -> some View](realityviewdefaultplaceholder/contentmargins(_:_:for:)-6qkbd.md)
  Configures the content margin for a provided placement.
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](realityviewdefaultplaceholder/contentmargins(_:for:).md)
  Configures the content margin for a provided placement.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](realityviewdefaultplaceholder/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [func contentShape<S>(S, eoFill: Bool) -> some View](realityviewdefaultplaceholder/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](realityviewdefaultplaceholder/contenttoolbar(for:content:)-56a2s.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentToolbar<Content>(for: ContentToolbarPlacement, content: () -> Content) -> some View](realityviewdefaultplaceholder/contenttoolbar(for:content:)-9ra6p.md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func contentTransition(ContentTransition) -> some View](realityviewdefaultplaceholder/contenttransition(_:).md)
  Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](realityviewdefaultplaceholder/contextmenu(_:).md)
  Adds a context menu to the view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](realityviewdefaultplaceholder/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](realityviewdefaultplaceholder/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](realityviewdefaultplaceholder/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contrast(Double) -> some View](realityviewdefaultplaceholder/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func controlGroupStyle<S>(S) -> some View](realityviewdefaultplaceholder/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func controlSize(ControlSize) -> some View](realityviewdefaultplaceholder/controlsize(_:).md)
  Sets the size for controls within this view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](realityviewdefaultplaceholder/coordinatespace(_:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func coordinateSpace<T>(name: T) -> some View](realityviewdefaultplaceholder/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [func copyable<T>(@autoclosure () -> [T]) -> some View](realityviewdefaultplaceholder/copyable(_:).md)
  Specifies a list of items to copy in response to the system’s Copy command.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](realityviewdefaultplaceholder/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func cuttable<T>(for: T.Type, action: () -> [T]) -> some View](realityviewdefaultplaceholder/cuttable(for:action:).md)
  Specifies an action that moves items to the Clipboard in response to the system’s Cut command.
- [func datePickerStyle<S>(S) -> some View](realityviewdefaultplaceholder/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](realityviewdefaultplaceholder/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultAppStorage(UserDefaults) -> some View](realityviewdefaultplaceholder/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
- [func defaultFocus<V>(FocusState<V>.Binding, V, priority: DefaultFocusEvaluationPriority) -> some View](realityviewdefaultplaceholder/defaultfocus(_:_:priority:).md)
  Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.
- [func defaultHoverEffect(HoverEffect?) -> some View](realityviewdefaultplaceholder/defaulthovereffect(_:)-1e885.md)
  Sets the default hover effect to use for views within this view.
- [func defaultHoverEffect(some CustomHoverEffect) -> some View](realityviewdefaultplaceholder/defaulthovereffect(_:)-ypwf.md)
  Sets the default hover effect to use within this view hierarchy.
- [func defaultScrollAnchor(UnitPoint?) -> some View](realityviewdefaultplaceholder/defaultscrollanchor(_:).md)
  Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [func defaultScrollAnchor(UnitPoint?, for: ScrollAnchorRole) -> some View](realityviewdefaultplaceholder/defaultscrollanchor(_:for:).md)
  Associates an anchor to control the position of a scroll view in a particular circumstance.
- [func defersSystemGestures(on: Edge.Set) -> some View](realityviewdefaultplaceholder/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [func deleteDisabled(Bool) -> some View](realityviewdefaultplaceholder/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
- [func dialogIcon(Image?) -> some View](realityviewdefaultplaceholder/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogPreventsAppTermination(Bool?) -> some View](realityviewdefaultplaceholder/dialogpreventsapptermination(_:).md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
- [func dialogSeverity(DialogSeverity) -> some View](realityviewdefaultplaceholder/dialogseverity(_:).md)
- [func dialogSuppressionToggle(Text, isSuppressed: Binding<Bool>) -> some View](realityviewdefaultplaceholder/dialogsuppressiontoggle(_:issuppressed:)-1o62v.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(LocalizedStringKey, isSuppressed: Binding<Bool>) -> some View](realityviewdefaultplaceholder/dialogsuppressiontoggle(_:issuppressed:)-3mpem.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle<S>(S, isSuppressed: Binding<Bool>) -> some View](realityviewdefaultplaceholder/dialogsuppressiontoggle(_:issuppressed:)-4sek3.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](realityviewdefaultplaceholder/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func disableAutocorrection(Bool?) -> some View](realityviewdefaultplaceholder/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func disabled(Bool) -> some View](realityviewdefaultplaceholder/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func disclosureGroupStyle<S>(S) -> some View](realityviewdefaultplaceholder/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [func dismissalConfirmationDialog<S, A>(S, shouldPresent: Bool, actions: () -> A) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:)-3fkjp.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:)-4w02f.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A>(Text, shouldPresent: Bool, actions: () -> A) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:)-75lj7.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<S, A, M>(S, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-104t8.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(LocalizedStringKey, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-33ifp.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func dismissalConfirmationDialog<A, M>(Text, shouldPresent: Bool, actions: () -> A, message: () -> M) -> some View](realityviewdefaultplaceholder/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-55dvf.md)
  Presents a confirmation dialog when a dismiss action has been triggered.
- [func distortionEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/distortioneffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](realityviewdefaultplaceholder/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func draggable<T>(@autoclosure () -> T) -> some View](realityviewdefaultplaceholder/draggable(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func draggable<V, T>(@autoclosure () -> T, preview: () -> V) -> some View](realityviewdefaultplaceholder/draggable(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](realityviewdefaultplaceholder/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [func dropDestination<T>(for: T.Type, action: ([T], CGPoint) -> Bool, isTargeted: (Bool) -> Void) -> some View](realityviewdefaultplaceholder/dropdestination(for:action:istargeted:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func dynamicTypeSize<T>(T) -> some View](realityviewdefaultplaceholder/dynamictypesize(_:)-4gkxt.md)
  Limits the Dynamic Type size within the view to the given range.
- [func dynamicTypeSize(DynamicTypeSize) -> some View](realityviewdefaultplaceholder/dynamictypesize(_:)-fqe1.md)
  Sets the Dynamic Type size within the view to the given value.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](realityviewdefaultplaceholder/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func environment<T>(T?) -> some View](realityviewdefaultplaceholder/environment(_:).md)
  Places an observable object in the view’s environment.
- [func environment<V>(WritableKeyPath<EnvironmentValues, V>, V) -> some View](realityviewdefaultplaceholder/environment(_:_:).md)
  Sets the environment value of the specified key path to the given value.
- [func environmentObject<T>(T) -> some View](realityviewdefaultplaceholder/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](realityviewdefaultplaceholder/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](realityviewdefaultplaceholder/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](realityviewdefaultplaceholder/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](realityviewdefaultplaceholder/exportsitemproviders(_:onexport:onedit:).md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](realityviewdefaultplaceholder/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/filedialogconfirmationlabel(_:)-5viiy.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogConfirmationLabel(Text?) -> some View](realityviewdefaultplaceholder/filedialogconfirmationlabel(_:)-740b8.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogConfirmationLabel<S>(S) -> some View](realityviewdefaultplaceholder/filedialogconfirmationlabel(_:)-j8c5.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](realityviewdefaultplaceholder/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](realityviewdefaultplaceholder/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](realityviewdefaultplaceholder/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage<S>(S) -> some View](realityviewdefaultplaceholder/filedialogmessage(_:)-1nzog.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/filedialogmessage(_:)-2f6tb.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogMessage(Text?) -> some View](realityviewdefaultplaceholder/filedialogmessage(_:)-9n3k7.md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](realityviewdefaultplaceholder/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-44r1r.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-5rgd8.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-5ybo2.md)
  Presents a system dialog for allowing the user to export a `ReferenceFileDocument` to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)-9z456.md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:documents:contenttype:oncompletion:)-8qkj9.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:documents:contenttype:oncompletion:)-9vvjt.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-6hptl.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `ReferenceFileDocument` to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)-9amr2.md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/fileexporterfilenamelabel(_:)-7g5nn.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel<S>(S) -> some View](realityviewdefaultplaceholder/fileexporterfilenamelabel(_:)-9fhpj.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
- [func fileExporterFilenameLabel(Text?) -> some View](realityviewdefaultplaceholder/fileexporterfilenamelabel(_:)-9lhul.md)
  On macOS, configures the `fileExporter` with a text to use as a label for the file name field.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](realityviewdefaultplaceholder/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](realityviewdefaultplaceholder/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](realityviewdefaultplaceholder/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](realityviewdefaultplaceholder/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func findDisabled(Bool) -> some View](realityviewdefaultplaceholder/finddisabled(_:).md)
  Prevents find and replace operations in a text editor.
- [func findNavigator(isPresented: Binding<Bool>) -> some View](realityviewdefaultplaceholder/findnavigator(ispresented:).md)
  Programmatically presents the find and replace interface for text editor views.
- [func fixedSize() -> some View](realityviewdefaultplaceholder/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](realityviewdefaultplaceholder/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](realityviewdefaultplaceholder/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [func focusEffectDisabled(Bool) -> some View](realityviewdefaultplaceholder/focuseffectdisabled(_:).md)
  Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
- [func focusScope(Namespace.ID) -> some View](realityviewdefaultplaceholder/focusscope(_:).md)
  Creates a focus scope that SwiftUI uses to limit default focus preferences.
- [func focusSection() -> some View](realityviewdefaultplaceholder/focussection.md)
  Indicates that the view’s frame and cohort of focusable descendants should be used to guide focus movement.
- [func focusable(Bool) -> some View](realityviewdefaultplaceholder/focusable(_:).md)
  Specifies if the view is focusable.
- [func focusable(Bool, interactions: FocusInteractions) -> some View](realityviewdefaultplaceholder/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [func focusable(Bool, onFocusChange: (Bool) -> Void) -> some View](realityviewdefaultplaceholder/focusable(_:onfocuschange:).md)
  Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.
- [func focused(FocusState<Bool>.Binding) -> some View](realityviewdefaultplaceholder/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](realityviewdefaultplaceholder/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focusedObject<T>(T) -> some View](realityviewdefaultplaceholder/focusedobject(_:)-2lzkm.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the focused view hierarchy.
- [func focusedObject<T>(T?) -> some View](realityviewdefaultplaceholder/focusedobject(_:)-8tday.md)
  Creates a new view that exposes the provided object to other views whose state depends on the focused view hierarchy.
- [func focusedSceneObject<T>(T?) -> some View](realityviewdefaultplaceholder/focusedsceneobject(_:)-29j59.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneObject<T>(T) -> some View](realityviewdefaultplaceholder/focusedsceneobject(_:)-4q34f.md)
  Creates a new view that exposes the provided object to other views whose whose state depends on the active scene.
- [func focusedSceneValue<T>(T?) -> some View](realityviewdefaultplaceholder/focusedscenevalue(_:).md)
  Sets the focused value for the given object type at a scene-wide scope.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T) -> some View](realityviewdefaultplaceholder/focusedscenevalue(_:_:)-3emju.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused scene.
- [func focusedSceneValue<T>(WritableKeyPath<FocusedValues, T?>, T?) -> some View](realityviewdefaultplaceholder/focusedscenevalue(_:_:)-5ucsc.md)
  Creates a new view that exposes the provided value to other views whose state depends on the active scene.
- [func focusedValue<T>(T?) -> some View](realityviewdefaultplaceholder/focusedvalue(_:).md)
  Sets the focused value for the given object type.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value?) -> some View](realityviewdefaultplaceholder/focusedvalue(_:_:)-29zpw.md)
  Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.
- [func focusedValue<Value>(WritableKeyPath<FocusedValues, Value?>, Value) -> some View](realityviewdefaultplaceholder/focusedvalue(_:_:)-3wpd1.md)
  Modifies this view by injecting a value that you provide for use by other views whose state depends on the focused view hierarchy.
- [func font(Font?) -> some View](realityviewdefaultplaceholder/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](realityviewdefaultplaceholder/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](realityviewdefaultplaceholder/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](realityviewdefaultplaceholder/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [func foregroundColor(Color?) -> some View](realityviewdefaultplaceholder/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func foregroundStyle<S>(S) -> some View](realityviewdefaultplaceholder/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](realityviewdefaultplaceholder/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](realityviewdefaultplaceholder/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func formStyle<S>(S) -> some View](realityviewdefaultplaceholder/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func frame() -> some View](realityviewdefaultplaceholder/frame.md)
  Positions this view within an invisible frame.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](realityviewdefaultplaceholder/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](realityviewdefaultplaceholder/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](realityviewdefaultplaceholder/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](realityviewdefaultplaceholder/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](realityviewdefaultplaceholder/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](realityviewdefaultplaceholder/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func gaugeStyle<S>(S) -> some View](realityviewdefaultplaceholder/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func geometryGroup() -> some View](realityviewdefaultplaceholder/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.
- [func gesture(some UIGestureRecognizerRepresentable) -> some View](realityviewdefaultplaceholder/gesture(_:).md)
  Attaches a `UIGestureRecognizerRepresentable` to the view.
- [func gesture<T>(T, including: GestureMask) -> some View](realityviewdefaultplaceholder/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](realityviewdefaultplaceholder/glassbackgroundeffect(_:displaymode:).md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](realityviewdefaultplaceholder/glassbackgroundeffect(_:in:displaymode:).md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](realityviewdefaultplaceholder/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](realityviewdefaultplaceholder/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func grayscale(Double) -> some View](realityviewdefaultplaceholder/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func gridCellAnchor(UnitPoint) -> some View](realityviewdefaultplaceholder/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellColumns(Int) -> some View](realityviewdefaultplaceholder/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](realityviewdefaultplaceholder/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](realityviewdefaultplaceholder/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.
- [func groupBoxStyle<S>(S) -> some View](realityviewdefaultplaceholder/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](realityviewdefaultplaceholder/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](realityviewdefaultplaceholder/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
- [func headerProminence(Prominence) -> some View](realityviewdefaultplaceholder/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func help(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/help(_:)-1pr2j.md)
  Adds help text to a view using a localized string that you provide.
- [func help<S>(S) -> some View](realityviewdefaultplaceholder/help(_:)-5iejc.md)
  Adds help text to a view using a string that you provide.
- [func help(Text) -> some View](realityviewdefaultplaceholder/help(_:)-a449.md)
  Adds help text to a view using a text view that you provide.
- [func hidden() -> some View](realityviewdefaultplaceholder/hidden.md)
  Hides this view unconditionally.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](realityviewdefaultplaceholder/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func horizontalRadioGroupLayout() -> some View](realityviewdefaultplaceholder/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func hoverEffect(HoverEffect) -> some View](realityviewdefaultplaceholder/hovereffect(_:).md)
  Applies a hover effect to this view.
- [func hoverEffect(some CustomHoverEffect, in: HoverEffectGroup?, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/hovereffect(_:in:isenabled:).md)
  Applies a hover effect to this view, optionally adding it to a `HoverEffectGroup`.
- [func hoverEffect(HoverEffect, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffect(in: HoverEffectGroup?, isEnabled: Bool, body: (EmptyHoverEffectContent, Bool, GeometryProxy) -> some HoverEffectContent) -> some View](realityviewdefaultplaceholder/hovereffect(in:isenabled:body:).md)
  Applies a hover effect to this view described by the given closure.
- [func hoverEffectDisabled(Bool) -> some View](realityviewdefaultplaceholder/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func hoverEffectGroup() -> some View](realityviewdefaultplaceholder/hovereffectgroup.md)
  Adds an implicit `HoverEffectGroup` to all effects defined on descendant views, so that all effects added to subviews activate as a group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(HoverEffectGroup?) -> some View](realityviewdefaultplaceholder/hovereffectgroup(_:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hoverEffectGroup(id: String?, in: Namespace.ID, behavior: HoverEffectGroup.Behavior) -> some View](realityviewdefaultplaceholder/hovereffectgroup(id:in:behavior:).md)
  Adds a `HoverEffectGroup` to all effects defined on descendant views, and activates the group whenever this view or any descendant views are hovered.
- [func hueRotation(Angle) -> some View](realityviewdefaultplaceholder/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func id<ID>(ID) -> some View](realityviewdefaultplaceholder/id(_:).md)
  Binds a view’s identity to the given proxy value.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](realityviewdefaultplaceholder/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func imageScale(Image.Scale) -> some View](realityviewdefaultplaceholder/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](realityviewdefaultplaceholder/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](realityviewdefaultplaceholder/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func indexViewStyle<S>(S) -> some View](realityviewdefaultplaceholder/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](realityviewdefaultplaceholder/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](realityviewdefaultplaceholder/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](realityviewdefaultplaceholder/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
- [func interactionActivityTrackingTag(String) -> some View](realityviewdefaultplaceholder/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func interactiveDismissDisabled(Bool) -> some View](realityviewdefaultplaceholder/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func invalidatableContent(Bool) -> some View](realityviewdefaultplaceholder/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
- [func italic(Bool) -> some View](realityviewdefaultplaceholder/italic(_:).md)
  Applies italics to the text in this view.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](realityviewdefaultplaceholder/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func kerning(CGFloat) -> some View](realityviewdefaultplaceholder/kerning(_:).md)
  Sets the spacing, or kerning, between characters for the text in this view.
- [func keyboardShortcut(KeyboardShortcut?) -> some View](realityviewdefaultplaceholder/keyboardshortcut(_:)-5fqme.md)
  Assigns an optional keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyboardShortcut) -> some View](realityviewdefaultplaceholder/keyboardshortcut(_:)-7n2r6.md)
  Assigns a keyboard shortcut to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](realityviewdefaultplaceholder/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](realityviewdefaultplaceholder/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardType(UIKeyboardType) -> some View](realityviewdefaultplaceholder/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func keyframeAnimator<Value>(initialValue: Value, repeating: Bool, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](realityviewdefaultplaceholder/keyframeanimator(initialvalue:repeating:content:keyframes:).md)
  Loops the given keyframes continuously, updating the view using the modifiers you apply in `body`.
- [func keyframeAnimator<Value>(initialValue: Value, trigger: some Equatable, content: (PlaceholderContentView<Self>, Value) -> some View, keyframes: (Value) -> some Keyframes) -> some View](realityviewdefaultplaceholder/keyframeanimator(initialvalue:trigger:content:keyframes:).md)
  Plays the given keyframes when the given trigger value changes, updating the view using the modifiers you apply in `body`.
- [func labelStyle<S>(S) -> some View](realityviewdefaultplaceholder/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func labeledContentStyle<S>(S) -> some View](realityviewdefaultplaceholder/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsHidden() -> some View](realityviewdefaultplaceholder/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](realityviewdefaultplaceholder/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func layerEffect(Shader, maxSampleOffset: CGSize, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/layereffect(_:maxsampleoffset:isenabled:).md)
  Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View](realityviewdefaultplaceholder/layoutdirectionbehavior(_:).md)
  Sets the behavior of this view for different layout directions.
- [func layoutPriority(Double) -> some View](realityviewdefaultplaceholder/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
- [func layoutValue<K>(key: K.Type, value: K.Value) -> some View](realityviewdefaultplaceholder/layoutvalue(key:value:).md)
  Associates a value with a custom layout property.
- [func lineLimit(Int?) -> some View](realityviewdefaultplaceholder/linelimit(_:)-15lwr.md)
  Sets the maximum number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeThrough<Int>) -> some View](realityviewdefaultplaceholder/linelimit(_:)-39e50.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(ClosedRange<Int>) -> some View](realityviewdefaultplaceholder/linelimit(_:)-3o0be.md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(PartialRangeFrom<Int>) -> some View](realityviewdefaultplaceholder/linelimit(_:)-9v2l7.md)
  Sets to a partial range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](realityviewdefaultplaceholder/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](realityviewdefaultplaceholder/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func listItemTint(ListItemTint?) -> some View](realityviewdefaultplaceholder/listitemtint(_:)-2ri2c.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](realityviewdefaultplaceholder/listitemtint(_:)-7twjc.md)
  Sets a fixed tint color for content in a list.
- [func listRowBackground<V>(V?) -> some View](realityviewdefaultplaceholder/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func listRowHoverEffect(HoverEffect?) -> some View](realityviewdefaultplaceholder/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](realityviewdefaultplaceholder/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [func listRowInsets(EdgeInsets?) -> some View](realityviewdefaultplaceholder/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](realityviewdefaultplaceholder/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](realityviewdefaultplaceholder/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSpacing(CGFloat?) -> some View](realityviewdefaultplaceholder/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](realityviewdefaultplaceholder/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](realityviewdefaultplaceholder/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSpacing(CGFloat) -> some View](realityviewdefaultplaceholder/listsectionspacing(_:)-4qu5b.md)
  Sets the spacing between adjacent sections in a `List` to a custom value.
- [func listSectionSpacing(ListSectionSpacing) -> some View](realityviewdefaultplaceholder/listsectionspacing(_:)-6pr4.md)
  Sets the spacing between adjacent sections in a `List`.
- [func listStyle<S>(S) -> some View](realityviewdefaultplaceholder/liststyle(_:).md)
  Sets the style for lists within this view.
- [func luminanceToAlpha() -> some View](realityviewdefaultplaceholder/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func mask<Mask>(Mask) -> some View](realityviewdefaultplaceholder/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](realityviewdefaultplaceholder/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](realityviewdefaultplaceholder/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](realityviewdefaultplaceholder/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](realityviewdefaultplaceholder/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](realityviewdefaultplaceholder/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](realityviewdefaultplaceholder/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func menuButtonStyle<S>(S) -> some View](realityviewdefaultplaceholder/menubuttonstyle(_:).md)
  Sets the style for menu buttons within this view.
- [func menuIndicator(Visibility) -> some View](realityviewdefaultplaceholder/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func menuOrder(MenuOrder) -> some View](realityviewdefaultplaceholder/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuStyle<S>(S) -> some View](realityviewdefaultplaceholder/menustyle(_:).md)
  Sets the style for menus within this view.
- [func minimumScaleFactor(CGFloat) -> some View](realityviewdefaultplaceholder/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](realityviewdefaultplaceholder/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [func modifierKeyAlternate<V>(EventModifiers, () -> V) -> some View](realityviewdefaultplaceholder/modifierkeyalternate(_:_:).md)
  Builds a view to use in place of the modified view when the user presses the modifier key(s) indicated by the given set.
- [func monospaced(Bool) -> some View](realityviewdefaultplaceholder/monospaced(_:).md)
  Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> some View](realityviewdefaultplaceholder/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func moveDisabled(Bool) -> some View](realityviewdefaultplaceholder/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
- [func multilineTextAlignment(TextAlignment) -> some View](realityviewdefaultplaceholder/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
- [func navigationBarBackButtonHidden(Bool) -> some View](realityviewdefaultplaceholder/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarHidden(Bool) -> some View](realityviewdefaultplaceholder/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](realityviewdefaultplaceholder/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](realityviewdefaultplaceholder/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](realityviewdefaultplaceholder/navigationbaritems(trailing:).md)
- [func navigationBarTitle(Text) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:)-32y0.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:)-664z0.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle<S>(S) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:)-889xr.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:displaymode:)-3pcuq.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:displaymode:)-8h601.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](realityviewdefaultplaceholder/navigationbartitle(_:displaymode:)-8i9u9.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](realityviewdefaultplaceholder/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](realityviewdefaultplaceholder/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](realityviewdefaultplaceholder/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](realityviewdefaultplaceholder/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationDocument(URL) -> some View](realityviewdefaultplaceholder/navigationdocument(_:)-47gk0.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D) -> some View](realityviewdefaultplaceholder/navigationdocument(_:)-69c7z.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<I, Never>) -> some View](realityviewdefaultplaceholder/navigationdocument(_:preview:)-1kwii.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I>(D, preview: SharePreview<Never, I>) -> some View](realityviewdefaultplaceholder/navigationdocument(_:preview:)-24bqg.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D>(D, preview: SharePreview<Never, Never>) -> some View](realityviewdefaultplaceholder/navigationdocument(_:preview:)-6tydj.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument<D, I1, I2>(D, preview: SharePreview<I1, I2>) -> some View](realityviewdefaultplaceholder/navigationdocument(_:preview:)-7taxd.md)
  Configures the view’s document for purposes of navigation.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](realityviewdefaultplaceholder/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](realityviewdefaultplaceholder/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationSplitViewStyle<S>(S) -> some View](realityviewdefaultplaceholder/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSubtitle(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/navigationsubtitle(_:)-4mgkj.md)
  Configures the view’s subtitle for purposes of navigation, using a localized string.
- [func navigationSubtitle(Text) -> some View](realityviewdefaultplaceholder/navigationsubtitle(_:)-57lln.md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationSubtitle<S>(S) -> some View](realityviewdefaultplaceholder/navigationsubtitle(_:)-6e3h8.md)
  Configures the view’s subtitle for purposes of navigation, using a string.
- [func navigationTitle(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/navigationtitle(_:)-1yokj.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle(Text) -> some View](realityviewdefaultplaceholder/navigationtitle(_:)-2vil5.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTitle(Binding<String>) -> some View](realityviewdefaultplaceholder/navigationtitle(_:)-662w.md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationTitle<V>(() -> V) -> some View](realityviewdefaultplaceholder/navigationtitle(_:)-7qni0.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle<S>(S) -> some View](realityviewdefaultplaceholder/navigationtitle(_:)-81bay.md)
  Configures the view’s title for purposes of navigation, using a string.
- [func navigationTransition(some NavigationTransition) -> some View](realityviewdefaultplaceholder/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func navigationViewStyle<S>(S) -> some View](realityviewdefaultplaceholder/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func offset(CGSize) -> some View](realityviewdefaultplaceholder/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](realityviewdefaultplaceholder/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func offset(z: CGFloat) -> some View](realityviewdefaultplaceholder/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.
- [func onAppear(perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, initial: Bool, () -> Void) -> some View](realityviewdefaultplaceholder/onchange(of:initial:_:)-50gzo.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, initial: Bool, (V, V) -> Void) -> some View](realityviewdefaultplaceholder/onchange(of:initial:_:)-5y6lj.md)
  Adds a modifier for this view that fires an action when a specific value changes.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](realityviewdefaultplaceholder/onchange(of:perform:).md)
  Performs an action when a specified value changes.
- [func onCommand(Selector, perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/oncommand(_:perform:).md)
  Adds an action to perform in response to the given selector.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](realityviewdefaultplaceholder/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
- [func onContinuousHover(coordinateSpace: CoordinateSpace, perform: (HoverPhase) -> Void) -> some View](realityviewdefaultplaceholder/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](realityviewdefaultplaceholder/oncopycommand(perform:).md)
  Adds an action to perform in response to the system’s Copy command.
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](realityviewdefaultplaceholder/oncutcommand(perform:).md)
  Adds an action to perform in response to the system’s Cut command.
- [func onDeleteCommand(perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/ondeletecommand(perform:).md)
  Adds an action to perform in response to the system’s Delete command, or pressing either the ⌫ (backspace) or ⌦ (forward delete) keys while the view has focus.
- [func onDisappear(perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onDrag(() -> NSItemProvider) -> some View](realityviewdefaultplaceholder/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](realityviewdefaultplaceholder/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](realityviewdefaultplaceholder/ondrop(of:delegate:)-7r23h.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](realityviewdefaultplaceholder/ondrop(of:delegate:)-7wjnv.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](realityviewdefaultplaceholder/ondrop(of:istargeted:perform:)-1opt9.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](realityviewdefaultplaceholder/ondrop(of:istargeted:perform:)-1u6vx.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](realityviewdefaultplaceholder/ondrop(of:istargeted:perform:)-5kahv.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](realityviewdefaultplaceholder/ondrop(of:istargeted:perform:)-84tfg.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
- [func onExitCommand(perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/onexitcommand(perform:).md)
  Sets up an action that triggers in response to receiving the exit command while the view has focus.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T) -> Void) -> some View](realityviewdefaultplaceholder/ongeometrychange(for:of:action:)-3z98q.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange<T>(for: T.Type, of: (GeometryProxy) -> T, action: (T, T) -> Void) -> some View](realityviewdefaultplaceholder/ongeometrychange(for:of:action:)-4bmtp.md)
  Adds an action to be performed when a value, created from a geometry proxy, changes.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T) -> Void) -> some View](realityviewdefaultplaceholder/ongeometrychange3d(for:of:action:)-4bl4p.md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onGeometryChange3D<T>(for: T.Type, of: (GeometryProxy3D) -> T, action: (T, T) -> Void) -> some View](realityviewdefaultplaceholder/ongeometrychange3d(for:of:action:)-5vouu.md)
  Returns a new view that arranges to call `action(oldValue, newValue)` whenever the value computed by `value(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onHover(perform: (Bool) -> Void) -> some View](realityviewdefaultplaceholder/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](realityviewdefaultplaceholder/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func onKeyPress(KeyEquivalent, action: () -> KeyPress.Result) -> some View](realityviewdefaultplaceholder/onkeypress(_:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(KeyEquivalent, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](realityviewdefaultplaceholder/onkeypress(_:phases:action:).md)
  Performs an action if the user presses a key on a hardware keyboard while the view has focus.
- [func onKeyPress(characters: CharacterSet, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](realityviewdefaultplaceholder/onkeypress(characters:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(keys: Set<KeyEquivalent>, phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](realityviewdefaultplaceholder/onkeypress(keys:phases:action:).md)
  Performs an action if the user presses one or more keys on a hardware keyboard while the view has focus.
- [func onKeyPress(phases: KeyPress.Phases, action: (KeyPress) -> KeyPress.Result) -> some View](realityviewdefaultplaceholder/onkeypress(phases:action:).md)
  Performs an action if the user presses any key on a hardware keyboard while the view has focus.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](realityviewdefaultplaceholder/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](realityviewdefaultplaceholder/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](realityviewdefaultplaceholder/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](realityviewdefaultplaceholder/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onModifierKeysChanged(mask: EventModifiers, initial: Bool, (EventModifiers, EventModifiers) -> Void) -> some View](realityviewdefaultplaceholder/onmodifierkeyschanged(mask:initial:_:).md)
  Performs an action whenever the user presses or releases a hardware modifier key.
- [func onMoveCommand(perform: ((MoveCommandDirection) -> Void)?) -> some View](realityviewdefaultplaceholder/onmovecommand(perform:).md)
  Adds an action to perform in response to a move command, like when the user presses an arrow key on a Mac keyboard, or taps the edge of the Siri Remote when controlling an Apple TV.
- [func onOpenURL(perform: (URL) -> ()) -> some View](realityviewdefaultplaceholder/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
- [func onPasteCommand(of: [String], perform: ([NSItemProvider]) -> Void) -> some View](realityviewdefaultplaceholder/onpastecommand(of:perform:)-4itmz.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of: [UTType], perform: ([NSItemProvider]) -> Void) -> some View](realityviewdefaultplaceholder/onpastecommand(of:perform:)-8jrmc.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand<Payload>(of: [UTType], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](realityviewdefaultplaceholder/onpastecommand(of:validator:perform:)-2a639.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPasteCommand<Payload>(of: [String], validator: ([NSItemProvider]) -> Payload?, perform: (Payload) -> Void) -> some View](realityviewdefaultplaceholder/onpastecommand(of:validator:perform:)-8q9u5.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.
- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](realityviewdefaultplaceholder/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](realityviewdefaultplaceholder/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [func onPlayPauseCommand(perform: (() -> Void)?) -> some View](realityviewdefaultplaceholder/onplaypausecommand(perform:).md)
  Adds an action to perform in response to the system’s Play/Pause command.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](realityviewdefaultplaceholder/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](realityviewdefaultplaceholder/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
- [func onScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](realityviewdefaultplaceholder/onscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase, ScrollPhaseChangeContext) -> Void) -> some View](realityviewdefaultplaceholder/onscrollphasechange(_:)-4supk.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollPhaseChange((ScrollPhase, ScrollPhase) -> Void) -> some View](realityviewdefaultplaceholder/onscrollphasechange(_:)-7010b.md)
  Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [func onScrollTargetVisibilityChange<ID>(idType: ID.Type, threshold: Double, ([ID]) -> Void) -> some View](realityviewdefaultplaceholder/onscrolltargetvisibilitychange(idtype:threshold:_:).md)
  Adds an action to be called with information about what views would be considered visible.
- [func onScrollVisibilityChange(threshold: Double, (Bool) -> Void) -> some View](realityviewdefaultplaceholder/onscrollvisibilitychange(threshold:_:).md)
  Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](realityviewdefaultplaceholder/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func onTapGesture(count: Int, coordinateSpace: CoordinateSpace, perform: (CGPoint) -> Void) -> some View](realityviewdefaultplaceholder/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](realityviewdefaultplaceholder/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onVolumeViewpointChange(updateStrategy: VolumeViewpointUpdateStrategy, initial: Bool, (Viewpoint3D, Viewpoint3D) -> Void) -> some View](realityviewdefaultplaceholder/onvolumeviewpointchange(updatestrategy:initial:_:).md)
  Adds an action to perform when the viewpoint of the volume changes.
- [func opacity(Double) -> some View](realityviewdefaultplaceholder/opacity(_:).md)
  Sets the transparency of this view.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () -> Content) -> some View](realityviewdefaultplaceholder/ornament(visibility:attachmentanchor:contentalignment:ornament:).md)
  Presents an ornament.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](realityviewdefaultplaceholder/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](realityviewdefaultplaceholder/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](realityviewdefaultplaceholder/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](realityviewdefaultplaceholder/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](realityviewdefaultplaceholder/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func overlayPreferenceValue<K, V>(K.Type, alignment: Alignment, (K.Value) -> V) -> some View](realityviewdefaultplaceholder/overlaypreferencevalue(_:alignment:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
- [func padding(CGFloat) -> some View](realityviewdefaultplaceholder/padding(_:)-36mmk.md)
  Adds a specific padding amount to each edge of this view.
- [func padding(EdgeInsets) -> some View](realityviewdefaultplaceholder/padding(_:)-40lnu.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](realityviewdefaultplaceholder/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(EdgeInsets3D) -> some View](realityviewdefaultplaceholder/padding3d(_:)-4bls0.md)
  Pads this view using the edge insets you specify.
- [func padding3D(CGFloat) -> some View](realityviewdefaultplaceholder/padding3d(_:)-6gxc0.md)
  Pads this view along all edge insets by the amount you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](realityviewdefaultplaceholder/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func pageCommand<V>(value: Binding<V>, in: ClosedRange<V>, step: V) -> some View](realityviewdefaultplaceholder/pagecommand(value:in:step:).md)
  Steps a value through a range in response to page up or page down commands.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](realityviewdefaultplaceholder/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func pasteDestination<T>(for: T.Type, action: ([T]) -> Void, validator: ([T]) -> [T]) -> some View](realityviewdefaultplaceholder/pastedestination(for:action:validator:).md)
  Specifies an action that adds validated items to a view in response to the system’s Paste command.
- [func persistentSystemOverlays(Visibility) -> some View](realityviewdefaultplaceholder/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func perspectiveRotationEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](realityviewdefaultplaceholder/perspectiverotationeffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func phaseAnimator<Phase>(some Sequence, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](realityviewdefaultplaceholder/phaseanimator(_:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change continuously.
- [func phaseAnimator<Phase>(some Sequence, trigger: some Equatable, content: (PlaceholderContentView<Self>, Phase) -> some View, animation: (Phase) -> Animation?) -> some View](realityviewdefaultplaceholder/phaseanimator(_:trigger:content:animation:).md)
  Animates effects that you apply to a view over a sequence of phases that change based on a trigger.
- [func pickerStyle<S>(S) -> some View](realityviewdefaultplaceholder/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func pointerStyle(PointerStyle?) -> some View](realityviewdefaultplaceholder/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
- [func pointerVisibility(Visibility) -> some View](realityviewdefaultplaceholder/pointervisibility(_:).md)
  Sets the visibility of the pointer when it’s over the view.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](realityviewdefaultplaceholder/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](realityviewdefaultplaceholder/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func position(CGPoint) -> some View](realityviewdefaultplaceholder/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](realityviewdefaultplaceholder/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func preference<K>(key: K.Type, value: K.Value) -> some View](realityviewdefaultplaceholder/preference(key:value:).md)
  Sets a value for the given preference.
- [func preferredColorScheme(ColorScheme?) -> some View](realityviewdefaultplaceholder/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](realityviewdefaultplaceholder/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [func prefersDefaultFocus(Bool, in: Namespace.ID) -> some View](realityviewdefaultplaceholder/prefersdefaultfocus(_:in:).md)
  Indicates that the view should receive focus by default for a given namespace.
- [func presentationBackground<S>(S) -> some View](realityviewdefaultplaceholder/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](realityviewdefaultplaceholder/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](realityviewdefaultplaceholder/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](realityviewdefaultplaceholder/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](realityviewdefaultplaceholder/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](realityviewdefaultplaceholder/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](realityviewdefaultplaceholder/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationDetents(Set<PresentationDetent>) -> some View](realityviewdefaultplaceholder/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](realityviewdefaultplaceholder/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](realityviewdefaultplaceholder/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationPreventsAppTermination(Bool?) -> some View](realityviewdefaultplaceholder/presentationpreventsapptermination(_:).md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [func presentationSizing(some PresentationSizing) -> some View](realityviewdefaultplaceholder/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
- [func presentedWindowStyle<S>(S) -> some View](realityviewdefaultplaceholder/presentedwindowstyle(_:).md)
  Sets the style for windows created by interacting with this view.
- [func presentedWindowToolbarStyle<S>(S) -> some View](realityviewdefaultplaceholder/presentedwindowtoolbarstyle(_:).md)
  Sets the style for the toolbar in windows created by interacting with this view.
- [func previewContext<C>(C) -> some View](realityviewdefaultplaceholder/previewcontext(_:).md)
  Declares a context for the preview.
- [func previewDevice(PreviewDevice?) -> some View](realityviewdefaultplaceholder/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](realityviewdefaultplaceholder/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](realityviewdefaultplaceholder/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewLayout(PreviewLayout) -> some View](realityviewdefaultplaceholder/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func privacySensitive(Bool) -> some View](realityviewdefaultplaceholder/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func progressViewStyle<S>(S) -> some View](realityviewdefaultplaceholder/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func projectionEffect(ProjectionTransform) -> some View](realityviewdefaultplaceholder/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func realityViewCameraControls(CameraControls) -> some View](realityviewdefaultplaceholder/realityviewcameracontrols(_:).md)
  Adds gestures that control the position and direction of a virtual camera.
- [func redacted(reason: RedactionReasons) -> some View](realityviewdefaultplaceholder/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func refreshable(action: () async -> Void) -> some View](realityviewdefaultplaceholder/refreshable(action:).md)
  Marks this view as refreshable.
- [func renameAction(() -> Void) -> some View](realityviewdefaultplaceholder/renameaction(_:)-4po0i.md)
  Sets a closure to run for the rename action.
- [func renameAction(FocusState<Bool>.Binding) -> some View](realityviewdefaultplaceholder/renameaction(_:)-656nv.md)
  Sets the rename action in the environment to update focus state.
- [func replaceDisabled(Bool) -> some View](realityviewdefaultplaceholder/replacedisabled(_:).md)
  Prevents replace operations in a text editor.
- [func rotation3DEffect(Rotation3D, anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/rotation3deffect(_:anchor:).md)
  Rotates the view’s content by the specified 3D rotation value.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> ModifiedContent<Self, _Rotation3DEffectAngleAxis>](realityviewdefaultplaceholder/rotation3deffect(_:axis:anchor:)-3are5.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/rotation3deffect(_:axis:anchor:)-81ely.md)
  Rotates the view’s content by an angle about an axis that you specify as a tuple of elements.
- [func rotation3DEffect(Angle, axis: RotationAxis3D, anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/rotation3deffect(_:axis:anchor:)-ouyq.md)
  Rotates the view’s content by an angle about an axis that you specify as a rotation axis value.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](realityviewdefaultplaceholder/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](realityviewdefaultplaceholder/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment, spacing: CGFloat?, content: () -> V) -> some View](realityviewdefaultplaceholder/safeareainset(edge:alignment:spacing:content:)-7mf6o.md)
  Shows the specified content above or below the modified view.
- [func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment, spacing: CGFloat?, content: () -> V) -> some View](realityviewdefaultplaceholder/safeareainset(edge:alignment:spacing:content:)-8hcjw.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(CGFloat) -> some View](realityviewdefaultplaceholder/safeareapadding(_:)-4a3yv.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(EdgeInsets) -> some View](realityviewdefaultplaceholder/safeareapadding(_:)-4i610.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](realityviewdefaultplaceholder/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [func saturation(Double) -> some View](realityviewdefaultplaceholder/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func scaleEffect(Size3D, anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/scaleeffect(_:anchor:)-174i4.md)
  Scales this view uniformly by the specified size in each dimension.
- [func scaleEffect(CGFloat, anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/scaleeffect(_:anchor:)-3j4fw.md)
  Scales this view uniformly by the specified factor.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](realityviewdefaultplaceholder/scaleeffect(_:anchor:)-3k5xm.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> some View](realityviewdefaultplaceholder/scaleeffect(_:anchor:)-4tvqo.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(CGFloat, anchor: UnitPoint) -> ModifiedContent<Self, _UniformScaleEffect>](realityviewdefaultplaceholder/scaleeffect(_:anchor:)-767i5.md)
  Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](realityviewdefaultplaceholder/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some View](realityviewdefaultplaceholder/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors.
- [func scaledToFill() -> some View](realityviewdefaultplaceholder/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](realityviewdefaultplaceholder/scaledtofit.md)
  Scales this view to fit its parent.
- [func scenePadding(Edge.Set) -> some View](realityviewdefaultplaceholder/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](realityviewdefaultplaceholder/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](realityviewdefaultplaceholder/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollClipDisabled(Bool) -> some View](realityviewdefaultplaceholder/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func scrollContentBackground(Visibility) -> some View](realityviewdefaultplaceholder/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func scrollDisabled(Bool) -> some View](realityviewdefaultplaceholder/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](realityviewdefaultplaceholder/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](realityviewdefaultplaceholder/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](realityviewdefaultplaceholder/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](realityviewdefaultplaceholder/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](realityviewdefaultplaceholder/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func scrollPosition(Binding<ScrollPosition>, anchor: UnitPoint?) -> some View](realityviewdefaultplaceholder/scrollposition(_:anchor:).md)
  Associates a binding to a scroll position with a scroll view within this view.
- [func scrollPosition(id: Binding<(some Hashable)?>, anchor: UnitPoint?) -> some View](realityviewdefaultplaceholder/scrollposition(id:anchor:).md)
  Associates a binding to be updated when a scroll view within this view scrolls.
- [func scrollTargetBehavior(some ScrollTargetBehavior) -> some View](realityviewdefaultplaceholder/scrolltargetbehavior(_:).md)
  Sets the scroll behavior of views scrollable in the provided axes.
- [func scrollTargetLayout(isEnabled: Bool) -> some View](realityviewdefaultplaceholder/scrolltargetlayout(isenabled:).md)
  Configures the outermost layout as a scroll target layout.
- [func scrollTransition(ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](realityviewdefaultplaceholder/scrolltransition(_:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis?, transition: (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View](realityviewdefaultplaceholder/scrolltransition(topleading:bottomtrailing:axis:transition:).md)
  Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view, or other container specified using the `coordinateSpace` parameter.
- [func searchCompletion(String) -> some View](realityviewdefaultplaceholder/searchcompletion(_:)-1iwos.md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchCompletion<T>(T) -> some View](realityviewdefaultplaceholder/searchcompletion(_:)-38t6t.md)
  Associates a search token with the value of this view when used as a search suggestion.
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](realityviewdefaultplaceholder/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](realityviewdefaultplaceholder/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](realityviewdefaultplaceholder/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.
- [func searchPresentationToolbarBehavior(SearchPresentationToolbarBehavior) -> some View](realityviewdefaultplaceholder/searchpresentationtoolbarbehavior(_:).md)
  Configures the search toolbar presentation behavior for any searchable modifiers within this view.
- [func searchScopes<V, S>(Binding<V>, activation: SearchScopeActivation, () -> S) -> some View](realityviewdefaultplaceholder/searchscopes(_:activation:_:).md)
  Configures the search scopes for this view with the specified activation strategy.
- [func searchScopes<V, S>(Binding<V>, scopes: () -> S) -> some View](realityviewdefaultplaceholder/searchscopes(_:scopes:).md)
  Configures the search scopes for this view.
- [func searchSuggestions<S>(() -> S) -> some View](realityviewdefaultplaceholder/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchSuggestions(Visibility, for: SearchSuggestionsPlacement.Set) -> some View](realityviewdefaultplaceholder/searchsuggestions(_:for:).md)
  Configures how to display search suggestions within this view.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:ispresented:placement:prompt:token:)-1a0qa.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:ispresented:placement:prompt:token:)-2cma.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:ispresented:placement:prompt:token:)-5hy1v.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:placement:prompt:token:)-264hu.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: some StringProtocol, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:placement:prompt:token:)-3hcge.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (Binding<C.Element>) -> some View) -> some View](realityviewdefaultplaceholder/searchable(text:editabletokens:placement:prompt:token:)-8onyc.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?) -> some View](realityviewdefaultplaceholder/searchable(text:ispresented:placement:prompt:)-2xt42.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S) -> some View](realityviewdefaultplaceholder/searchable(text:ispresented:placement:prompt:)-50uaj.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](realityviewdefaultplaceholder/searchable(text:ispresented:placement:prompt:)-6ms52.md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:)-1heb1.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:)-2lprd.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:)-4j6c6.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:suggestions:)-518rn.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:suggestions:)-6xius.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](realityviewdefaultplaceholder/searchable(text:placement:prompt:suggestions:)-9rhwn.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:ispresented:placement:prompt:token:)-252rq.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:ispresented:placement:prompt:token:)-5uskf.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:ispresented:placement:prompt:token:)-u78f.md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:placement:prompt:token:)-2vb1v.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:placement:prompt:token:)-8mp8m.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:placement:prompt:token:)-9jgs0.md)
  Marks this view as searchable with text and tokens.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-1juzh.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-278nn.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:)-7o5wl.md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-2ngz.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: Text?, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-3p8z3.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, placement: SearchFieldPlacement, prompt: S, token: (C.Element) -> T) -> some View](realityviewdefaultplaceholder/searchable(text:tokens:suggestedtokens:placement:prompt:token:)-62lke.md)
  Marks this view as searchable with text, tokens, and suggestions.
- [func sectionActions<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/sectionactions(content:).md)
  Adds custom actions to a section.
- [func selectionDisabled(Bool) -> some View](realityviewdefaultplaceholder/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](realityviewdefaultplaceholder/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](realityviewdefaultplaceholder/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [func sensoryFeedback<T>(trigger: T, (T, T) -> SensoryFeedback?) -> some View](realityviewdefaultplaceholder/sensoryfeedback(trigger:_:).md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](realityviewdefaultplaceholder/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](realityviewdefaultplaceholder/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](realityviewdefaultplaceholder/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](realityviewdefaultplaceholder/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func speechAdjustedPitch(Double) -> some View](realityviewdefaultplaceholder/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](realityviewdefaultplaceholder/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](realityviewdefaultplaceholder/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](realityviewdefaultplaceholder/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some View](realityviewdefaultplaceholder/springloadingbehavior(_:).md)
  Sets the spring loading behavior this view.
- [func statusBar(hidden: Bool) -> some View](realityviewdefaultplaceholder/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func statusBarHidden(Bool) -> some View](realityviewdefaultplaceholder/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](realityviewdefaultplaceholder/strikethrough(_:pattern:color:).md)
  Applies a strikethrough to the text in this view.
- [func submitLabel(SubmitLabel) -> some View](realityviewdefaultplaceholder/submitlabel(_:).md)
  Sets the submit label for this view.
- [func submitScope(Bool) -> some View](realityviewdefaultplaceholder/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func supportedVolumeViewpoints(SquareAzimuth.Set) -> some View](realityviewdefaultplaceholder/supportedvolumeviewpoints(_:).md)
  Specifies which viewpoints are supported for the window bar and ornaments in a volume.
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](realityviewdefaultplaceholder/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](realityviewdefaultplaceholder/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](realityviewdefaultplaceholder/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](realityviewdefaultplaceholder/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](realityviewdefaultplaceholder/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](realityviewdefaultplaceholder/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
- [func tabItem<V>(() -> V) -> some View](realityviewdefaultplaceholder/tabitem(_:).md)
  Sets the tab bar item associated with this view.
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](realityviewdefaultplaceholder/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewStyle<S>(S) -> some View](realityviewdefaultplaceholder/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func tableColumnHeaders(Visibility) -> some View](realityviewdefaultplaceholder/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func tableStyle<S>(S) -> some View](realityviewdefaultplaceholder/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func tag<V>(V, includeOptional: Bool) -> some View](realityviewdefaultplaceholder/tag(_:includeoptional:).md)
  Sets the unique tag value of this view.
- [func task<T>(id: T, priority: TaskPriority, () async -> Void) -> some View](realityviewdefaultplaceholder/task(id:priority:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(priority: TaskPriority, () async -> Void) -> some View](realityviewdefaultplaceholder/task(priority:_:).md)
  Adds an asynchronous task to perform before this view appears.
- [func textCase(Text.Case?) -> some View](realityviewdefaultplaceholder/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
- [func textContentType(UITextContentType?) -> some View](realityviewdefaultplaceholder/textcontenttype(_:)-3jpie.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [func textContentType(NSTextContentType?) -> some View](realityviewdefaultplaceholder/textcontenttype(_:)-8hp93.md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textEditorStyle(some TextEditorStyle) -> some View](realityviewdefaultplaceholder/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [func textFieldStyle<S>(S) -> some View](realityviewdefaultplaceholder/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textInputAutocapitalization(TextInputAutocapitalization?) -> some View](realityviewdefaultplaceholder/textinputautocapitalization(_:).md)
  Sets how often the shift key in the keyboard is automatically enabled.
- [func textInputCompletion(String) -> some View](realityviewdefaultplaceholder/textinputcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a text input suggestion
- [func textInputSuggestions<S>(() -> S) -> some View](realityviewdefaultplaceholder/textinputsuggestions(_:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, Content>(Data, content: (Data.Element) -> Content) -> some View](realityviewdefaultplaceholder/textinputsuggestions(_:content:).md)
  Configures the text input suggestions for this view.
- [func textInputSuggestions<Data, ID, Content>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content) -> some View](realityviewdefaultplaceholder/textinputsuggestions(_:id:content:).md)
  Configures the text input suggestions for this view.
- [func textRenderer<T>(T) -> some View](realityviewdefaultplaceholder/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func textSelection<S>(S) -> some View](realityviewdefaultplaceholder/textselection(_:).md)
  Controls whether people can select text within this view.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](realityviewdefaultplaceholder/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tint(Color?) -> some View](realityviewdefaultplaceholder/tint(_:).md)
  Sets the tint color within this view.
- [func toggleStyle<S>(S) -> some View](realityviewdefaultplaceholder/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/toolbar(content:)-2xb41.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/toolbar(content:)-7y017.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](realityviewdefaultplaceholder/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](realityviewdefaultplaceholder/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarBackground(Visibility, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarbackground(_:for:)-2qsl6.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarBackground<S>(S, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarbackground(_:for:)-3b52a.md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](realityviewdefaultplaceholder/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func toolbarRole(ToolbarRole) -> some View](realityviewdefaultplaceholder/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](realityviewdefaultplaceholder/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](realityviewdefaultplaceholder/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](realityviewdefaultplaceholder/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func touchBar<Content>(TouchBar<Content>) -> some View](realityviewdefaultplaceholder/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBar<Content>(content: () -> Content) -> some View](realityviewdefaultplaceholder/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBarCustomizationLabel(Text) -> some View](realityviewdefaultplaceholder/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](realityviewdefaultplaceholder/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.
- [func touchBarItemPrincipal(Bool) -> some View](realityviewdefaultplaceholder/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func tracking(CGFloat) -> some View](realityviewdefaultplaceholder/tracking(_:).md)
  Sets the tracking for the text in this view.
- [func transaction((inout Transaction) -> Void) -> some View](realityviewdefaultplaceholder/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](realityviewdefaultplaceholder/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](realityviewdefaultplaceholder/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transform3DEffect(AffineTransform3D) -> some View](realityviewdefaultplaceholder/transform3deffect(_:).md)
  Applies a 3D transformation to the receiver.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](realityviewdefaultplaceholder/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformEffect(CGAffineTransform) -> some View](realityviewdefaultplaceholder/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](realityviewdefaultplaceholder/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](realityviewdefaultplaceholder/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func transition<T>(T) -> some View](realityviewdefaultplaceholder/transition(_:)-2zh2k.md)
  Associates a transition with the view.
- [func transition(AnyTransition) -> some View](realityviewdefaultplaceholder/transition(_:)-6q13d.md)
  Associates a transition with the view.
- [func truncationMode(Text.TruncationMode) -> some View](realityviewdefaultplaceholder/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func typeSelectEquivalent(Text?) -> some View](realityviewdefaultplaceholder/typeselectequivalent(_:)-2yo6p.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent(LocalizedStringKey) -> some View](realityviewdefaultplaceholder/typeselectequivalent(_:)-6ol92.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typeSelectEquivalent<S>(S) -> some View](realityviewdefaultplaceholder/typeselectequivalent(_:)-8c2zc.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
- [func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/typesettinglanguage(_:isenabled:)-1r2at.md)
  Specifies the language for typesetting.
- [func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View](realityviewdefaultplaceholder/typesettinglanguage(_:isenabled:)-5g58g.md)
  Specifies the language for typesetting.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some View](realityviewdefaultplaceholder/underline(_:pattern:color:).md)
  Applies an underline to the text in this view.
- [func unredacted() -> some View](realityviewdefaultplaceholder/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func upperLimbVisibility(Visibility) -> some View](realityviewdefaultplaceholder/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an `ImmersiveSpace` scene is presented.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](realityviewdefaultplaceholder/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](realityviewdefaultplaceholder/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func visualEffect((EmptyVisualEffect, GeometryProxy) -> some VisualEffect) -> some View](realityviewdefaultplaceholder/visualeffect(_:).md)
  Applies effects to this view, while providing access to layout information through a geometry proxy.
- [func visualEffect3D((EmptyVisualEffect, GeometryProxy3D) -> some VisualEffect) -> some View](realityviewdefaultplaceholder/visualeffect3d(_:).md)
  Applies effects to this view, while providing access to layout information through a 3D geometry proxy.
- [func volumeBaseplateVisibility(Visibility) -> some View](realityviewdefaultplaceholder/volumebaseplatevisibility(_:).md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](realityviewdefaultplaceholder/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](realityviewdefaultplaceholder/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](realityviewdefaultplaceholder/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](realityviewdefaultplaceholder/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](realityviewdefaultplaceholder/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](realityviewdefaultplaceholder/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](realityviewdefaultplaceholder/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.
- [func zIndex(Double) -> some View](realityviewdefaultplaceholder/zindex(_:).md)
  Controls the display order of overlapping views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/view-implementations)*