# ProgressiveImmersionAspectRatio

**Framework**: SwiftUI  
**Kind**: struct

The shape of the portal that a progressive immersion style opens.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ProgressiveImmersionAspectRatio
```

#### Overview

A progressive immersive space replaces passthrough inside a portal that people resize with the Digital Crown. Pass a value of this type to [`progressive(aspectRatio:)`](immersionstyle/progressive(aspectratio:).md) to ask for a wide or a tall portal, which lets the shape suit the content you show:

```swift
@main
struct MatchApp: App {
    @State private var style: any ImmersionStyle =
        .progressive(aspectRatio: .landscape)

    var body: some Scene {
        ImmersiveSpace {
            MatchView()
        }
        .immersionStyle(selection: $style, in: style)
    }
}
```

The system chooses a shape for you when you pass [`automatic`](progressiveimmersionaspectratio/automatic.md).

## Topics

### Type Properties
- [static var automatic: ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio/automatic.md)
  The system will choose a default portal aspect ratio.
- [static var landscape: ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio/landscape.md)
  The portal will be wide.
- [static var portrait: ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio/portrait.md)
  The portal will be tall.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ImmersiveSpace](immersivespace.md)
  A scene that presents its content in an unbounded space.
- [struct ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md)
  A result builder for composing a collection of immersive space elements.
- [func immersionStyle(selection: Binding<any ImmersionStyle>, in: any ImmersionStyle...) -> some Scene](scene/immersionstyle(selection:in:).md)
  Sets the style for an immersive space.
- [protocol ImmersionStyle](immersionstyle.md)
  The styles that an immersive space can have.
- [var immersiveSpaceDisplacement: Pose3D](environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [struct ImmersiveEnvironmentBehavior](immersiveenvironmentbehavior.md)
  The behavior of the system-provided immersive environments when a scene is opened by your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressiveimmersionaspectratio)*