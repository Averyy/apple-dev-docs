# immersionStyle(selection:in:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func immersionStyle(selection: Binding<any ImmersionStyle>, in styles: any ImmersionStyle...) -> some Scene
```

#### Return Value

A scene that uses one of the specified `styles`.

#### Discussion

Use this modifier to configure the appearance and behavior of an [`ImmersiveSpace`](immersivespace.md). Specify a style that conforms to the [`ImmersionStyle`](immersionstyle.md) protocol, like [`mixed`](immersionstyle/mixed.md) or [`full`](immersionstyle/full.md). For example, the following app defines a solar system scene that uses full immersion:

```swift
@main
struct SolarSystemApp: App {
    @State private var style: ImmersionStyle = .full

    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
        .immersionStyle(selection: $style, in: .full)
    }
}
```

## Parameters

- `selection`: A   to the style that the space uses. You can   change this value to change the scene’s style even after you   present the immersive space. Even though you provide a binding,   the value changes only if you change it.
- `styles`: The list of styles that the   input can have.   Include any styles that you plan to use during the lifetime   of the scene.

## See Also

- [struct ImmersiveSpace](immersivespace.md)
  A scene that presents its content in an unbounded space.
- [struct ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md)
  A result builder for composing a collection of immersive space elements.
- [protocol ImmersionStyle](immersionstyle.md)
  The styles that an immersive space can have.
- [var immersiveSpaceDisplacement: Pose3D](environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/immersionstyle(selection:in:))*