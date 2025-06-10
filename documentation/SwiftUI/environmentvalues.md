# EnvironmentValues

**Framework**: SwiftUI  
**Kind**: struct

A collection of environment values propagated through a view hierarchy.

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
struct EnvironmentValues
```

#### Overview

SwiftUI exposes a collection of values to your app’s views in an `EnvironmentValues` structure. To read a value from the structure, declare a property using the [`Environment`](environment.md) property wrapper and specify the value’s key path. For example, you can read the current locale:

```swift
@Environment(\.locale) var locale: Locale
```

Use the property you declare to dynamically control a view’s layout. SwiftUI automatically sets or updates many environment values, like [`pixelLength`](environmentvalues/pixellength.md), [`scenePhase`](environmentvalues/scenephase.md), or [`locale`](environmentvalues/locale.md), based on device characteristics, system state, or user settings. For others, like [`lineLimit`](environmentvalues/linelimit.md), SwiftUI provides a reasonable default value.

You can set or override some values using the [`environment(_:_:)`](view/environment(_:_:).md) view modifier:

```swift
MyView()
    .environment(\.lineLimit, 2)
```

The value that you set affects the environment for the view that you modify — including its descendants in the view hierarchy — but only up to the point where you apply a different environment modifier.

SwiftUI provides dedicated view modifiers for setting some values, which typically makes your code easier to read. For example, rather than setting the [`lineLimit`](environmentvalues/linelimit.md) value directly, as in the previous example, you should instead use the [`lineLimit(_:)`](view/linelimit(_:).md) modifier:

```swift
MyView()
    .lineLimit(2)
```

In some cases, using a dedicated view modifier provides additional functionality. For example, you must use the [`preferredColorScheme(_:)`](view/preferredcolorscheme(_:).md) modifier rather than setting [`colorScheme`](environmentvalues/colorscheme.md) directly to ensure that the new value propagates up to the presenting container when presenting a view like a popover:

```swift
MyView()
    .popover(isPresented: $isPopped) {
        PopoverContent()
            .preferredColorScheme(.dark)
    }
