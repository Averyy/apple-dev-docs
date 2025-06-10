# Appearance modifiers

**Framework**: SwiftUI

Configure a view’s foreground and background styles, controls, and visibility.

#### Overview

Use these modifiers to configure the appearance of a view, including the use of color and tint, and the application of overlays and background elements. Control the visibility of a view and specific elements within a view. Manage the shape and size of various controls.

For information about configuring views, see [`View configuration`](view-configuration.md).

## Topics

### Colors and patterns
- [func backgroundStyle<S>(S) -> some View](view/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func allowedDynamicRange(Image.DynamicRange?) -> some View](view/alloweddynamicrange(_:).md)
  Returns a new view configured with the specified allowed dynamic range.
### Tint
- [func tint(_:)](view/tint(_:).md)
  Sets the tint color within this view.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listItemTint(_:)](view/listitemtint(_:).md)
  Sets a fixed tint color for content in a list.
### Light and dark appearance
- [func preferredColorScheme(ColorScheme?) -> some View](view/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](view/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
### Foreground elements
- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
### Background elements
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](view/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some View](view/alternatingrowbackgrounds(_:).md)
  Overrides whether lists and tables in this view have alternating row backgrounds.
- [func listRowBackground<V>(V?) -> some View](view/listrowbackground(_:).md)
  Places a custom background view behind a list row item.
- [func scrollContentBackground(Visibility) -> some View](view/scrollcontentbackground(_:).md)
  Specifies the visibility of the background for scrollable views within this view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](view/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](view/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func glassBackgroundEffect(displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(displaymode:).md)
  Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [func glassBackgroundEffect<S>(in: S, displayMode: GlassBackgroundDisplayMode) -> some View](view/glassbackgroundeffect(in:displaymode:).md)
  Fills the view’s background with an automatic glass background effect and a shape that you specify.
### Control configuration
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](view/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [func horizontalRadioGroupLayout() -> some View](view/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func controlSize(_:)](view/controlsize(_:).md)
  Sets the size for controls within this view.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](view/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [func headerProminence(Prominence) -> some View](view/headerprominence(_:).md)
  Sets the header prominence for this view.
- [func scrollDisabled(Bool) -> some View](view/scrolldisabled(_:).md)
  Disables or enables scrolling in scrollable views.
- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](view/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](view/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](view/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func menuOrder(MenuOrder) -> some View](view/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](view/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](view/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [func typeSelectEquivalent(_:)](view/typeselectequivalent(_:).md)
  Sets an explicit type select equivalent text in a collection, such as a list or table.
### Symbol effects
- [func symbolEffect<T>(T, options: SymbolEffectOptions, isActive: Bool) -> some View](view/symboleffect(_:options:isactive:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffect<T, U>(T, options: SymbolEffectOptions, value: U) -> some View](view/symboleffect(_:options:value:).md)
  Returns a new view with a symbol effect added to it.
- [func symbolEffectsRemoved(Bool) -> some View](view/symboleffectsremoved(_:).md)
  Returns a new view with its inherited symbol image effects either removed or left unchanged.
### Privacy and redaction
- [func privacySensitive(Bool) -> some View](view/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func invalidatableContent(Bool) -> some View](view/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
### Visibility
- [func hidden() -> some View](view/hidden.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](view/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](view/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollClipDisabled(Bool) -> some View](view/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func tableColumnHeaders(Visibility) -> some View](view/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func upperLimbVisibility(Visibility) -> some View](view/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](immersivespace.md) scene is presented.
- [func volumeBaseplateVisibility(Visibility) -> some View](view/volumebaseplatevisibility(_:).md)
  Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.
### Sensory feedback
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](view/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback(trigger:_:)](view/sensoryfeedback(trigger:_:).md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](view/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
### Widget configuration
- [func widgetAccentable(Bool) -> some View](view/widgetaccentable(_:).md)
  Adds the view and all of its subviews to the accented group.
- [func widgetCurvesContent(Bool) -> some View](view/widgetcurvescontent(_:).md)
  Displays the widget’s content along a curve if the context allows it.
- [func widgetLabel(_:)](view/widgetlabel(_:).md)
  Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [func widgetLabel<Label>(label: () -> Label) -> some View](view/widgetlabel(label:).md)
  Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](view/dynamicisland(verticalplacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
### Window behaviors
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](view/windowdismissbehavior(_:).md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](view/windowfullscreenbehavior(_:).md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](view/windowminimizebehavior(_:).md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](view/windowresizebehavior(_:).md)
  Configures the resize functionality for the window enclosing `self`.

## See Also

- [Accessibility modifiers](view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Text and symbol modifiers](view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-appearance)*