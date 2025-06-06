# Preview(_:immersionStyle:traits:body:cameras:)

**Framework**: SwiftUI  
**Kind**: macro

Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<Style>(_ name: String? = nil, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., @ViewBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera]) where Style : ImmersionStyle
```

#### Overview

This preview macro behaves like [`Preview(_:immersionStyle:traits:body:)`](preview(_:immersionstyle:traits:body:).md) combined with [`Preview(_:traits:body:cameras:)`](preview(_:traits:body:cameras:).md): it enables you to define an immersive space scene context for the view, and also to define custom, fixed viewpoints for the preview:

```swift
#Preview("Mixed immersive space", immersionStyle: .mixed) {
   ContentView()
} cameras: {
   PreviewCamera(from: .front)
   PreviewCamera(from: .top, zoom: 2)
   PreviewCamera(from: .leading, zoom: 0.5, name: "close up")
}
```

See those other preview macros for more information about using scenes and cameras in your preview. If you want to preview in a window rather than an immersive space, use [`Preview(_:windowStyle:traits:body:cameras:)`](preview(_:windowstyle:traits:body:cameras:).md).

## Parameters

- `name`: An optional display name for the preview. If you don’t specify a   name, the canvas labels the preview using the line number where the   preview appears in source.
- `immersionStyle`: The   to use for the preview. Use this   input to display the view as if it appears in an immersive space   that has the specified style.
- `traits`: An optional list of     instances that customize the appearance of the preview.
- `body`: A   that produces a SwiftUI view to preview. You   typically specify one of your app’s custom views and optionally any   inputs, model data, modifiers, and enclosing views that the custom   view needs for normal operation.
- `cameras`: One or more preview cameras that indicate the custom, fixed   viewpoints that you want to be able to view the preview from. The first   of these replaces the front viewpoint as the default.

## See Also

- [macro Preview<Style>(String?, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:immersionstyle:traits:body:).md)
  Creates a preview of a SwiftUI view in an immersive space.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:windowstyle:traits:body:).md)
  Creates a preview of a SwiftUI view in a window.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:windowstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preview(_:immersionstyle:traits:body:cameras:))*