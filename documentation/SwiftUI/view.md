# View

**Framework**: SwiftUI  
**Kind**: protocol

A type that represents part of your app’s user interface and provides modifiers that you use to configure views.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol View
```

## Mentions

- [Declaring a custom view](declaring-a-custom-view.md)
- [Configuring views](configuring-views.md)
- [Reducing view modifier maintenance](reducing-view-modifier-maintenance.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)
- [Performing a search operation](performing-a-search-operation.md)

#### Overview

You create custom views by declaring types that conform to the `View` protocol. Implement the required [`body`](view/body-8kl5o.md) computed property to provide the content for your custom view.

```swift
struct MyView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
```

Assemble the view’s body by combining one or more of the built-in views provided by SwiftUI, like the [`Text`](text.md) instance in the example above, plus other custom views that you define, into a hierarchy of views. For more information about creating custom views, see [`Declaring a custom view`](declaring-a-custom-view.md).

The `View` protocol provides a set of modifiers — protocol methods with default implementations — that you use to configure views in the layout of your app. Modifiers work by wrapping the view instance on which you call them in another view with the specified characteristics, as described in [`Configuring views`](configuring-views.md). For example, adding the [`opacity(_:)`](view/opacity(_:).md) modifier to a text view returns a new view with some amount of transparency:

```swift
Text("Hello, World!")
    .opacity(0.5) // Display partially transparent text.
