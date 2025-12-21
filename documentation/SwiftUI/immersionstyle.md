# ImmersionStyle

**Framework**: SwiftUI  
**Kind**: protocol

The styles that an immersive space can have.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
protocol ImmersionStyle
```

#### Overview

Configure the appearance and behavior of an [`ImmersiveSpace`](immersivespace.md) by adding the [`immersionStyle(selection:in:)`](scene/immersionstyle(selection:in:).md) scene modifier to the space and specifying a style that conforms to this protocol, like [`mixed`](immersionstyle/mixed.md) or [`full`](immersionstyle/full.md). For example, the following app defines a solar system scene that uses full immersion:

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

## Topics

### Getting built-in styles
- [static var automatic: AutomaticImmersionStyle](immersionstyle/automatic.md)
  The default immersion style.
- [static var full: FullImmersionStyle](immersionstyle/full.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [static var mixed: MixedImmersionStyle](immersionstyle/mixed.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [static var progressive: ProgressiveImmersionStyle](immersionstyle/progressive.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
### Supporting types
- [struct AutomaticImmersionStyle](automaticimmersionstyle.md)
  The default style of immersive spaces.
- [struct FullImmersionStyle](fullimmersionstyle.md)
  An immersion style that displays unbounded content that completely replaces passthrough video.
- [struct MixedImmersionStyle](mixedimmersionstyle.md)
  An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [struct ProgressiveImmersionStyle](progressiveimmersionstyle.md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
### Type Methods
- [static progressive(_:initialAmount:)](immersionstyle/progressive(_:initialamount:).md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
- [static progressive(_:initialAmount:aspectRatio:)](immersionstyle/progressive(_:initialamount:aspectratio:).md)
  An immersion style that displays unbounded content that partially replaces passthrough video.
- [static func progressive(aspectRatio: ProgressiveImmersionAspectRatio) -> ProgressiveImmersionStyle](immersionstyle/progressive(aspectratio:).md)
  An immersion style that displays unbounded content that partially replaces passthrough video.

## Relationships

### Conforming Types
- [AutomaticImmersionStyle](automaticimmersionstyle.md)
- [FullImmersionStyle](fullimmersionstyle.md)
- [MixedImmersionStyle](mixedimmersionstyle.md)
- [ProgressiveImmersionStyle](progressiveimmersionstyle.md)

## See Also

- [struct ImmersiveSpace](immersivespace.md)
  A scene that presents its content in an unbounded space.
- [struct ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md)
  A result builder for composing a collection of immersive space elements.
- [func immersionStyle(selection: Binding<any ImmersionStyle>, in: any ImmersionStyle...) -> some Scene](scene/immersionstyle(selection:in:).md)
  Sets the style for an immersive space.
- [var immersiveSpaceDisplacement: Pose3D](environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [struct ImmersiveEnvironmentBehavior](immersiveenvironmentbehavior.md)
  The behavior of the system-provided immersive environments when a scene is opened by your app.
- [struct ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionstyle)*