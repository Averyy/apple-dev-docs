# Preview(_:immersionStyle:traits:body:)

**Framework**: SwiftUI  
**Kind**: macro

Creates a preview of a SwiftUI view in an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<Style>(_ name: String? = nil, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., @ViewBuilder body: @escaping @MainActor () -> any View) where Style : ImmersionStyle
```

#### Overview

This preview macro behaves like [`Preview(_:traits:_:body:)`](preview(_:traits:_:body:).md), except that it also enables you to define a scene context for the view. Specifically, it places the view in an immersive space with the specified immersion style, like the [`mixed`](immersionstyle/mixed.md) style:

```swift
#Preview("Mixed immersive space", immersionStyle: .mixed) {
   ContentView()
}
```

Use this preview macro when the view needs scene context to behave as it would during normal operation of your app.

Other preview macros provide different customization options. For example, if you want to see how the view appears in a window rather than an immersive space, you can use [`Preview(_:windowStyle:traits:body:)`](preview(_:windowstyle:traits:body:).md). If you want to add custom, fixed viewpoints to an immersive space preview, use [`Preview(_:immersionStyle:traits:body:cameras:)`](preview(_:immersionstyle:traits:body:cameras:).md).

## Parameters

- `name`: An optional display name for the preview. If you don’t specify a   name, the canvas labels the preview using the line number where the   preview appears in source.
- `immersionStyle`: The   to use for the preview. Use this   input to display the view as if it appears in an immersive space   that has the specified style.
- `traits`: An optional list of     instances that customize the appearance of the preview.
- `body`: A   that produces a SwiftUI view to preview. You   typically specify one of your app’s custom views and optionally any   inputs, model data, modifiers, and enclosing views that the custom   view needs for normal operation.

## See Also

- [macro Preview<Style>(String?, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:immersionstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:windowstyle:traits:body:).md)
  Creates a preview of a SwiftUI view in a window.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:windowstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preview(_:immersionstyle:traits:body:))*