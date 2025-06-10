# View configuration

**Framework**: SwiftUI

Adjust the characteristics of views in a hierarchy.

#### Overview

SwiftUI enables you to tune the appearance and behavior of views using view modifiers.

![None](https://docs-assets.developer.apple.com/published/4f97c3ff1212e8df86b49977696cabfe/view-configuration-hero%402x.png)

Many modifiers apply to specific kinds of views or behaviors, but some apply more generally. For example, you can conditionally hide any view by dynamically setting its opacity, display contextual help when people hover over a view, or request the light or dark appearance for a view.

## Topics

### Hiding views
- [func opacity(Double) -> some View](view/opacity(_:).md)
  Sets the transparency of this view.
- [func hidden() -> some View](view/hidden.md)
  Hides this view unconditionally.
### Hiding system elements
- [func labelsHidden() -> some View](view/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](view/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](view/labelsvisibility(_:).md).
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func statusBarHidden(Bool) -> some View](view/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [enum Visibility](visibility.md)
  The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.
### Managing view interaction
- [func disabled(Bool) -> some View](view/disabled(_:).md)
  Adds a condition that controls whether users can interact with this view.
- [var isEnabled: Bool](environmentvalues/isenabled.md)
  A Boolean value that indicates whether the view associated with this environment allows user interaction.
- [func interactionActivityTrackingTag(String) -> some View](view/interactionactivitytrackingtag(_:).md)
  Sets a tag that you use for tracking interactivity.
- [func invalidatableContent(Bool) -> some View](view/invalidatablecontent(_:).md)
  Mark the receiver as their content might be invalidated.
### Providing contextual help
- [func help(_:)](view/help(_:).md)
  Adds help text to a view using a text view that you provide.
### Detecting and requesting the light or dark appearance
- [func preferredColorScheme(ColorScheme?) -> some View](view/preferredcolorscheme(_:).md)
  Sets the preferred color scheme for this presentation.
- [var colorScheme: ColorScheme](environmentvalues/colorscheme.md)
  The color scheme of this environment.
- [enum ColorScheme](colorscheme.md)
  The possible color schemes, corresponding to the light and dark appearances.
### Getting the color scheme contrast
- [var colorSchemeContrast: ColorSchemeContrast](environmentvalues/colorschemecontrast.md)
  The contrast associated with the color scheme of this environment.
- [enum ColorSchemeContrast](colorschemecontrast.md)
  The contrast between the app’s foreground and background colors.
### Configuring passthrough
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some View](view/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [struct SurroundingsEffect](surroundingseffect.md)
  Effects that the system can apply to passthrough video.
- [struct BreakthroughEffect](breakthrougheffect.md)
### Redacting private content
- [Designing your app for the Always On state](../watchOS-Apps/designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [func privacySensitive(Bool) -> some View](view/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.
- [struct RedactionReasons](redactionreasons.md)
  The reasons to apply a redaction to data displayed on screen.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-configuration)*