```

The complete list of default modifiers provides a large set of controls for managing views. For example, you can fine tune [`Layout modifiers`](view-layout.md), add [`Accessibility modifiers`](view-accessibility.md) information, and respond to [`Input and event modifiers`](view-input-and-events.md). You can also collect groups of default modifiers into new, custom view modifiers for easy reuse.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is declared in its original declaration. Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt-out the isolation.

## Topics

### Implementing a custom view
- [var body: Self.Body](view/body-8kl5o.md)
  The content and behavior of the view.
- [associatedtype Body : View](view/body-swift.associatedtype.md)
  The type of view representing the body of this view.
- [func modifier<T>(T) -> ModifiedContent<Self, T>](view/modifier(_:).md)
  Applies a modifier to a view and returns a new view.
- [Previews in Xcode](previews-in-xcode.md)
  Generate dynamic, interactive previews of your custom views.
### Configuring view elements
- [Accessibility modifiers](view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md)
  Configure charts that you declare with Swift Charts.
### Drawing views
- [Style modifiers](view-style-modifiers.md)
  Apply built-in styles to different types of views.
- [Layout modifiers](view-layout.md)
  Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.
- [Graphics and rendering modifiers](view-graphics-and-rendering.md)
  Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.
### Providing interactivity
- [Input and event modifiers](view-input-and-events.md)
  Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](view-search.md)
  Enable people to search for content in your app.
- [Presentation modifiers](view-presentation.md)
  Define additional views for the view to present under specified conditions.
- [State modifiers](view-state.md)
  Access storage and provide child views with configuration data.
### Deprecated modifiers
- [Deprecated modifiers](view-deprecated.md)
  Review unsupported modifiers and their replacements.
### Instance Methods
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](view/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [func accessibilityDefaultFocus<Value>(AccessibilityFocusState<Value>.Binding, Value) -> some View](view/accessibilitydefaultfocus(_:_:).md)
  Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.
- [func accessibilityScrollStatus(_:isEnabled:)](view/accessibilityscrollstatus(_:isenabled:).md)
  Changes the announcement provided by accessibility technologies when a user scrolls a scroll view within this view.
- [func accessoryWidgetGroupStyle(AccessoryWidgetGroupStyle) -> some View](view/accessorywidgetgroupstyle(_:).md)
  The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](view/addordertowalletbuttonstyle(_:).md)
  Sets the button’s style.
- [func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View](view/addpasstowalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [func allowsWindowActivationEvents() -> some View](view/allowswindowactivationevents.md)
  Configures gestures in this view hierarchy to handle events that activate the containing window.
- [func appStoreOffer(isPresented: Binding<Bool>, kind: AppStoreOfferKind, onDismiss: ((Result<AppStoreOfferKind.PresentationResult, any Error>) async -> ())?) -> some View](view/appstoreoffer(ispresented:kind:ondismiss:).md)
- [func aspectRatio3D(Size3D?, contentMode: ContentMode) -> some View](view/aspectratio3d(_:contentmode:).md)
  Constrains this view’s dimensions to the specified 3D aspect ratio.
- [func assistiveAccessNavigationIcon(Image) -> some View](view/assistiveaccessnavigationicon(_:).md)
  Configures the view’s icon for purposes of navigation.
- [func assistiveAccessNavigationIcon(systemImage: String) -> some View](view/assistiveaccessnavigationicon(systemimage:).md)
  Configures the view’s icon for purposes of navigation.
- [func attributedTextFormattingDefinition(_:)](view/attributedtextformattingdefinition(_:).md)
  Apply a text formatting definition to all nested editor views.
- [func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View](view/automateddeviceenrollmentaddition(ispresented:).md)
  Presents a modal view that enables users to add devices to their organization.
- [func backgroundExtensionEffect() -> some View](view/backgroundextensioneffect.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func breakthroughEffect(BreakthroughEffect) -> some View](view/breakthrougheffect(_:).md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
- [func buttonSizing(ButtonSizing) -> some View](view/buttonsizing(_:).md)
- [func certificateSheet(trust: Binding<SecTrust?>, title: String?, message: String?, help: URL?) -> some View](view/certificatesheet(trust:title:message:help:).md)
  Displays a certificate sheet using the provided certificate trust.
- [func chart3DCameraProjection(Chart3DCameraProjection) -> some View](view/chart3dcameraprojection(_:).md)
- [func chart3DPose(_:)](view/chart3dpose(_:).md)
- [func chartZAxis(Visibility) -> some View](view/chartzaxis(_:).md)
  Sets the visibility of the z axis.
- [func chartZAxis<Content>(content: () -> Content) -> some View](view/chartzaxis(content:).md)
  Configures the z-axis for 3D charts in the view.
- [func chartZAxisLabel(_:position:alignment:spacing:)](view/chartzaxislabel(_:position:alignment:spacing:).md)
  Adds z axis label for charts in the view. It effects 3D charts only.
- [func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartzscale(domain:range:type:).md)
- [func chartZScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartzscale(domain:type:).md)
- [func chartZScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartzscale(range:type:).md)
- [func chartZSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](view/chartzselection(range:).md)
- [func chartZSelection<P>(value: Binding<P?>) -> some View](view/chartzselection(value:).md)
- [func contactAccessButtonCaption(ContactAccessButton.Caption) -> some View](view/contactaccessbuttoncaption(_:).md)
- [func contactAccessButtonStyle(ContactAccessButton.Style) -> some View](view/contactaccessbuttonstyle(_:).md)
- [func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: ([String]) -> ()) -> some View](view/contactaccesspicker(ispresented:completionhandler:).md)
  Modally present UI which allows the user to select which contacts your app has access to.
- [func containerValue<V>(WritableKeyPath<ContainerValues, V>, V) -> some View](view/containervalue(_:_:).md)
  Sets a particular container value of a view.
- [func contentCaptureProtected(Bool) -> some View](view/contentcaptureprotected(_:).md)
- [func contentToolbar(for:content:)](view/contenttoolbar(for:content:).md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)?) -> some View](view/continuitydevicepicker(ispresented:ondidconnect:).md)
  A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [func controlWidgetActionHint(_:)](view/controlwidgetactionhint(_:).md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](view/controlwidgetstatus(_:).md)
  The status of the control described by the modified label.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](view/currententitlementtask(for:priority:action:).md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func dialogPreventsAppTermination(Bool?) -> some View](view/dialogpreventsapptermination(_:).md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [func dragConfiguration(DragConfiguration) -> some View](view/dragconfiguration(_:).md)
  Configures a drag session.
- [func dragContainer<ItemID, Item, Data>(for: Item.Type, id: (Item) -> ItemID, in: Namespace.ID?, (ItemID) -> Data) -> some View](view/dragcontainer(for:id:in:_:).md)
  A container with draggable views. The drag payload is based on the current selection.
- [func dragContainer(for:id:in:selection:_:)](view/dragcontainer(for:id:in:selection:_:).md)
  A container with single item selection and draggable views. The drag payload is based on the current selection and provided identifiers.
- [func dragContainer<Item, Data>(for: Item.Type, in: Namespace.ID?, (Item.ID) -> Data) -> some View](view/dragcontainer(for:in:_:).md)
  A container with draggable views. The drag payload is identifiable. To form the payload, use the identifier of the dragged view inside the container.
- [func dragContainer(for:in:selection:_:)](view/dragcontainer(for:in:selection:_:).md)
  A container with multiple selection and draggable views. The drag payload is identifiable and is based on the current selection.
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](view/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func draggable<Item>(Item.Type, @autoclosure () -> Item?) -> some View](view/draggable(_:_:).md)
  Activates this view as the source of a drag and drop operation. A view can be dragged separately, or as an element of a drag container.
- [func draggable<ItemID>(containerItemID: ItemID) -> some View](view/draggable(containeritemid:).md)
  Inside a drag container, activates this view as the source of a drag and drop operation. Supports lazy drag containers.
- [func draggable<T, ID>(for: T.Type, id: ID, (ID) -> T?) -> some View](view/draggable(for:id:_:).md)
  Activates this view as the source of a drag-and-drop operation.
- [func dropConfiguration((DropSession) -> DropConfiguration) -> some View](view/dropconfiguration(_:).md)
  Configures a drop session.
- [func dropDestination<T>(for: T.Type, isEnabled: Bool, action: ([T], DropSession) -> Void) -> some View](view/dropdestination(for:isenabled:action:).md)
  Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](view/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [func gameSaveSyncingAlert(directory: Binding<GameSaveSyncedDirectory?>, finishedLoading: () -> Void) -> some View](view/gamesavesyncingalert(directory:finishedloading:).md)
  Presents a modal view while the game synced directory loads.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(_:displaymode:).md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(_:in:displaymode:).md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func glassEffect(Glass, in: some Shape, isEnabled: Bool) -> some View](view/glasseffect(_:in:isenabled:).md)
  Applies the Liquid Glass effect to a view.
- [func glassEffectID((some Hashable & Sendable)?, in: Namespace.ID) -> some View](view/glasseffectid(_:in:).md)
  Associates an identity value to Liquid Glass effects defined within this view.
- [func glassEffectTransition(GlassEffectTransition, isEnabled: Bool) -> some View](view/glasseffecttransition(_:isenabled:).md)
  Associates a glass effect transition with any glass effects defined within this view.
- [func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View](view/glasseffectunion(id:namespace:).md)
  Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [func groupActivityAssociation(GroupActivityAssociationKind?) -> some View](view/groupactivityassociation(_:).md)
  Specifies how a view should be associated with the current SharePlay group activity.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](view/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func handlesGameControllerEvents(matching: GCUIEventTypes) -> some View](view/handlesgamecontrollerevents(matching:).md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
- [func handlesGameControllerEvents(matching: GCUIEventTypes, withOptions: GameControllerEventHandlingOptions?) -> some View](view/handlesgamecontrollerevents(matching:withoptions:).md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view or one of its descendants has focus.
- [func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func healthDataAccessRequest(store: HKHealthStore, readTypes: Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:readtypes:trigger:completion:).md)
  Requests permission to read the specified HealthKit data types.
- [func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:).md)
  Requests permission to save and read the specified HealthKit data types.
- [func imagePlaygroundGenerationStyle(ImagePlaygroundStyle, in: [ImagePlaygroundStyle]) -> some View](view/imageplaygroundgenerationstyle(_:in:).md)
  Sets the generation style for an image playground.
- [func imagePlaygroundPersonalizationPolicy(ImagePlaygroundPersonalizationPolicy) -> some View](view/imageplaygroundpersonalizationpolicy(_:).md)
  Policy determining whether to support the usage of people in the playground or not.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimage:oncompletion:oncancellation:).md)
  Presents the system sheet to create images from the specified input.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:).md)
  Presents the system sheet to create images from the specified input.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimage:oncompletion:oncancellation:).md)
  Presents the system sheet to create images from the specified input.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](view/imageplaygroundsheet(ispresented:concepts:sourceimageurl:oncompletion:oncancellation:).md)
  Presents the system sheet to create images from the specified input.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](view/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.
- [func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?) -> some View](view/inapppurchaseoptions(_:).md)
  Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, journalingSuggestionToken: JournalingSuggestionPresentationToken?, onCompletion: (JournalingSuggestion) async -> Void) -> some View](view/journalingsuggestionspicker(ispresented:journalingsuggestiontoken:oncompletion:).md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, onCompletion: (JournalingSuggestion) async -> Void) -> some View](view/journalingsuggestionspicker(ispresented:oncompletion:).md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [func labelIconToTitleSpacing(CGFloat) -> some View](view/labelicontotitlespacing(_:).md)
  Set the spacing between the icon and title in labels.
- [func labelReservedIconWidth(CGFloat) -> some View](view/labelreservediconwidth(_:).md)
  Set the width reserved for icons in labels.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [func labelsVisibility(Visibility) -> some View](view/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [func lineHeight(AttributedString.LineHeight?) -> some View](view/lineheight(_:).md)
  A modifier for the default line height in the view hierarchy.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](view/listrowinsets(_:_:).md)
  Sets the insets of rows in a list on the specified edges.
- [func listSectionIndexVisibility(Visibility) -> some View](view/listsectionindexvisibility(_:).md)
  Changes the visibility of the list section index.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](view/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>, subscriptionGroupID: String) -> some View](view/managesubscriptionssheet(ispresented:subscriptiongroupid:).md)
- [func managedContentStyle(ManagedContentStyle) -> some View](view/managedcontentstyle(_:).md)
  Applies a managed content style to the view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](view/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](view/manipulable(using:).md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](view/mapcamerakeyframeanimator(trigger:keyframes:).md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func mapControlVisibility(Visibility) -> some View](view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapControls(() -> some View) -> some View](view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View](view/mapfeatureselectionaccessory(_:).md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View](view/mapfeatureselectioncontent(content:).md)
  Specifies a custom presentation for the currently selected feature.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View](view/mapfeatureselectiondisabled(_:).md)
  Specifies which map features should have selection disabled.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](view/mapitemdetailpopover(item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool) -> some View](view/mapitemdetailsheet(ispresented:item:displaysmap:).md)
  Presents a map item detail sheet.
- [func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool) -> some View](view/mapitemdetailsheet(item:displaysmap:).md)
  Presents a map item detail sheet.
- [func mapScope(Namespace.ID) -> some View](view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [func mapStyle(MapStyle) -> some View](view/mapstyle(_:).md)
  Specifies the map style to be used.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some View](view/matchedtransitionsource(id:in:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID, configuration: (EmptyMatchedTransitionSourceConfiguration) -> some MatchedTransitionSourceConfiguration) -> some View](view/matchedtransitionsource(id:in:configuration:).md)
  Identifies this view as the source of a navigation transition, such as a zoom transition.
- [func materialActiveAppearance(MaterialActiveAppearance) -> some View](view/materialactiveappearance(_:).md)
  Sets an explicit active appearance for materials in this view.
- [func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View](view/multilinetextalignment(strategy:).md)
  A modifier for the default text alignment strategy in the view hierarchy.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](view/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](view/onappintentexecution(_:perform:).md)
  Registers a handler to invoke in response to the specified app intent that your app receives.
- [func onApplePayCouponCodeChange(perform: (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View](view/onapplepaycouponcodechange(perform:).md)
  Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View](view/onapplepaypaymentmethodchange(perform:).md)
  Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [func onApplePayShippingContactChange(perform: (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View](view/onapplepayshippingcontactchange(perform:).md)
  Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [func onApplePayShippingMethodChange(perform: (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View](view/onapplepayshippingmethodchange(perform:).md)
  Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [func onCameraCaptureEvent(isEnabled:defaultSoundDisabled:action:)](view/oncameracaptureevent(isenabled:defaultsounddisabled:action:).md)
  Used to register an action triggered by system capture events.
- [func onCameraCaptureEvent(isEnabled:defaultSoundDisabled:primaryAction:secondaryAction:)](view/oncameracaptureevent(isenabled:defaultsounddisabled:primaryaction:secondaryaction:).md)
  Used to register actions triggered by system capture events.
- [func onDragSessionUpdated((DragSession) -> Void) -> some View](view/ondragsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing dragging operation activated by `draggable(_:)` or other drag modifiers.
- [func onDropSessionUpdated((DropSession) -> Void) -> some View](view/ondropsessionupdated(_:).md)
  Specifies an action to perform on each update of an ongoing drop operation activated by `dropDestination(_:)` or other drop modifiers.
- [func onGeometryChange3D(for:of:action:)](view/ongeometrychange3d(for:of:action:).md)
  Returns a new view that arranges to call `action(value)` whenever the value computed by `transform(proxy)` changes, where `proxy` provides access to the view’s 3D geometry properties.
- [func onInAppPurchaseCompletion(perform: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View](view/oninapppurchasecompletion(perform:).md)
  Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View](view/oninapppurchasestart(perform:).md)
  Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [func onMapCameraChange(frequency:_:)](view/onmapcamerachange(frequency:_:).md)
  Performs an action when Map camera framing changes
- [func onOpenURL(prefersInApp: Bool) -> some View](view/onopenurl(prefersinapp:).md)
  Sets an `OpenURLAction` that prefers opening URL with an in-app browser. It’s equivalent to calling `.onOpenURL(_:)`
- [func onWorldRecenter(action:)](view/onworldrecenter(action:).md)
  Adds an action to perform when recentering the view with the digital crown.
- [func payLaterViewAction(PayLaterViewAction) -> some View](view/paylaterviewaction(_:).md)
  Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View](view/paylaterviewdisplaystyle(_:).md)
  Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [func payWithApplePayButtonDisableCardArt() -> some View](view/paywithapplepaybuttondisablecardart.md)
  Sets the features that should be allowed to show on the payment buttons.
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](view/paywithapplepaybuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdges: Edge.Set, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:ispresented:attachmentanchor:arrowedges:action:).md)
  Presents a popover tip on the modified view.
- [func postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func preferredSubscriptionOffer((Product, Product.SubscriptionInfo, [Product.SubscriptionOffer]) -> Product.SubscriptionOffer?) -> some View](view/preferredsubscriptionoffer(_:).md)
  Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [func preferredWindowClippingMargins(_:_:)](view/preferredwindowclippingmargins(_:_:).md)
  Requests additional margins for drawing beyond the bounds of the window.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](view/presentationbreakthrougheffect(_:).md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationPreventsAppTermination(Bool?) -> some View](view/presentationpreventsapptermination(_:).md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [func productDescription(Visibility) -> some View](view/productdescription(_:).md)
  Configure the visibility of labels displaying an in-app purchase product description within the view.
- [func productIconBorder() -> some View](view/producticonborder.md)
  Adds a standard border to an in-app purchase product’s icon .
- [func productViewStyle(some ProductViewStyle) -> some View](view/productviewstyle(_:).md)
  Sets the style for In-App Purchase product views within a view.
- [func realityViewCameraControls(CameraControls) -> some View](view/realityviewcameracontrols(_:).md)
  Adds gestures that control the position and direction of a virtual camera.
- [func realityViewLayoutBehavior(RealityViewLayoutOption) -> some View](view/realityviewlayoutbehavior(_:).md)
  A view modifier that controls the frame sizing and content alignment behavior for `RealityView`
- [func rotation3DLayout(Rotation3D) -> some View](view/rotation3dlayout(_:).md)
  Rotates a view with impacts to its frame in a containing layout
- [func rotation3DLayout(_:axis:)](view/rotation3dlayout(_:axis:).md)
  Rotates a view with impacts to its frame in a containing layout
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Renders the provided content appropriately to be displayed as a custom bar.
- [func scaledToFill3D() -> some View](view/scaledtofill3d.md)
  Scales this view to fill its parent.
- [func scaledToFit3D() -> some View](view/scaledtofit3d.md)
  Scales this view to fit its parent.
- [func scrollEdgeEffectDisabled(Bool, for: Edge.Set) -> some View](view/scrolledgeeffectdisabled(_:for:).md)
  Disables any scroll edge effects for scroll views within this hierarchy.
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [func searchSelection(Binding<TextSelection?>) -> some View](view/searchselection(_:).md)
  Binds the selection of the search field associated with the nearest searchable modifier to the given [`TextSelection`](textselection.md) value.
- [func searchToolbarBehavior(SearchToolbarBehavior) -> some View](view/searchtoolbarbehavior(_:).md)
  Configures the behavior for search in the toolbar.
- [func sectionIndexLabel(_:)](view/sectionindexlabel(_:).md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](view/spatialoverlay(alignment:content:).md)
  Adds secondary views within the 3D bounds of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](view/spatialoverlaypreferencevalue(_:alignment:_:).md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View](view/storebutton(_:for:).md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](view/storeproducttask(for:priority:action:).md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View](view/storeproductstask(for:priority:action:).md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func subscriptionIntroductoryOffer(applyOffer: (Product, Product.SubscriptionInfo) -> Bool, compactJWS: (Product, Product.SubscriptionInfo) async throws -> String) -> some View](view/subscriptionintroductoryoffer(applyoffer:compactjws:).md)
  Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.
- [func subscriptionOfferViewButtonVisibility(Visibility, for: SubscriptionOfferViewButtonKind...) -> some View](view/subscriptionofferviewbuttonvisibility(_:for:).md)
- [func subscriptionOfferViewDetailAction((() -> ())?) -> some View](view/subscriptionofferviewdetailaction(_:).md)
- [func subscriptionOfferViewStyle(some SubscriptionOfferViewStyle) -> some View](view/subscriptionofferviewstyle(_:).md)
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, compactJWS: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> String) -> some View](view/subscriptionpromotionaloffer(offer:compactjws:).md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](view/subscriptionpromotionaloffer(offer:signature:).md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View](view/subscriptionstatustask(for:priority:action:).md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View](view/subscriptionstorebuttonlabel(_:).md)
  Configures subscription store view instances within a view to use the provided button label.
- [func subscriptionStoreControlBackground(_:)](view/subscriptionstorecontrolbackground(_:).md)
  Set a standard effect to use for the background of subscription store view controls within the view.
- [func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo) -> some View) -> some View](view/subscriptionstorecontrolicon(icon:).md)
  Sets a view to use to decorate individual subscription options within a subscription store view.
- [func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) -> some View](view/subscriptionstorecontrolstyle(_:).md)
  Sets the control style for subscription store views within a view.
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some View](view/subscriptionstorecontrolstyle(_:placement:).md)
  Sets the control style and control placement for subscription store views within a view.
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View](view/subscriptionstoreoptiongroupstyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.
- [func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View](view/subscriptionstorepickeritembackground(_:).md)
  Sets the background style for picker items of the subscription store view instances within a view.
- [func subscriptionStorePickerItemBackground(some ShapeStyle, in: some Shape) -> some View](view/subscriptionstorepickeritembackground(_:in:).md)
  Sets the background shape and style for subscription store view picker items within a view.
- [func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind, destination: () -> some View) -> some View](view/subscriptionstorepolicydestination(for:destination:).md)
  Configures a view as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyDestination(url: URL, for: SubscriptionStorePolicyKind) -> some View](view/subscriptionstorepolicydestination(url:for:).md)
  Configures a URL as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View](view/subscriptionstorepolicyforegroundstyle(_:).md)
  Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle) -> some View](view/subscriptionstorepolicyforegroundstyle(_:_:).md)
  Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStoreSignInAction((() -> ())?) -> some View](view/subscriptionstoresigninaction(_:).md)
  Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [func symbolColorRenderingMode(SymbolColorRenderingMode?) -> some View](view/symbolcolorrenderingmode(_:).md)
  Sets the color rendering mode for symbol images.
- [func symbolVariableValueMode(SymbolVariableValueMode?) -> some View](view/symbolvariablevaluemode(_:).md)
  Sets the variable value mode mode for symbol images within this view.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](view/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](view/tabviewbottomaccessory(content:).md)
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool) -> some View](view/tabletopgame(_:parent:automaticupdate:).md)
  Adds a tabletop game to a view.
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool, interaction: (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View](view/tabletopgame(_:parent:automaticupdate:interaction:).md)
  Supplies a closure which returns a new interaction whenever needed.
- [func textContentType(_:)](view/textcontenttype(_:).md)
  Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [func textInputFormattingControlVisibility(Visibility, for: TextInputFormattingControlPlacement.Set) -> some View](view/textinputformattingcontrolvisibility(_:for:).md)
  Define which system text formatting controls are available.
- [func textRenderer<T>(T) -> some View](view/textrenderer(_:).md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](view/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [func tipAnchor<AnchorID>(AnchorID) -> some View](view/tipanchor(_:).md)
  Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [func tipBackground<S>(S) -> some View](view/tipbackground(_:).md)
  Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips.
- [func tipBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/tipbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presented tip.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](view/tipcornerradius(_:antialiased:).md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](view/tipimagesize(_:).md)
  Sets the size for a tip’s image.
- [func tipImageStyle<S>(S) -> some View](view/tipimagestyle(_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](view/tipimagestyle(_:_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/tipimagestyle(_:_:_:).md)
  Sets the style for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](view/tipviewstyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [func toolbarItemHidden(Bool) -> some View](view/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View](view/transactionpicker(ispresented:selection:).md)
  Presents a picker that selects a collection of transactions.
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](view/transactiontask(_:action:).md)
  Provides a task to perform before this view appears
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](view/verifyidentitywithwalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](view/webviewbackforwardnavigationgestures(_:).md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](view/webviewcontentbackground(_:).md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](view/webviewcontextmenu(menu:).md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](view/webviewelementfullscreenbehavior(_:).md)
  Determines whether a web view can display content full screen.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](view/webviewlinkpreviews(_:).md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](view/webviewmagnificationgestures(_:).md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/webviewonscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/webviewscrollinputbehavior(_:for:).md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](view/webviewscrollposition(_:).md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](view/webviewtextselection(_:).md)
  Determines whether to allow people to select or otherwise interact with text.
- [func windowResizeAnchor(UnitPoint?) -> some View](view/windowresizeanchor(_:).md)
  Sets the window anchor point used when the size of the view changes such that the window must resize.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](view/windowtoolbarfullscreenvisibility(_:).md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View](view/workoutpreview(_:ispresented:).md)
  Presents a preview of the workout contents as a modal sheet
- [func writingDirection(strategy: Text.WritingDirectionStrategy) -> some View](view/writingdirection(strategy:).md)
  A modifier for the default text writing direction strategy in the view hierarchy.
- [func writingToolsAffordanceVisibility(Visibility) -> some View](view/writingtoolsaffordancevisibility(_:).md)
  Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [func writingToolsBehavior(WritingToolsBehavior) -> some View](view/writingtoolsbehavior(_:).md)
  Specifies the Writing Tools behavior for text and text input in the environment.

## Relationships

### Inherited By
- [DynamicViewContent](dynamicviewcontent.md)
- [InsettableShape](insettableshape.md)
- [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
- [NSViewRepresentable](nsviewrepresentable.md)
- [Shape](shape.md)
- [ShapeView](shapeview.md)
- [UIViewControllerRepresentable](uiviewcontrollerrepresentable.md)
- [UIViewRepresentable](uiviewrepresentable.md)
- [WKInterfaceObjectRepresentable](wkinterfaceobjectrepresentable.md)
### Conforming Types
- [AngularGradient](angulargradient.md)
- [AnyShape](anyshape.md)
- [AnyView](anyview.md)
- [AsyncImage](asyncimage.md)
- [Button](button.md)
- [ButtonBorderShape](buttonbordershape.md)
- [ButtonStyleConfiguration.Label](buttonstyleconfiguration/label-swift.struct.md)
- [Canvas](canvas.md)
- [Capsule](capsule.md)
- [Circle](circle.md)
- [Color](color.md)
- [ColorPicker](colorpicker.md)
- [ContainerRelativeShape](containerrelativeshape.md)
- [ContentUnavailableView](contentunavailableview.md)
- [ControlGroup](controlgroup.md)
- [ControlGroupStyleConfiguration.Content](controlgroupstyleconfiguration/content-swift.struct.md)
- [ControlGroupStyleConfiguration.Label](controlgroupstyleconfiguration/label-swift.struct.md)
- [DatePicker](datepicker.md)
- [DatePickerStyleConfiguration.Label](datepickerstyleconfiguration/label-swift.struct.md)
- [DebugReplaceableView](debugreplaceableview.md)
- [DefaultButtonLabel](defaultbuttonlabel.md)
- [DefaultDateProgressLabel](defaultdateprogresslabel.md)
- [DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
- [DefaultSettingsLinkLabel](defaultsettingslinklabel.md)
- [DefaultShareLinkLabel](defaultsharelinklabel.md)
- [DefaultTabLabel](defaulttablabel.md)
- [DefaultWindowVisibilityToggleLabel](defaultwindowvisibilitytogglelabel.md)
- [DisclosureGroup](disclosuregroup.md)
- [DisclosureGroupStyleConfiguration.Content](disclosuregroupstyleconfiguration/content-swift.struct.md)
- [DisclosureGroupStyleConfiguration.Label](disclosuregroupstyleconfiguration/label-swift.struct.md)
- [Divider](divider.md)
- [DocumentLaunchView](documentlaunchview.md)
- [EditButton](editbutton.md)
- [EditableCollectionContent](editablecollectioncontent.md)
- [Ellipse](ellipse.md)
- [EllipticalGradient](ellipticalgradient.md)
- [EmptyView](emptyview.md)
- [EquatableView](equatableview.md)
- [FillShapeView](fillshapeview.md)
- [ForEach](foreach.md)
- [Form](form.md)
- [FormStyleConfiguration.Content](formstyleconfiguration/content-swift.struct.md)
- [Gauge](gauge.md)
- [GaugeStyleConfiguration.CurrentValueLabel](gaugestyleconfiguration/currentvaluelabel-swift.struct.md)
- [GaugeStyleConfiguration.Label](gaugestyleconfiguration/label-swift.struct.md)
- [GaugeStyleConfiguration.MarkedValueLabel](gaugestyleconfiguration/markedvaluelabel.md)
- [GaugeStyleConfiguration.MaximumValueLabel](gaugestyleconfiguration/maximumvaluelabel-swift.struct.md)
- [GaugeStyleConfiguration.MinimumValueLabel](gaugestyleconfiguration/minimumvaluelabel-swift.struct.md)
- [GeometryReader](geometryreader.md)
- [GeometryReader3D](geometryreader3d.md)
- [GlassBackgroundEffectConfiguration.Content](glassbackgroundeffectconfiguration/content-swift.struct.md)
- [GlassEffectContainer](glasseffectcontainer.md)
- [Grid](grid.md)
- [GridRow](gridrow.md)
- [Group](group.md)
- [GroupBox](groupbox.md)
- [GroupBoxStyleConfiguration.Content](groupboxstyleconfiguration/content-swift.struct.md)
- [GroupBoxStyleConfiguration.Label](groupboxstyleconfiguration/label-swift.struct.md)
- [GroupElementsOfContent](groupelementsofcontent.md)
- [GroupSectionsOfContent](groupsectionsofcontent.md)
- [HSplitView](hsplitview.md)
- [HStack](hstack.md)
- [HelpLink](helplink.md)
- [Image](image.md)
- [KeyframeAnimator](keyframeanimator.md)
- [Label](label.md)
- [LabelStyleConfiguration.Icon](labelstyleconfiguration/icon-swift.struct.md)
- [LabelStyleConfiguration.Title](labelstyleconfiguration/title-swift.struct.md)
- [LabeledContent](labeledcontent.md)
- [LabeledContentStyleConfiguration.Content](labeledcontentstyleconfiguration/content-swift.struct.md)
- [LabeledContentStyleConfiguration.Label](labeledcontentstyleconfiguration/label-swift.struct.md)
- [LabeledControlGroupContent](labeledcontrolgroupcontent.md)
- [LabeledToolbarItemGroupContent](labeledtoolbaritemgroupcontent.md)
- [LazyHGrid](lazyhgrid.md)
- [LazyHStack](lazyhstack.md)
- [LazyVGrid](lazyvgrid.md)
- [LazyVStack](lazyvstack.md)
- [LinearGradient](lineargradient.md)
- [Link](link.md)
- [List](list.md)
- [Menu](menu.md)
- [MenuButton](menubutton.md)
- [MenuStyleConfiguration.Content](menustyleconfiguration/content.md)
- [MenuStyleConfiguration.Label](menustyleconfiguration/label.md)
- [MeshGradient](meshgradient.md)
- [ModifiedContent](modifiedcontent.md)
- [MultiDatePicker](multidatepicker.md)
- [NavigationLink](navigationlink.md)
- [NavigationSplitView](navigationsplitview.md)
- [NavigationStack](navigationstack.md)
- [NavigationView](navigationview.md)
- [NewDocumentButton](newdocumentbutton.md)
- [OffsetShape](offsetshape.md)
- [OutlineGroup](outlinegroup.md)
- [OutlineSubgroupChildren](outlinesubgroupchildren.md)
- [PasteButton](pastebutton.md)
- [Path](path.md)
- [PhaseAnimator](phaseanimator.md)
- [Picker](picker.md)
- [PlaceholderContentView](placeholdercontentview.md)
- [PresentedWindowContent](presentedwindowcontent.md)
- [PreviewModifierContent](previewmodifiercontent.md)
- [PrimitiveButtonStyleConfiguration.Label](primitivebuttonstyleconfiguration/label-swift.struct.md)
- [ProgressView](progressview.md)
- [ProgressViewStyleConfiguration.CurrentValueLabel](progressviewstyleconfiguration/currentvaluelabel-swift.struct.md)
- [ProgressViewStyleConfiguration.Label](progressviewstyleconfiguration/label-swift.struct.md)
- [RadialGradient](radialgradient.md)
- [Rectangle](rectangle.md)
- [RenameButton](renamebutton.md)
- [RotatedShape](rotatedshape.md)
- [RoundedRectangle](roundedrectangle.md)
- [ScaledShape](scaledshape.md)
- [ScrollView](scrollview.md)
- [ScrollViewReader](scrollviewreader.md)
- [SearchUnavailableContent.Actions](searchunavailablecontent/actions.md)
- [SearchUnavailableContent.Description](searchunavailablecontent/description.md)
- [SearchUnavailableContent.Label](searchunavailablecontent/label.md)
- [Section](section.md)
- [SectionConfiguration.Actions](sectionconfiguration/actions-swift.struct.md)
- [SecureField](securefield.md)
- [SettingsLink](settingslink.md)
- [ShareLink](sharelink.md)
- [Slider](slider.md)
- [Spacer](spacer.md)
- [Stepper](stepper.md)
- [StrokeBorderShapeView](strokebordershapeview.md)
- [StrokeShapeView](strokeshapeview.md)
- [SubscriptionView](subscriptionview.md)
- [Subview](subview.md)
- [SubviewsCollection](subviewscollection.md)
- [SubviewsCollectionSlice](subviewscollectionslice.md)
- [TabContentBuilder.Content](tabcontentbuilder/content.md)
- [TabView](tabview.md)
- [Table](table.md)
- [Text](text.md)
- [TextEditor](texteditor.md)
- [TextField](textfield.md)
- [TextFieldLink](textfieldlink.md)
- [TimelineView](timelineview.md)
- [Toggle](toggle.md)
- [ToggleStyleConfiguration.Label](togglestyleconfiguration/label-swift.struct.md)
- [TransformedShape](transformedshape.md)
- [TupleView](tupleview.md)
- [UnevenRoundedRectangle](unevenroundedrectangle.md)
- [VSplitView](vsplitview.md)
- [VStack](vstack.md)
- [ViewThatFits](viewthatfits.md)
- [WindowVisibilityToggle](windowvisibilitytoggle.md)
- [ZStack](zstack.md)
- [ZStackContent3D](zstackcontent3d.md)

## See Also

- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [struct ViewBuilder](viewbuilder.md)
  A custom parameter attribute that constructs views from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view)*