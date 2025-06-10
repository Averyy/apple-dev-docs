# View Modifiers

**Framework**: FamilyControls

Apply standard modifiers to configure the family activity picker view and the views it contains.

#### Overview

Every type that conforms to the [`View`](https://developer.apple.com/documentation/SwiftUI/View) protocol gains access to the set of view modifiers defined by that protocol. For information about using view modifiers, see [`Configuring views`](https://developer.apple.com/documentation/SwiftUI/Configuring-Views).

## Topics

### Accessibility Labels
- [func accessibilityLabel<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ee7a.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1ug11.md)
  Adds a label to the view that describes its contents.
- [func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitylabel(_:)-1goip.md)
  Adds a label to the view that describes its contents.
- [func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-1ijca.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels([Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-8dgot.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityinputlabels(_:)-9t208.md)
  Sets alternate input labels with which users identify a view.
- [func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in: Namespace.ID) -> some View](familyactivitypicker/accessibilitylabeledpair(role:id:in:).md)
  Pairs an accessibility element representing a label with the element for the matching content.
### Accessibility Values
- [func accessibilityValue<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityvalue(_:)-23u6p.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityvalue(_:)-4hvxj.md)
  Adds a textual description of the value that the view contains.
- [func accessibilityValue(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityvalue(_:)-9owpi.md)
  Adds a textual description of the value that the view contains.
### Accessibility Hints
- [func accessibilityHint(Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityhint(_:)-6qwn7.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint(LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityhint(_:)-8mj2n.md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibilityHint<S>(S) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityhint(_:)-r1tf.md)
  Communicates to the user what happens after performing the view’s action.
### Accessibility Actions
- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<S>(named: S, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityaction(named:_:)-1elny.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: Text, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityaction(named:_:)-1ll74.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named: LocalizedStringKey, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityaction(named:_:)-9xrhk.md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](familyactivitypicker/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
### Accessibility Activation Point
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-34miz.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-ci2b.md)
  Specifies the unit point where activations occur in the view.
- [func accessibilityActivationPoint(CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityactivationpoint(_:)-6snx8.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityactivationpoint(_:)-8dxs2.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
### Accessibility Elements
- [func accessibilityElement(children: AccessibilityChildBehavior) -> some View](familyactivitypicker/accessibilityelement(children:).md)
  Creates a new accessibility element, or modifies the `AccessibilityChildBehavior` of the existing accessibility element.
- [func accessibilityChildren<V>(children: () -> V) -> some View](familyactivitypicker/accessibilitychildren(children:).md)
  Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [func accessibilityHidden(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityhidden(_:).md)
  Specifies whether to hide this view from system accessibility features.
### Accessibility Custom Controls
- [func accessibilityRepresentation<V>(representation: () -> V) -> some View](familyactivitypicker/accessibilityrepresentation(representation:).md)
  Replaces one or more accessibility elements for this view with new accessibility elements.
- [func accessibilityRespondsToUserInteraction(Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityrespondstouserinteraction(_:).md)
  Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.
### Accessibility Custom Content
- [func accessibilityCustomContent(LocalizedStringKey, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-1eecd.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, Text?, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-5rztl.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(AccessibilityCustomContentKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-8vkni.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-916gj.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(Text, Text, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-93rid.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-9h049.md)
  Add additional accessibility information to the view.
- [func accessibilityCustomContent<V>(LocalizedStringKey, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-vbej.md)
  Add additional accessibility information to the view.
### Accessibility Navigation
- [func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-210yl.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-234mz.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-3nods.md)
  Create an Accessibility Rotor with the specified user-visible label, and entries generated from the content closure.
- [func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () -> Content) -> some View](familyactivitypicker/accessibilityrotor(_:entries:)-99hnz.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel, ID>(L, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-1hmpp.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(Text, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-2um65.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(LocalizedStringKey, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-6bu1u.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries: [EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entryid:entrylabel:)-f72f.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<EntryModel>(Text, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-4lszi.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(LocalizedStringKey, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-8vebh.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-8wmbn.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor.
- [func accessibilityRotor<L, EntryModel>(L, entries: [EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View](familyactivitypicker/accessibilityrotor(_:entries:entrylabel:)-976pf.md)
  Create an Accessibility Rotor with the specified user-visible label and entries.
- [func accessibilityRotor(Text, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-64gnn.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(AccessibilitySystemRotor, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-66zli.md)
  Create an Accessibility Rotor replacing the specified system-provided Rotor. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor<L>(L, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-9swhk.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotor(LocalizedStringKey, textRanges: [Range<String.Index>]) -> some View](familyactivitypicker/accessibilityrotor(_:textranges:)-wfkm.md)
  Create an Accessibility Rotor with the specified user-visible label and entries for each of the specified ranges. The Rotor will be attached to the current Accessibility element, and each entry will go the specified range of that element.
- [func accessibilityRotorEntry<ID>(id: ID, in: Namespace.ID) -> some View](familyactivitypicker/accessibilityrotorentry(id:in:).md)
  Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [func accessibilityLinkedGroup<ID>(id: ID, in: Namespace.ID) -> some View](familyactivitypicker/accessibilitylinkedgroup(id:in:).md)
  Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [func accessibilitySortPriority(Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitysortpriority(_:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
### Accessibility Focus
- [func accessibilityFocused(AccessibilityFocusState<Bool>.Binding) -> some View](familyactivitypicker/accessibilityfocused(_:).md)
  Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [func accessibilityFocused<Value>(AccessibilityFocusState<Value>.Binding, equals: Value) -> some View](familyactivitypicker/accessibilityfocused(_:equals:).md)
  Modifies this view by binding its accessibility element’s focus state to the given state value.
### Accessibility Traits
- [func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityaddtraits(_:).md)
  Adds the given traits to the view.
- [func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityremovetraits(_:).md)
  Removes the given traits from this view.
### Accessibility Identity
- [func accessibilityIdentifier(String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityidentifier(_:).md)
  Uses the string you specify to identify the view.
### Accessibility Color Inversion
- [func accessibilityIgnoresInvertColors(Bool) -> some View](familyactivitypicker/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
### Accessibility Content Descriptions
- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
### VoiceOver
- [func speechAdjustedPitch(Double) -> some View](familyactivitypicker/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> some View](familyactivitypicker/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> some View](familyactivitypicker/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](familyactivitypicker/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.
### Accessibility Chart Descriptions
- [func accessibilityChartDescriptor<R>(R) -> some View](familyactivitypicker/accessibilitychartdescriptor(_:).md)
  Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
### Tint Color
- [func tint(Color?) -> some View](familyactivitypicker/tint(_:).md)
  Sets the tint color within this view.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listItemTint(ListItemTint?) -> some View](familyactivitypicker/listitemtint(_:)-9guaj.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](familyactivitypicker/listitemtint(_:)-9hrk.md)
  Sets a fixed tint color for content in a list.
### Foreground Elements
- [func foregroundStyle<S>(S) -> some View](familyactivitypicker/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](familyactivitypicker/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](familyactivitypicker/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func foregroundColor(Color?) -> some View](familyactivitypicker/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
### Background Elements
- [func border<S>(S, width: CGFloat) -> some View](familyactivitypicker/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](familyactivitypicker/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-180sg.md)
  Sets the view’s background to a shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-3jkgw.md)
  Sets the view’s background to a shape filled with a style.
- [func background<S>(in: S, fillStyle: FillStyle) -> some View](familyactivitypicker/background(in:fillstyle:)-7fmje.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View](familyactivitypicker/background(_:in:fillstyle:)-2cobx.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func listRowBackground<V>(V?) -> some View](familyactivitypicker/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
### Light and Dark Appearance
- [func preferredColorScheme(ColorScheme?) -> some View](familyactivitypicker/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
### Prominence
- [func headerProminence(Prominence) -> some View](familyactivitypicker/headerprominence(_:).md)
  Sets the header prominence for this view.
### Privacy and Redaction
- [func privacySensitive(Bool) -> some View](familyactivitypicker/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](familyactivitypicker/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](familyactivitypicker/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
### Visibility
- [func hidden() -> some View](familyactivitypicker/hidden.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](familyactivitypicker/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](familyactivitypicker/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
### Fonts
- [func font(Font?) -> some View](familyactivitypicker/font(_:).md)
  Sets the default font for text in this view.
### Text Style
- [func monospacedDigit() -> some View](familyactivitypicker/monospaceddigit.md)
  Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [func textCase(Text.Case?) -> some View](familyactivitypicker/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.
### Text Layout
- [func allowsTightening(Bool) -> some View](familyactivitypicker/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func minimumScaleFactor(CGFloat) -> some View](familyactivitypicker/minimumscalefactor(_:).md)
  Sets the minimum amount that text in this view scales down to fit in the available space.
- [func truncationMode(Text.TruncationMode) -> some View](familyactivitypicker/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](familyactivitypicker/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
### Multiline Text
- [func lineSpacing(CGFloat) -> some View](familyactivitypicker/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func multilineTextAlignment(TextAlignment) -> some View](familyactivitypicker/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.
### Text Selection
- [func textSelection<S>(S) -> some View](familyactivitypicker/textselection(_:).md)
  Controls whether people can select text within this view.
### Text Entry
- [func keyboardType(UIKeyboardType) -> some View](familyactivitypicker/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func disableAutocorrection(Bool?) -> some View](familyactivitypicker/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](familyactivitypicker/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.
- [func textContentType(UITextContentType?) -> some View](familyactivitypicker/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
### Keyboard Shortcuts
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers) -> some View](familyactivitypicker/keyboardshortcut(_:modifiers:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
- [func keyboardShortcut(KeyEquivalent, modifiers: EventModifiers, localization: KeyboardShortcut.Localization) -> some View](familyactivitypicker/keyboardshortcut(_:modifiers:localization:).md)
  Defines a keyboard shortcut and assigns it to the modified control.
### Symbol Appearance
- [func symbolRenderingMode(SymbolRenderingMode?) -> some View](familyactivitypicker/symbolrenderingmode(_:).md)
  Sets the rendering mode for symbol images within this view.
- [func symbolVariant(SymbolVariants) -> some View](familyactivitypicker/symbolvariant(_:).md)
  Makes symbols within the view show a particular variant.
### Badges
- [func badge(LocalizedStringKey?) -> some View](familyactivitypicker/badge(_:)-15e4b.md)
  Generates a badge for the view from a localized string key.
- [func badge(Int) -> some View](familyactivitypicker/badge(_:)-15pe.md)
  Generates a badge for the view from an integer value.
- [func badge<S>(S?) -> some View](familyactivitypicker/badge(_:)-720cq.md)
  Generates a badge for the view from a string.
- [func badge(Text?) -> some View](familyactivitypicker/badge(_:)-7hd2m.md)
  Generates a badge for the view from a text view.
### Search
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey) -> some View](familyactivitypicker/searchable(text:placement:prompt:)-4oday.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](familyactivitypicker/searchable(text:placement:prompt:)-634x8.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](familyactivitypicker/searchable(text:placement:prompt:)-dn5c.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-1hlnk.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-5gxr9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-g7yw.md)
  Marks this view as searchable, which configures the display of a search field.
### Navigation Titles
- [func navigationTitle<V>(() -> V) -> some View](familyactivitypicker/navigationtitle(_:)-3uuta.md)
  Configures the view’s title for purposes of navigation, using a custom view.
- [func navigationTitle(Text) -> some View](familyactivitypicker/navigationtitle(_:)-7gm3d.md)
  Configures the view’s title for purposes of navigation.
- [func navigationTitle(LocalizedStringKey) -> some View](familyactivitypicker/navigationtitle(_:)-7i3uf.md)
  Configures the view’s title for purposes of navigation, using a localized string.
- [func navigationTitle<S>(S) -> some View](familyactivitypicker/navigationtitle(_:)-y4fk.md)
  Configures the view’s title for purposes of navigation, using a string.
### Navigation Bars
- [func navigationBarHidden(Bool) -> some View](familyactivitypicker/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func navigationBarBackButtonHidden(Bool) -> some View](familyactivitypicker/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
### Toolbars
- [func toolbar<Content>(content: () -> Content) -> some View](familyactivitypicker/toolbar(content:)-4me03.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(content: () -> Content) -> some View](familyactivitypicker/toolbar(content:)-60tl0.md)
  Populates the toolbar or navigation bar with the views you provide.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](familyactivitypicker/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
### Tab Views
- [func tabItem<V>(() -> V) -> some View](familyactivitypicker/tabitem(_:).md)
  Sets the tab bar item associated with this view.
### Help Text
- [func help<S>(S) -> some View](familyactivitypicker/help(_:)-30gcc.md)
  Adds help text to a view using a string that you provide.
- [func help(Text) -> some View](familyactivitypicker/help(_:)-5nten.md)
  Adds help text to a view using a text view that you provide.
- [func help(LocalizedStringKey) -> some View](familyactivitypicker/help(_:)-pa0w.md)
  Adds help text to a view using a localized string that you provide.
### Context Menus
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](familyactivitypicker/contextmenu(menuitems:).md)
  Adds a context menu to a view.
### The Status Bar
- [func statusBar(hidden: Bool) -> some View](familyactivitypicker/statusbar(hidden:).md)
  Sets the visibility of the status bar.
### Styles
- [func buttonStyle<S>(S) -> some View](familyactivitypicker/buttonstyle(_:)-5jlha.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonStyle<S>(S) -> some View](familyactivitypicker/buttonstyle(_:)-9kz36.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func controlGroupStyle<S>(S) -> some View](familyactivitypicker/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func datePickerStyle<S>(S) -> some View](familyactivitypicker/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func groupBoxStyle<S>(S) -> some View](familyactivitypicker/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func indexViewStyle<S>(S) -> some View](familyactivitypicker/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func labelStyle<S>(S) -> some View](familyactivitypicker/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func listStyle<S>(S) -> some View](familyactivitypicker/liststyle(_:).md)
  Sets the style for lists within this view.
- [func menuStyle<S>(S) -> some View](familyactivitypicker/menustyle(_:).md)
  Sets the style for menus within this view.
- [func navigationViewStyle<S>(S) -> some View](familyactivitypicker/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func pickerStyle<S>(S) -> some View](familyactivitypicker/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func progressViewStyle<S>(S) -> some View](familyactivitypicker/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func textFieldStyle<S>(S) -> some View](familyactivitypicker/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func toggleStyle<S>(S) -> some View](familyactivitypicker/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func tabViewStyle<S>(S) -> some View](familyactivitypicker/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
### Size
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](familyactivitypicker/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](familyactivitypicker/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func fixedSize() -> some View](familyactivitypicker/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](familyactivitypicker/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](familyactivitypicker/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.
### Position
- [func position(CGPoint) -> some View](familyactivitypicker/position(_:).md)
  Positions the center of this view at the specified point in its parent’s coordinate space.
- [func position(x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/position(x:y:).md)
  Positions the center of this view at the specified coordinates in its parent’s coordinate space.
- [func offset(CGSize) -> some View](familyactivitypicker/offset(_:).md)
  Offset this view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/offset(x:y:).md)
  Offset this view by the specified horizontal and vertical distances.
- [func coordinateSpace<T>(name: T) -> some View](familyactivitypicker/coordinatespace(name:).md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
### Padding
- [func padding(EdgeInsets) -> some View](familyactivitypicker/padding(_:)-3l4hp.md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](familyactivitypicker/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func scenePadding(Edge.Set) -> some View](familyactivitypicker/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](familyactivitypicker/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
### Layering
- [func zIndex(Double) -> some View](familyactivitypicker/zindex(_:).md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](familyactivitypicker/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func listRowInsets(EdgeInsets?) -> some View](familyactivitypicker/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](familyactivitypicker/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
### Masks and Clipping
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](familyactivitypicker/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func clipped(antialiased: Bool) -> some View](familyactivitypicker/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](familyactivitypicker/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](familyactivitypicker/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func containerShape<T>(T) -> some View](familyactivitypicker/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
### Scale
- [func scaledToFill() -> some View](familyactivitypicker/scaledtofill.md)
  Scales this view to fill its parent.
- [func scaledToFit() -> some View](familyactivitypicker/scaledtofit.md)
  Scales this view to fit its parent.
- [func scaleEffect(CGSize, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(_:anchor:)-1mz0o.md)
  Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.
- [func scaleEffect(x: CGFloat, y: CGFloat, anchor: UnitPoint) -> some View](familyactivitypicker/scaleeffect(x:y:anchor:).md)
  Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [func imageScale(Image.Scale) -> some View](familyactivitypicker/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [func aspectRatio(CGSize, contentMode: ContentMode) -> some View](familyactivitypicker/aspectratio(_:contentmode:)-7zcef.md)
  Constrains this view’s dimensions to the aspect ratio of the given size.
### Rotation and Transformation
- [func rotationEffect(Angle, anchor: UnitPoint) -> some View](familyactivitypicker/rotationeffect(_:anchor:).md)
  Rotates a view’s rendered output in two dimensions around the specified point.
- [func rotation3DEffect(Angle, axis: (x: CGFloat, y: CGFloat, z: CGFloat), anchor: UnitPoint, anchorZ: CGFloat, perspective: CGFloat) -> some View](familyactivitypicker/rotation3deffect(_:axis:anchor:anchorz:perspective:).md)
  Renders a view’s content as if it’s rotated in three dimensions around the specified axis.
- [func projectionEffect(ProjectionTransform) -> some View](familyactivitypicker/projectioneffect(_:).md)
  Applies a projection transformation to this view’s rendered output.
- [func transformEffect(CGAffineTransform) -> some View](familyactivitypicker/transformeffect(_:).md)
  Applies an affine transformation to this view’s rendered output.
### Graphical Effects
- [func blur(radius: CGFloat, opaque: Bool) -> some View](familyactivitypicker/blur(radius:opaque:).md)
  Applies a Gaussian blur to this view.
- [func opacity(Double) -> some View](familyactivitypicker/opacity(_:).md)
  Sets the transparency of this view.
- [func brightness(Double) -> some View](familyactivitypicker/brightness(_:).md)
  Brightens this view by the specified amount.
- [func contrast(Double) -> some View](familyactivitypicker/contrast(_:).md)
  Sets the contrast and separation between similar colors in this view.
- [func colorInvert() -> some View](familyactivitypicker/colorinvert.md)
  Inverts the colors in this view.
- [func colorMultiply(Color) -> some View](familyactivitypicker/colormultiply(_:).md)
  Adds a color multiplication effect to this view.
- [func saturation(Double) -> some View](familyactivitypicker/saturation(_:).md)
  Adjusts the color saturation of this view.
- [func grayscale(Double) -> some View](familyactivitypicker/grayscale(_:).md)
  Adds a grayscale effect to this view.
- [func hueRotation(Angle) -> some View](familyactivitypicker/huerotation(_:).md)
  Applies a hue rotation effect to this view.
- [func luminanceToAlpha() -> some View](familyactivitypicker/luminancetoalpha.md)
  Adds a luminance to alpha effect to this view.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some View](familyactivitypicker/shadow(color:radius:x:y:).md)
  Adds a shadow to this view.
### Composites
- [func blendMode(BlendMode) -> some View](familyactivitypicker/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](familyactivitypicker/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](familyactivitypicker/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
### Animations
- [func animation<V>(Animation?, value: V) -> some View](familyactivitypicker/animation(_:value:).md)
  Applies the given animation to this view when the specified value changes.
- [func transaction((inout Transaction) -> Void) -> some View](familyactivitypicker/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](familyactivitypicker/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
### Interactivity
- [func disabled(Bool) -> some View](familyactivitypicker/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](familyactivitypicker/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
### Swipe Actions
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](familyactivitypicker/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
### Refresh Controls
- [func refreshable(action: () async -> Void) -> some View](familyactivitypicker/refreshable(action:).md)
  Marks this view as refreshable.
### Taps and Gestures
- [func onTapGesture(count: Int, perform: () -> Void) -> some View](familyactivitypicker/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func gesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
### Hover
- [func onHover(perform: (Bool) -> Void) -> some View](familyactivitypicker/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func hoverEffect(HoverEffect) -> some View](familyactivitypicker/hovereffect(_:).md)
  Applies a hover effect to this view.
### Focus
- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](familyactivitypicker/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](familyactivitypicker/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [func focusable(Bool) -> some View](familyactivitypicker/focusable(_:).md)
  Specifies if the view is focusable.
### Drag and Drop
- [func onDrag<V>(() -> NSItemProvider, preview: () -> V) -> some View](familyactivitypicker/ondrag(_:preview:).md)
  Activates this view as the source of a drag and drop operation.
- [func onDrag(() -> NSItemProvider) -> some View](familyactivitypicker/ondrag(_:).md)
  Activates this view as the source of a drag and drop operation.
- [func itemProvider(Optional<() -> NSItemProvider?>) -> some View](familyactivitypicker/itemprovider(_:).md)
  Provides a closure that vends the drag representation to be used for a particular data element.
- [func onDrop(of: [UTType], delegate: any DropDelegate) -> some View](familyactivitypicker/ondrop(of:delegate:)-3ufe4.md)
  Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-5tsvq.md)
  Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [func onDrop(of: [UTType], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-85s24.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
### Submission
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](familyactivitypicker/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](familyactivitypicker/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](familyactivitypicker/submitlabel(_:).md)
  Sets the submit label for this view.
### Movement
- [func moveDisabled(Bool) -> some View](familyactivitypicker/movedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is movable.
### Deletion
- [func deleteDisabled(Bool) -> some View](familyactivitypicker/deletedisabled(_:).md)
  Adds a condition for whether the view’s view hierarchy is deletable.
### User Activities
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](familyactivitypicker/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](familyactivitypicker/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](familyactivitypicker/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
### View Life Cycle
- [func onAppear(perform: (() -> Void)?) -> some View](familyactivitypicker/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onDisappear(perform: (() -> Void)?) -> some View](familyactivitypicker/ondisappear(perform:).md)
  Adds an action to perform after this view disappears.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](familyactivitypicker/onchange(of:perform:).md)
  Performs an action when a specified value changes.
### URLs
- [func onOpenURL(perform: (URL) -> ()) -> some View](familyactivitypicker/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
### Publisher Events
- [func onReceive<P>(P, perform: (P.Output) -> Void) -> some View](familyactivitypicker/onreceive(_:perform:).md)
  Adds an action to perform when this view detects data emitted by the given publisher.
### Hit Testing
- [func allowsHitTesting(Bool) -> some View](familyactivitypicker/allowshittesting(_:).md)
  Configures whether this view participates in hit test operations.
- [func contentShape<S>(S, eoFill: Bool) -> some View](familyactivitypicker/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
### Alerts
- [func alert<A>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A) -> some View](familyactivitypicker/alert(_:ispresented:actions:)-6lo8z.md)
  Presents an alert when a given condition is true, using a localized string key for the title.
- [func alert<A>(Text, isPresented: Binding<Bool>, actions: () -> A) -> some View](familyactivitypicker/alert(_:ispresented:actions:)-9tpgm.md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert<S, A>(S, isPresented: Binding<Bool>, actions: () -> A) -> some View](familyactivitypicker/alert(_:ispresented:actions:)-nusq.md)
  Presents an alert when a given condition is true, using a string variable as a title.
- [func alert<S, A, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:)-1ebnr.md)
  Presents an alert using the given data to produce the alert’s content and a string variable as a title.
- [func alert<A, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:)-7vxkj.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:)-80c9a.md)
  Presents an alert using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](familyactivitypicker/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
### Alerts with a Message
- [func alert<A, M>(Text, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/alert(_:ispresented:actions:message:)-3yino.md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/alert(_:ispresented:actions:message:)-5d7w0.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/alert(_:ispresented:actions:message:)-8ae3a.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-233cu.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-2d9eq.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-7626v.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](familyactivitypicker/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
### Confirmation Dialogs
- [func confirmationDialog<A>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-2bylv.md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog<S, A>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-5uss9.md)
  Presents a confirmation dialog when a given condition is true, using a string variable as a title.
- [func confirmationDialog<A>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:)-95nrx.md)
  Presents a confirmation dialog when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<S, A, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-3wmm9.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.
- [func confirmationDialog<A, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-6z9kv.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-84l76.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
### Confirmation Dialogs with a Message
- [func confirmationDialog<A, M>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-1eep0.md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog<S, A, M>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-595po.md)
  Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.
- [func confirmationDialog<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-85sm5.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string key for the title.
- [func confirmationDialog<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-3miu6.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string key for the title.
- [func confirmationDialog<A, M, T>(Text, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-5xnm2.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func confirmationDialog<S, A, M, T>(S, isPresented: Binding<Bool>, titleVisibility: Visibility, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:)-tgyv.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a string variable for the title.
### Sheets
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](familyactivitypicker/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](familyactivitypicker/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](familyactivitypicker/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](familyactivitypicker/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
### Popovers
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](familyactivitypicker/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](familyactivitypicker/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
### Sheet and Popover Dismissal
- [func interactiveDismissDisabled(Bool) -> some View](familyactivitypicker/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
### File Managers
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3cork.md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:)-3mnp5.md)
  Presents a system interface for exporting a document that’s stored in a reference type, like a class, to a file on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-2szoo.md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentType: UTType, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileexporter(ispresented:documents:contenttype:oncompletion:)-9hq0d.md)
  Presents a system interface for exporting a collection of reference type documents to files on disk.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](familyactivitypicker/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](familyactivitypicker/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
### Identity
- [func id<ID>(ID) -> some View](familyactivitypicker/id(_:).md)
  Binds a view’s identity to the given proxy value.
### Default Storage
- [func defaultAppStorage(UserDefaults) -> some View](familyactivitypicker/defaultappstorage(_:).md)
  The default store used by `AppStorage` contained within the view.
### Preferences
- [func preference<K>(key: K.Type, value: K.Value) -> some View](familyactivitypicker/preference(key:value:).md)
  Sets a value for the given preference.
- [func transformPreference<K>(K.Type, (inout K.Value) -> Void) -> some View](familyactivitypicker/transformpreference(_:_:).md)
  Applies a transformation to a preference value.
- [func anchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (Anchor<A>) -> K.Value) -> some View](familyactivitypicker/anchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func transformAnchorPreference<A, K>(key: K.Type, value: Anchor<A>.Source, transform: (inout K.Value, Anchor<A>) -> Void) -> some View](familyactivitypicker/transformanchorpreference(key:value:transform:).md)
  Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.
- [func onPreferenceChange<K>(K.Type, perform: (K.Value) -> Void) -> some View](familyactivitypicker/onpreferencechange(_:perform:).md)
  Adds an action to perform when the specified preference key’s value changes.
- [func backgroundPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](familyactivitypicker/backgroundpreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [func overlayPreferenceValue<Key, T>(Key.Type, (Key.Value) -> T) -> some View](familyactivitypicker/overlaypreferencevalue(_:_:).md)
  Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.
### Environment Values
- [func environmentObject<T>(T) -> some View](familyactivitypicker/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func transformEnvironment<V>(WritableKeyPath<EnvironmentValues, V>, transform: (inout V) -> Void) -> some View](familyactivitypicker/transformenvironment(_:transform:).md)
  Transforms the environment value of the specified key path with the given function.
### Configuring View Previews
- [func previewDevice(PreviewDevice?) -> some View](familyactivitypicker/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](familyactivitypicker/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewLayout(PreviewLayout) -> some View](familyactivitypicker/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](familyactivitypicker/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewContext<C>(C) -> some View](familyactivitypicker/previewcontext(_:).md)
  Declares a context for the preview.
### Implementing View Modifiers
- [func modifier<T>(T) -> ModifiedContent<Self, T>](familyactivitypicker/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
### Deprecated Accessibility Modifiers
- [func accessibility(label: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(label:).md)
  Adds a label to the view that describes its contents.
- [func accessibility(value: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(value:).md)
  Adds a textual description of the value that the view contains.
- [func accessibility(hidden: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(hidden:).md)
  Specifies whether to hide this view from system accessibility features.
- [func accessibility(identifier: String) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(identifier:).md)
  Uses the specified string to identify the view.
- [func accessibility(selectionIdentifier: AnyHashable) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(selectionidentifier:).md)
  Sets a selection identifier for this view’s accessibility element.
- [func accessibility(hint: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(hint:).md)
  Communicates to the user what happens after performing the view’s action.
- [func accessibility(activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-34miz.md)
  Specifies the point where activations occur in the view.
- [func accessibility(activationPoint: UnitPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(activationpoint:)-ci2b.md)
  Specifies the unit point where activations occur in the view.
- [func accessibility(inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(inputlabels:).md)
  Sets alternate input labels with which users identify a view.
- [func accessibility(addTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(addtraits:).md)
  Adds the given traits to the view.
- [func accessibility(removeTraits: AccessibilityTraits) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(removetraits:).md)
  Removes the given traits from this view.
- [func accessibility(sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibility(sortpriority:).md)
  Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
- [func accessibilityCustomContent<L, V>(L, V, importance: AXCustomContent.Importance) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](familyactivitypicker/accessibilitycustomcontent(_:_:importance:)-8480d.md)
  Add additional accessibility information to the view.
### Deprecated Appearance Modifiers
- [func colorScheme(ColorScheme) -> some View](familyactivitypicker/colorscheme(_:).md)
  Sets this view’s color scheme.
### Deprecated Auxiliary View Modifiers
- [func navigationBarTitle<S>(S) -> some View](familyactivitypicker/navigationbartitle(_:)-5rx0t.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey) -> some View](familyactivitypicker/navigationbartitle(_:)-808tn.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](familyactivitypicker/navigationbartitle(_:)-9xbmw.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-22lni.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-30k3d.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-9ps22.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](familyactivitypicker/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](familyactivitypicker/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](familyactivitypicker/navigationbaritems(trailing:).md)
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](familyactivitypicker/contextmenu(_:).md)
  Adds a context menu to the view.
### Deprecated Layout Modifiers
- [func frame() -> some View](familyactivitypicker/frame.md)
  Positions this view within an invisible frame.
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](familyactivitypicker/edgesignoringsafearea(_:).md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](familyactivitypicker/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func background<Background>(Background, alignment: Alignment) -> some View](familyactivitypicker/background(_:alignment:).md)
  Layers the given view behind this view.
### Deprecated Graphics and Rendering Modifiers
- [func accentColor(Color?) -> some View](familyactivitypicker/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func mask<Mask>(Mask) -> some View](familyactivitypicker/mask(_:).md)
  Masks this view using the alpha channel of the given view.
- [func animation(Animation?) -> some View](familyactivitypicker/animation(_:).md)
  Applies the given animation to all animatable values within this view.
### Deprecated Input and Event Modifiers
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](familyactivitypicker/ondrop(of:delegate:)-3cx1m.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-647xj.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-6kw8i.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.
### Deprecated View Presentation Modifiers
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](familyactivitypicker/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](familyactivitypicker/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](familyactivitypicker/alert(ispresented:content:).md)
  Presents an alert to the user.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](familyactivitypicker/alert(item:content:).md)
  Presents an alert to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker-view-modifiers)*