# toolbarVerticalEdge

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

This value reflects the system’s preferred edge for the vertical bar in the current context, regardless of whether a vertical bar is currently visible. Use it to position custom bars or other UI relative to the system’s bar placement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
var toolbarVerticalEdge: HorizontalEdge? { get }
```

#### Discussion

This value is read-only; the system determines the edge based on locale and device.

Returns `nil` on devices and in contexts where the system never places a vertical bar — for example hardware without a vertical bar, or a size class or orientation in which no vertical bar is used.

```swift
struct ContentView: View {
    @Environment(\.toolbarVerticalEdge) var toolbarVerticalEdge

    var body: some View {
        FloatingToolPalette()
            .frame(maxWidth: .infinity,
                   alignment: toolbarVerticalEdge == .trailing
                       ? .trailing : .leading)
    }
}
```

## See Also

### Display characteristics
- [var appearsActive: Bool](./appearsactive.md)
  Whether views and styles in this environment should prefer an active appearance over an inactive appearance.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarverticaledge)*