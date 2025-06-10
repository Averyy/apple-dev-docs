# Accessible appearance

**Framework**: SwiftUI

Enhance the legibility of content in your app’s interface.

#### Overview

Make content easier for people to see by making it larger, giving it greater contrast, or reducing the amount of distracting motion.

![None](https://docs-assets.developer.apple.com/published/798b84460063f228cc1996fef3379310/accessible-appearance-hero%402x.png)

For design guidance, see [`Accessibility`](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility) in the Accessibility section of the Human Interface Guidelines.

## Topics

### Managing color
- [func accessibilityIgnoresInvertColors(Bool) -> some View](view/accessibilityignoresinvertcolors(_:).md)
  Sets whether this view should ignore the system Smart Invert setting.
- [var accessibilityInvertColors: Bool](environmentvalues/accessibilityinvertcolors.md)
  Whether the system preference for Invert Colors is enabled.
- [var accessibilityDifferentiateWithoutColor: Bool](environmentvalues/accessibilitydifferentiatewithoutcolor.md)
  Whether the system preference for Differentiate without Color is enabled.
### Enlarging content
- [func accessibilityShowsLargeContentViewer() -> some View](view/accessibilityshowslargecontentviewer.md)
  Adds a default large content view to be shown by the large content viewer.
- [func accessibilityShowsLargeContentViewer<V>(() -> V) -> some View](view/accessibilityshowslargecontentviewer(_:).md)
  Adds a custom large content view to be shown by the large content viewer.
- [var accessibilityLargeContentViewerEnabled: Bool](environmentvalues/accessibilitylargecontentviewerenabled.md)
  Whether the Large Content Viewer is enabled.
### Improving legibility
- [var accessibilityShowButtonShapes: Bool](environmentvalues/accessibilityshowbuttonshapes.md)
  Whether the system preference for Show Button Shapes is enabled.
- [var accessibilityReduceTransparency: Bool](environmentvalues/accessibilityreducetransparency.md)
  Whether the system preference for Reduce Transparency is enabled.
- [var legibilityWeight: LegibilityWeight?](environmentvalues/legibilityweight.md)
  The font weight to apply to text.
- [enum LegibilityWeight](legibilityweight.md)
  The Accessibility Bold Text user setting options.
### Minimizing motion
- [var accessibilityDimFlashingLights: Bool](environmentvalues/accessibilitydimflashinglights.md)
  Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [var accessibilityPlayAnimatedImages: Bool](environmentvalues/accessibilityplayanimatedimages.md)
  Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [var accessibilityReduceMotion: Bool](environmentvalues/accessibilityreducemotion.md)
  Whether the system preference for Reduce Motion is enabled.
### Using assistive access
- [var accessibilityAssistiveAccessEnabled: Bool](environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [struct AssistiveAccess](assistiveaccess.md)
  A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.

## See Also

- [Accessibility fundamentals](accessibility-fundamentals.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Accessible controls](accessible-controls.md)
  Improve access to actions that your app can undertake.
- [Accessible descriptions](accessible-descriptions.md)
  Describe interface elements to help people understand what they represent.
- [Accessible navigation](accessible-navigation.md)
  Enable users to navigate to specific user interface elements using rotors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessible-appearance)*