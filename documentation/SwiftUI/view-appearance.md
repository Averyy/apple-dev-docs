# Appearance modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Configure a view’s foreground and background styles, controls, and visibility.

#### Overview

Use these modifiers to configure the appearance of a view, including the use of color and tint, and the application of overlays and background elements. Control the visibility of a view and specific elements within a view. Manage the shape and size of various controls.

For information about configuring views, see [View configuration](./view-configuration.md).

## Topics

### Colors and patterns
- [func backgroundStyle<S>(S) -> some View](./view/backgroundstyle%28_%29.md)
  Sets the specified style to render backgrounds within the view.
- [func foregroundStyle<S>(S) -> some View](./view/foregroundstyle%28_%29.md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](./view/foregroundstyle%28_,_%29.md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](./view/foregroundstyle%28_,_,_%29.md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](./view/alloweddynamicrange%28_%29.md)
  Returns a new view configured with the specified allowed dynamic range.
### Tint
- [func tint(_:)](./view/tint%28_%29.md)
  Sets the tint color within this view.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](./view/listrowseparatortint%28_,edges%29.md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](./view/listsectionseparatortint%28_,edges%29.md)
  Sets the tint color associated with a section.
- [func listItemTint(_:)](./view/listitemtint%28_%29.md)
  Sets a fixed tint color for content in a list.
### Light and dark appearance
- [func preferredColorScheme(ColorScheme?) -> some View](./view/preferredcolorscheme%28_%29.md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](./view/preferredsurroundingseffect%28_%29.md)
  Applies an effect to passthrough video.
### Foreground elements
- [func border<S>(S, width: CGFloat) -> some View](./view/border%28_,width%29.md)
  Adds a border to this view with the specified style and width.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./view/overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./view/overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [func spatialOverlay<V>(alignment: Alignment3D, content: () -> V) -> some View](./view/spatialoverlay%28alignment,content%29.md)
  Adds secondary views within the 3D bounds of this view.
- [func spatialOverlayPreferenceValue<K, V>(K.Type, alignment: Alignment3D, (K.Value) -> V) -> some View](./view/spatialoverlaypreferencevalue%28_,alignment,_%29.md)
  Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.
### Background elements
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./view/background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](./view/background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](./view/background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](./view/alternatingrowbackgrounds%28_%29.md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func listRowBackground<V>(V?) -> some View](./view/listrowbackground%28_%29.md)
  Places a custom background view behind a list row item.
- [func scrollContentBackground(Visibility) -> some View](./view/scrollcontentbackground%28_%29.md)
  Specifies the visibility of the background for scrollable views within this view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./view/containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./view/containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](./view/glassbackgroundeffect%28displaymode%29.md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(S, displayMode: GlassBackgroundDisplayMode) -> some View](./view/glassbackgroundeffect%28_,displaymode%29.md)
  Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](./view/glassbackgroundeffect%28in,displaymode%29.md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [func glassBackgroundEffect<T, S>(S, in: T, displayMode: GlassBackgroundDisplayMode) -> some View](./view/glassbackgroundeffect%28_,in,displaymode%29.md)
  Fills the view’s background with a custom glass background effect and a shape that you specify.
- [func backgroundExtensionEffect() -> some View](./view/backgroundextensioneffect%28%29.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [func backgroundExtensionEffect(isEnabled: Bool) -> some View](./view/backgroundextensioneffect%28isenabled%29.md)
  Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
### Passthrough
- [func breakthroughEffect(BreakthroughEffect) -> some View](./view/breakthrougheffect%28_%29.md)
  Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.
### Control configuration
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](./view/defaultwheelpickeritemheight%28_%29.md)
  Sets the default wheel-style picker item height.
- [func horizontalRadioGroupLayout() -> some View](./view/horizontalradiogrouplayout%28%29.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func controlSize(_:)](./view/controlsize%28_%29.md)
  Sets the size for controls within this view.
- [func buttonBorderShape(ButtonBorderShape) -> some View](./view/buttonbordershape%28_%29.md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](./view/buttonrepeatbehavior%28_%29.md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func headerProminence(Prominence) -> some View](./view/headerprominence%28_%29.md)
  Sets the header prominence for this view.
- [func scrollDisabled(Bool) -> some View](./view/scrolldisabled%28_%29.md)
  Disables or enables scrolling in scrollable views.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](./view/scrollbouncebehavior%28_,axes%29.md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](./view/scrollindicatorsflash%28onappear%29.md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](./view/scrollindicatorsflash%28trigger%29.md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func menuOrder(MenuOrder) -> some View](./view/menuorder%28_%29.md)
  Sets the preferred order of items for menus presented from this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](./view/menuactiondismissbehavior%28_%29.md)
  Tells a menu whether to dismiss after performing an action.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](./view/paletteselectioneffect%28_%29.md)
  Specifies the selection effect to apply to a palette item.
