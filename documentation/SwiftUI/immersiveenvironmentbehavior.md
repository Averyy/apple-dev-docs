# ImmersiveEnvironmentBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The behavior of the system-provided immersive environments when a scene is opened by your app.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct ImmersiveEnvironmentBehavior
```

## Overview

Use one of these values with the [`immersiveEnvironmentBehavior(_:)`](./scene/immersiveenvironmentbehavior%28_%29.md) scene modifier to indicate how the immersive environment should behave when your app opens a scene.

## Topics

### Type Properties
- [static var automatic: ImmersiveEnvironmentBehavior](./immersiveenvironmentbehavior/automatic.md)
  A behavior that matches the system default behavior.
- [static var coexist: ImmersiveEnvironmentBehavior](./immersiveenvironmentbehavior/coexist.md)
  A behavior that keeps the system’s immersive environment as is when opening a scene.
- [static var replace: ImmersiveEnvironmentBehavior](./immersiveenvironmentbehavior/replace.md)
  A behavior that replaces any currently opened immersive environment with the new scene.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating an immersive space
- [struct ImmersiveSpace](./immersivespace.md)
  A scene that presents its content in an unbounded space.
- [struct ImmersiveSpaceContentBuilder](./immersivespacecontentbuilder.md)
  A result builder for composing a collection of immersive space elements.
- [func immersionStyle(selection: Binding<any ImmersionStyle>, in: any ImmersionStyle...) -> some Scene](./scene/immersionstyle%28selection,in%29.md)
  Sets the style for an immersive space.
- [protocol ImmersionStyle](./immersionstyle.md)
  The styles that an immersive space can have.
- [var immersiveSpaceDisplacement: Pose3D](./environmentvalues/immersivespacedisplacement.md)
  The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [struct ProgressiveImmersionAspectRatio](./progressiveimmersionaspectratio.md)
  The shape of the portal that a progressive immersion style opens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersiveenvironmentbehavior)*