# Preview(_:traits:body:cameras:)

**Framework**: Swiftui  
**Kind**: macro

Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @ViewBuilder body: @escaping @MainActor () -> any View, @PreviewCameraBuilder cameras: () -> [PreviewCamera])
```

#### Overview

This macro behaves like [`Preview(_:traits:_:body:)`](preview(_:traits:_:body:).md) except that it also enables you to specify one or more [`PreviewCamera`](https://developer.apple.com/documentation/DeveloperToolsSupport/PreviewCamera) instances that define custom, fixed viewpoints from which to view the preview:

```swift
#Preview {
    ContentView()
} cameras: {
    PreviewCamera(from: .bottomLeadingBack, name: "Corner 1")
    PreviewCamera(from: .topTrailingFront, name: "Corner 2")
}
```

If you use one of the preview macros that doesn’t include a `cameras` closure, the canvas displays the preview from the front by default. It also provides a camera picker to choose other standard, fixed viewpoints — like the top or the back. When you do specify one or more preview cameras, the canvas adds a submenu to the camera picker that lists the viewpoints that you define, like Corner 1 and Corner 2 in the above example. The canvas also displays the preview from the first of these custom viewpoints by default when it loads the preview.

> **Note**: In addition to using fixed camera perspectives, you can also interactively alter the viewpoint of a preview in the canvas using controls like those that Simulator provides. For more information, see doc://com.apple.documentation/documentation/visionOS/interacting-with-your-app-in-the-visionos-simulator.

Other preview macros provide different customization options. For example, if you want to preview the view as it would appear in a particular kind of scene, you can use [`Preview(_:immersionStyle:traits:body:cameras:)`](preview(_:immersionstyle:traits:body:cameras:).md) or [`Preview(_:windowStyle:traits:body:cameras:)`](preview(_:windowstyle:traits:body:cameras:).md).

## Parameters

- `name`: An optional display name for the preview. If you don’t specify a   name, the canvas labels the preview using the line number where the   preview appears in source.
- `traits`: An optional list of     instances that customize the appearance of the preview.
- `body`: A   that produces a SwiftUI view to preview. You   typically specify one of your app’s custom views and optionally any   inputs, model data, modifiers, and enclosing views that the custom   view needs for normal operation.
- `cameras`: One or more preview cameras that indicate the custom, fixed   viewpoints that you want to be able to view the preview from. The first   of these replaces the front viewpoint as the default.

## See Also

- [macro Preview(String?, body: () -> any View)](preview(_:body:).md)
  Creates a preview of a SwiftUI view.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>, PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:traits:_:body:).md)
  Creates a preview of a SwiftUI view using the specified traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/preview(_:traits:body:cameras:))*