- [func typeSelectEquivalent(_:)](./view/typeselectequivalent%28_%29.md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
### Symbol effects
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](./view/symboleffect%28_,options,isactive%29.md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](./view/symboleffect%28_,options,value%29.md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](./view/symboleffectsremoved%28_%29.md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
### Privacy and redaction
- [func privacySensitive(Bool) -> some View](./view/privacysensitive%28_%29.md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](./view/redacted%28reason%29.md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](./view/unredacted%28%29.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func invalidatableContent(Bool) -> some View](./view/invalidatablecontent%28_%29.md)
  Mark the receiver as their content might be invalidated.
- [func contentCaptureProtected(Bool) -> some View](./view/contentcaptureprotected%28_%29.md)
### Visibility
- [func hidden() -> some View](./view/hidden%28%29.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](./view/labelshidden%28%29.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](./view/labelsvisibility%28_%29.md)
  Controls the visibility of labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](./view/menuindicator%28_%29.md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](./view/listrowseparator%28_,edges%29.md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](./view/listsectionseparator%28_,edges%29.md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionIndexVisibility(Visibility) -> some View](./view/listsectionindexvisibility%28_%29.md)
  Changes the visibility of the list section index.
- [func persistentSystemOverlays(Visibility) -> some View](./view/persistentsystemoverlays%28_%29.md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](./view/scrollindicators%28_,axes%29.md)
  Sets the visibility of scroll indicators within this view.
- [func scrollClipDisabled(Bool) -> some View](./view/scrollclipdisabled%28_%29.md)
  Sets whether a scroll view clips its content to its bounds.
- [func sliderThumbVisibility(Visibility) -> some View](./view/sliderthumbvisibility%28_%29.md)
  Sets the thumb visibility for `Slider`s within this view.
- [func tableColumnHeaders(Visibility) -> some View](./view/tablecolumnheaders%28_%29.md)
  Controls the visibility of a `Table`’s column header views.
- [func upperLimbVisibility(Visibility) -> some View](./view/upperlimbvisibility%28_%29.md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](./immersivespace.md) scene is presented.
- [func volumeBaseplateVisibility(Visibility) -> some View](./view/volumebaseplatevisibility%28_%29.md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
### Sensory feedback
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](./view/sensoryfeedback%28_,trigger%29.md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback(trigger:_:)](./view/sensoryfeedback%28trigger,_%29.md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](./view/sensoryfeedback%28_,trigger,condition%29.md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
### Widget configuration
- [func widgetAccentable(Bool) -> some View](./view/widgetaccentable%28_%29.md)
  Adds the view and all of its subviews to the accented group.
- [func widgetCurvesContent(Bool) -> some View](./view/widgetcurvescontent%28_%29.md)
  Displays the widget’s content along a curve if the context allows it.
- [func widgetLabel(_:)](./view/widgetlabel%28_%29.md)
  Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [func widgetLabel<Label>(label: () -> Label) -> some View](./view/widgetlabel%28label%29.md)
  Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](./view/dynamicisland%28verticalplacement%29.md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [func accessoryWidgetGroupStyle(AccessoryWidgetGroupStyle) -> some View](./view/accessorywidgetgroupstyle%28_%29.md)
  The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
- [func controlWidgetActionHint(_:)](./view/controlwidgetactionhint%28_%29.md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](./view/controlwidgetstatus%28_%29.md)
  The status of the control described by the modified label.
### Window behaviors
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](./view/windowdismissbehavior%28_%29.md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](./view/windowfullscreenbehavior%28_%29.md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](./view/windowtoolbarfullscreenvisibility%28_%29.md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](./view/windowminimizebehavior%28_%29.md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeAnchor(UnitPoint?) -> some View](./view/windowresizeanchor%28_%29.md)
  Sets the window anchor point used when the size of the view changes such that the window must resize.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](./view/windowresizebehavior%28_%29.md)
  Configures the resize functionality for the window enclosing `self`.
- [func preferredWindowClippingMargins(_:_:)](./view/preferredwindowclippingmargins%28_,_%29.md)
  Requests additional margins for drawing beyond the bounds of the window.

## See Also

### Configuring view elements
- [Accessibility modifiers](./view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Text and symbol modifiers](./view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](./view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](./view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-appearance)*