```

Create a custom environment value by declaring a new property in an extension to the environment values structure and applying the [`Entry()`](entry().md) macro to the variable declaration:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
}

extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

Clients of your value then access the value in the usual way, reading it with the [`Environment`](environment.md) property wrapper, and setting it with the `myCustomValue` view modifier.

## Topics

### Creating and accessing values
- [init()](environmentvalues/init.md)
  Creates an environment values instance.
- [subscript(_:)](environmentvalues/subscript(_:).md)
  Accesses the environment value associated with a custom key.
- [var description: String](environmentvalues/description.md)
  A string that represents the contents of the environment values instance.
### Accessibility
- [var accessibilityAssistiveAccessEnabled: Bool](environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [var accessibilityDimFlashingLights: Bool](environmentvalues/accessibilitydimflashinglights.md)
  Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [var accessibilityDifferentiateWithoutColor: Bool](environmentvalues/accessibilitydifferentiatewithoutcolor.md)
  Whether the system preference for Differentiate without Color is enabled.
- [var accessibilityEnabled: Bool](environmentvalues/accessibilityenabled.md)
  A Boolean value that indicates whether the user has enabled an assistive technology.
- [var accessibilityInvertColors: Bool](environmentvalues/accessibilityinvertcolors.md)
  Whether the system preference for Invert Colors is enabled.
- [var accessibilityLargeContentViewerEnabled: Bool](environmentvalues/accessibilitylargecontentviewerenabled.md)
  Whether the Large Content Viewer is enabled.
- [var accessibilityPlayAnimatedImages: Bool](environmentvalues/accessibilityplayanimatedimages.md)
  Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [var accessibilityPrefersHeadAnchorAlternative: Bool](environmentvalues/accessibilityprefersheadanchoralternative.md)
  Whether the system setting to prefer alternatives to head-anchored content is on.
- [var accessibilityQuickActionsEnabled: Bool](environmentvalues/accessibilityquickactionsenabled.md)
  A Boolean that indicates whether the quick actions feature is enabled.
- [var accessibilityReduceMotion: Bool](environmentvalues/accessibilityreducemotion.md)
  Whether the system preference for Reduce Motion is enabled.
- [var accessibilityReduceTransparency: Bool](environmentvalues/accessibilityreducetransparency.md)
  Whether the system preference for Reduce Transparency is enabled.
- [var accessibilityShowButtonShapes: Bool](environmentvalues/accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var accessibilitySwitchControlEnabled: Bool](environmentvalues/accessibilityswitchcontrolenabled.md)
  A Boolean value that indicates whether the Switch Control motor accessibility feature is in use.
- [var accessibilityVoiceOverEnabled: Bool](environmentvalues/accessibilityvoiceoverenabled.md)
  A Boolean value that indicates whether the VoiceOver screen reader is in use.
- [var legibilityWeight: LegibilityWeight?](environmentvalues/legibilityweight.md)
  The font weight to apply to text.
### Actions
- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [var openImmersiveSpace: OpenImmersiveSpaceAction](environmentvalues/openimmersivespace.md)
  An action that presents an immersive space.
- [var dismissImmersiveSpace: DismissImmersiveSpaceAction](environmentvalues/dismissimmersivespace.md)
  An immersive space dismissal action stored in a view’s environment.
- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [var openURL: OpenURLAction](environmentvalues/openurl.md)
  An action that opens a URL.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [var pushWindow: PushWindowAction](environmentvalues/pushwindow.md)
  A window presentation action stored in a view’s environment.
- [var purchase: PurchaseAction](environmentvalues/purchase.md)
  An action that starts an in-app purchase.
- [var refresh: RefreshAction?](environmentvalues/refresh.md)
  A refresh action stored in a view’s environment.
- [var rename: RenameAction?](environmentvalues/rename.md)
  An action that activates the standard rename interaction.
- [var resetFocus: ResetFocusAction](environmentvalues/resetfocus.md)
  An action that requests the focus system to reevaluate default focus.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.
### Authentication
- [var authorizationController: AuthorizationController](environmentvalues/authorizationcontroller.md)
  A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [var webAuthenticationSession: WebAuthenticationSession](environmentvalues/webauthenticationsession.md)
  A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.
### Controls and input
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [var keyboardShortcut: KeyboardShortcut?](environmentvalues/keyboardshortcut.md)
  The keyboard shortcut that buttons in this environment will be triggered with.
- [var menuIndicatorVisibility: Visibility](environmentvalues/menuindicatorvisibility.md)
  The menu indicator visibility to apply to controls within a view.
- [var menuOrder: MenuOrder](environmentvalues/menuorder.md)
  The preferred order of items for menus presented from this view.
- [var searchSuggestionsPlacement: SearchSuggestionsPlacement](environmentvalues/searchsuggestionsplacement.md)
  The current placement of search suggestions.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [var preferredPencilSqueezeAction: PencilPreferredAction](environmentvalues/preferredpencilsqueezeaction.md)
  The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
### Display characteristics
- [var appearsActive: Bool](environmentvalues/appearsactive.md)
  Whether views and styles in this environment should prefer an active appearance over an inactive appearance.
- [var colorScheme: ColorScheme](environmentvalues/colorscheme.md)
  The color scheme of this environment.
- [var colorSchemeContrast: ColorSchemeContrast](environmentvalues/colorschemecontrast.md)
  The contrast associated with the color scheme of this environment.
- [var displayScale: CGFloat](environmentvalues/displayscale.md)
  The display scale of this environment.
- [var horizontalSizeClass: UserInterfaceSizeClass?](environmentvalues/horizontalsizeclass.md)
  The horizontal size class of this environment.
- [var imageScale: Image.Scale](environmentvalues/imagescale.md)
  The image scale for this environment.
- [var pixelLength: CGFloat](environmentvalues/pixellength.md)
  The size of a pixel on the screen.
- [var sidebarRowSize: SidebarRowSize](environmentvalues/sidebarrowsize.md)
  The current size of sidebar rows.
- [var verticalSizeClass: UserInterfaceSizeClass?](environmentvalues/verticalsizeclass.md)
  The vertical size class of this environment.
- [var immersiveSpaceDisplacement: Pose3D](environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [var labelsVisibility: Visibility](environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](view/labelsvisibility(_:).md).
- [var materialActiveAppearance: MaterialActiveAppearance](environmentvalues/materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct TabBarPlacement](tabbarplacement.md)
  A placement for tabs in a tab view.
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
### Global objects
- [var calendar: Calendar](environmentvalues/calendar.md)
  The current calendar that views should use when handling dates.
- [var documentConfiguration: DocumentConfiguration?](environmentvalues/documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [var locale: Locale](environmentvalues/locale.md)
  The current locale that views should use.
- [var managedObjectContext: NSManagedObjectContext](environmentvalues/managedobjectcontext.md)
- [var modelContext: ModelContext](environmentvalues/modelcontext.md)
  The SwiftData model context that will be used for queries and other model operations within this environment.
- [var timeZone: TimeZone](environmentvalues/timezone.md)
  The current time zone that views should use when handling dates.
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.
### Scrolling
- [var isScrollEnabled: Bool](environmentvalues/isscrollenabled.md)
  A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.
- [var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md)
  The visibility to apply to scroll indicators of any horizontally scrollable content.
- [var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md)
  The visiblity to apply to scroll indicators of any vertically scrollable content.
- [var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md)
  The way that scrollable content interacts with the software keyboard.
- [var horizontalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md)
  The scroll bounce mode for the horizontal axis of scrollable views.
- [var verticalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md)
  The scroll bounce mode for the vertical axis of scrollable views.
### State
- [var editMode: Binding<EditMode>?](environmentvalues/editmode.md)
  An indication of whether the user can edit the contents of a view associated with this environment.
- [var isActivityFullscreen: Bool](environmentvalues/isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [var isEnabled: Bool](environmentvalues/isenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [var isFocused: Bool](environmentvalues/isfocused.md)
  Returns whether the nearest focusable ancestor has focus.
- [var isFocusEffectEnabled: Bool](environmentvalues/isfocuseffectenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows focus effects to be displayed.
- [var isHoverEffectEnabled: Bool](environmentvalues/ishovereffectenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [var isLuminanceReduced: Bool](environmentvalues/isluminancereduced.md)
  A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [var isPresented: Bool](environmentvalues/ispresented.md)
  A Boolean value that indicates whether the view associated with this environment is currently presented.
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.
- [var isSearching: Bool](environmentvalues/issearching.md)
  A Boolean value that indicates when the user is searching.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [var scenePhase: ScenePhase](environmentvalues/scenephase.md)
  The current phase of the scene.
- [var supportsMultipleWindows: Bool](environmentvalues/supportsmultiplewindows.md)
  A Boolean value that indicates whether the current platform supports opening multiple windows.
### StoreKit configuration
- [var displayStoreKitMessage: DisplayMessageAction](environmentvalues/displaystorekitmessage.md)
- [var requestReview: RequestReviewAction](environmentvalues/requestreview.md)
### Text styles
- [var allowsTightening: Bool](environmentvalues/allowstightening.md)
  A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [var autocorrectionDisabled: Bool](environmentvalues/autocorrectiondisabled.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var dynamicTypeSize: DynamicTypeSize](environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [var font: Font?](environmentvalues/font.md)
  The default font of this environment.
- [var layoutDirection: LayoutDirection](environmentvalues/layoutdirection.md)
  The layout direction associated with the current environment.
- [var lineLimit: Int?](environmentvalues/linelimit.md)
  The maximum number of lines that text can occupy in a view.
- [var lineSpacing: CGFloat](environmentvalues/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [var minimumScaleFactor: CGFloat](environmentvalues/minimumscalefactor.md)
  The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [var multilineTextAlignment: TextAlignment](environmentvalues/multilinetextalignment.md)
  An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.
- [var textCase: Text.Case?](environmentvalues/textcase.md)
  A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [var truncationMode: Text.TruncationMode](environmentvalues/truncationmode.md)
  A value that indicates how the layout truncates the last line of text to fit into the available space.
- [var textSelectionAffinity: TextSelectionAffinity](environmentvalues/textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
### View attributes
- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [var backgroundStyle: AnyShapeStyle?](environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [var contentTransition: ContentTransition](environmentvalues/contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](environmentvalues/contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a list.
- [var headerProminence: Prominence](environmentvalues/headerprominence.md)
  The prominence to apply to section headers within a view.
- [var physicalMetrics: PhysicalMetricsConverter](environmentvalues/physicalmetrics.md)
  The physical metrics associated with a scene.
- [var realityKitScene: Scene?](environmentvalues/realitykitscene.md)
- [var realityViewCameraControls: CameraControls](environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var springLoadingBehavior: SpringLoadingBehavior](environmentvalues/springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.
- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [var symbolVariants: SymbolVariants](environmentvalues/symbolvariants.md)
  The symbol variant to use in this environment.
- [var worldTrackingLimitations: Set<WorldTrackingLimitation>](environmentvalues/worldtrackinglimitations.md)
  The current limitations of the device tracking the user’s surroundings.
### Widgets
- [var showsWidgetContainerBackground: Bool](environmentvalues/showswidgetcontainerbackground.md)
  An environment variable that indicates whether the background of a widget appears.
- [var showsWidgetLabel: Bool](environmentvalues/showswidgetlabel.md)
  A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [var widgetFamily: WidgetFamily](environmentvalues/widgetfamily.md)
  The template of the widget — small, medium, or large.
- [var widgetRenderingMode: WidgetRenderingMode](environmentvalues/widgetrenderingmode.md)
  The widget’s rendering mode, based on where the system is displaying it.
- [var widgetContentMargins: EdgeInsets](environmentvalues/widgetcontentmargins.md)
  A property that identifies the content margins of a widget.
### Deprecated environment values
- [var disableAutocorrection: Bool?](environmentvalues/disableautocorrection.md)
  A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [var sizeCategory: ContentSizeCategory](environmentvalues/sizecategory.md)
  The size of content.
- [var presentationMode: Binding<PresentationMode>](environmentvalues/presentationmode.md)
  A binding to the current presentation mode of the view associated with this environment.
- [struct PresentationMode](presentationmode.md)
  An indication whether a view is currently presented by another view.
- [var complicationRenderingMode: ComplicationRenderingMode](environmentvalues/complicationrenderingmode.md)
  The complication rendering mode for the current environment.
- [var controlActiveState: ControlActiveState](environmentvalues/controlactivestate.md)
  The active appearance expected of controls in a window.
### Instance Properties
- [var activityFamily: ActivityFamily](environmentvalues/activityfamily.md)
  The size family of the current Live Activity.
- [var buttonSizing: ButtonSizing](environmentvalues/buttonsizing.md)
- [var controlSize: ControlSize](environmentvalues/controlsize-3sgmh.md)
  The size to apply to controls within a view.
- [var controlSize: ControlSize](environmentvalues/controlsize-9ixbk.md)
  The size to apply to controls within a view.
- [var credentialExportManager: ASCredentialExportManager](environmentvalues/credentialexportmanager.md)
  This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [var credentialImportManager: ASCredentialImportManager](environmentvalues/credentialimportmanager.md)
  This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:
- [var devicePickerSupports: DevicePickerSupportedAction](environmentvalues/devicepickersupports.md)
  Checks for support to present a DevicePicker.
- [var findContext: FindContext?](environmentvalues/findcontext.md)
- [var fontResolutionContext: Font.Context](environmentvalues/fontresolutioncontext.md)
  Information used to resolve a font.
- [var imagePlaygroundAllowedGenerationStyles: [ImagePlaygroundStyle]](environmentvalues/imageplaygroundallowedgenerationstyles.md)
- [var imagePlaygroundPersonalizationPolicy: ImagePlaygroundPersonalizationPolicy](environmentvalues/imageplaygroundpersonalizationpolicy.md)
- [var imagePlaygroundSelectedGenerationStyle: ImagePlaygroundStyle](environmentvalues/imageplaygroundselectedgenerationstyle.md)
- [var isActivityUpdateReduced: Bool](environmentvalues/isactivityupdatereduced.md)
  A Boolean value that indicates whether the Live Activity update synchronization rate is reduced.
- [var isUserAuthenticationEnabled: Bool](environmentvalues/isuserauthenticationenabled.md)
  The current system user authentication enablement status.
- [var labelIconToTitleSpacing: CGFloat?](environmentvalues/labelicontotitlespacing.md)
  The spacing between the icon and title of a label.
- [var labelReservedIconWidth: CGFloat?](environmentvalues/labelreservediconwidth.md)
  The width reserved for icons in labels.
- [var levelOfDetail: LevelOfDetail](environmentvalues/levelofdetail.md)
  The level of detail the view is recommended to have.
- [var lineHeight: AttributedString.LineHeight?](environmentvalues/lineheight.md)
  The default line height for text influenced by this environment.
- [var navigationLinkIndicatorVisibility: Visibility](environmentvalues/navigationlinkindicatorvisibility.md)
  A value that says whether a built-in navigation link would show a disclosure indicator in the current context.
- [var remoteDeviceIdentifier: RemoteDeviceIdentifier?](environmentvalues/remotedeviceidentifier.md)
  An opaque object that identifies the device on which the scene (from which this value is accessed from) is being presented on.
- [var requestAgeRange: DeclaredAgeRangeAction](environmentvalues/requestagerange.md)
  The property in the environment for adoption of the age range API.
- [var supportedActivityFamilies: Set<ActivityFamily>](environmentvalues/supportedactivityfamilies.md)
  An environment value that that indicates potential rendered family for a Live Activity.
- [var supportsImagePlayground: Bool](environmentvalues/supportsimageplayground.md)
  A Boolean value that indicates whether image generation is available on the current device.
- [var supportsRemoteScenes: Bool](environmentvalues/supportsremotescenes.md)
  Indicates if the current device supports presenting a [`RemoteImmersiveSpace`](remoteimmersivespace.md) on a remote device.
- [var surfaceSnappingInfo: SurfaceSnappingInfo](environmentvalues/surfacesnappinginfo.md)
  Provides information about the current snap state of the scene.
- [var symbolColorRenderingMode: SymbolColorRenderingMode?](environmentvalues/symbolcolorrenderingmode.md)
  The property specifying how symbol images fill their layers, or nil to use the default fill style.
- [var symbolVariableValueMode: SymbolVariableValueMode?](environmentvalues/symbolvariablevaluemode.md)
  The current symbol variable value mode, or `nil` denoting that the mode is picked automatically.
- [var tabBarPlacement: TabBarPlacement?](environmentvalues/tabbarplacement.md)
  The current placement of the tab bar.
- [var tabViewBottomAccessoryPlacement: TabViewBottomAccessoryPlacement?](environmentvalues/tabviewbottomaccessoryplacement.md)
  The current placement of the tab view bottom accessory.
- [var windowClippingMargins: EdgeInsets3D](environmentvalues/windowclippingmargins.md)
- [var writingToolsBehavior: WritingToolsBehavior?](environmentvalues/writingtoolsbehavior.md)
  The current Writing Tools behavior for text and text input.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [struct Environment](environment.md)
  A property wrapper that reads a value from a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues)*