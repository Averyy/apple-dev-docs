# ImmersiveSpaceContentBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A result builder for composing a collection of immersive space elements.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct ImmersiveSpaceContentBuilder
```

## Topics

### Building content
- [static func buildBlock<Content>(Content) -> Content](./immersivespacecontentbuilder/buildblock%28_%29.md)

## See Also

### Creating an immersive space
- [struct ImmersiveSpace](./immersivespace.md)
  A scene that presents its content in an unbounded space.
- [func immersionStyle(selection: Binding<any ImmersionStyle>, in: any ImmersionStyle...) -> some Scene](./scene/immersionstyle%28selection,in%29.md)
  Sets the style for an immersive space.
- [protocol ImmersionStyle](./immersionstyle.md)
  The styles that an immersive space can have.
- [var immersiveSpaceDisplacement: Pose3D](./environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [struct ImmersiveEnvironmentBehavior](./immersiveenvironmentbehavior.md)
  The behavior of the system-provided immersive environments when a scene is opened by your app.
- [struct ProgressiveImmersionAspectRatio](./progressiveimmersionaspectratio.md)
  The shape of the portal that a progressive immersion style opens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespacecontentbuilder)*