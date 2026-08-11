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
### Modifying technology-specific views
- [Technology-specific modifiers](view-technology-modifiers.md)
  Add modifiers to customize SwiftUI views that other Apple frameworks provide.
### Deprecated modifiers
- [Deprecated modifiers](view-deprecated.md)
  Review unsupported modifiers and their replacements.
### Instance Methods
- [func presentationPlacement(PresentationPlacement) -> some View](view/presentationplacement(_:).md)
  Sets the placement of a presentation within the presenting view.

## Relationships

### Inherited By
- [DynamicViewContent](dynamicviewcontent.md)
- [InsettableShape](insettableshape.md)
- [NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
- [NSViewRepresentable](nsviewrepresentable.md)
- [RoundedRectangularShape](roundedrectangularshape.md)
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
- [ConcentricRectangle](concentricrectangle.md)
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
- [DefaultGlassEffectShape](defaultglasseffectshape.md)
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
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
- [TextInputBorderShape](textinputbordershape.md)
- [TimelineView](timelineview.md)
- [Toggle](toggle.md)
- [ToggleStyleConfiguration.Label](togglestyleconfiguration/label-swift.struct.md)
- [TransformedShape](transformedshape.md)
- [TupleContent](tuplecontent.md)
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
- [Wishlist: Planning travel in a SwiftUI app](wishlist-planning-travel-in-a-swiftui-app.md)
  Build a travel planning app that organizes trips into collections and tracks activity completion.
- [typealias ContentBuilder](contentbuilder.md)
  A custom parameter attribute that constructs views and other content types from closures.
- [struct ViewBuilder](viewbuilder.md)
  A custom parameter attribute that constructs views from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view)*