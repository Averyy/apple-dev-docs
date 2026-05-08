# appearsActive

**Framework**: SwiftUI  
**Kind**: property

Whether views and styles in this environment should prefer an active appearance over an inactive appearance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 10.15+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@backDeployed(before: macOS 15.0)
var appearsActive: Bool { get set }
```

#### Discussion

On macOS, views in the focused window (also referred to as the “key” window) should appear active. Some contexts also appear active in other circumstances, such as the contents of a window toolbar appearing active when the window is not focused but is the main window.

Typical adjustments made when a view does not appear active include:

- Uses of `Color.accentColor` should generally be removed or replaced with a desaturated style.
- Text and image content in sidebars should appear dimmer.
- Buttons with destructive actions should appear disabled.
- `ShapeStyle.selection` and selection in list and tables will automatically become a grey color

Custom views, styles, and shape styles can use this to adjust their own appearance:

```swift
struct ProminentPillButtonStyle: ButtonStyle {
    @Environment(\.appearsActive) private var appearsActive

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .lineLimit(1)
            .padding(.horizontal, 8)
            .padding(.vertical, 2)
            .frame(minHeight: 20)
            .overlay(Capsule().strokeBorder(.tertiary))
            .background(appearsActive ? Color.accentColor : .clear, in: .capsule)
            .contentShape(.capsule)
    }
}
```

On all other platforms, this value is always `true`.

This is bridged with `UITraitCollection.activeAppearance` for UIKit hosted content.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/appearsactive)*