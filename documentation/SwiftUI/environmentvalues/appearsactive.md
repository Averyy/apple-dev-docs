# appearsActive

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

### Display characteristics
- [var colorScheme: ColorScheme](./colorscheme.md)
  The color scheme of this environment.
- [var colorSchemeContrast: ColorSchemeContrast](./colorschemecontrast.md)
  The contrast associated with the color scheme of this environment.
- [var displayScale: CGFloat](./displayscale.md)
  The display scale of this environment.
- [var horizontalSizeClass: UserInterfaceSizeClass?](./horizontalsizeclass.md)
  The horizontal size class of this environment.
- [var imageScale: Image.Scale](./imagescale.md)
  The image scale for this environment.
- [var pixelLength: CGFloat](./pixellength.md)
  The size of a pixel on the screen.
- [var sidebarRowSize: SidebarRowSize](./sidebarrowsize.md)
  The current size of sidebar rows.
- [var verticalSizeClass: UserInterfaceSizeClass?](./verticalsizeclass.md)
  The vertical size class of this environment.
- [var immersiveSpaceDisplacement: Pose3D](./immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [var labelsVisibility: Visibility](./labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](../view/labelsvisibility%28_%29.md).
- [var materialActiveAppearance: MaterialActiveAppearance](./materialactiveappearance.md)
  The behavior materials should use for their active state, defaulting to `automatic`.
- [struct TabBarPlacement](../tabbarplacement.md)
  A placement for tabs in a tab view.
- [var toolbarLabelStyle: ToolbarLabelStyle?](./toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [var toolbarVerticalEdge: HorizontalEdge?](./toolbarverticaledge.md)
  This value reflects the system’s preferred edge for the vertical bar in the current context, regardless of whether a vertical bar is currently visible. Use it to position custom bars or other UI relative to the system’s bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/appearsactive)*