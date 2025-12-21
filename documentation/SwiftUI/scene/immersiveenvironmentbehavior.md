# immersiveEnvironmentBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the immersive environment behavior that should apply when this scene opens.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func immersiveEnvironmentBehavior(_ behavior: ImmersiveEnvironmentBehavior) -> some Scene
```

#### Return Value

A scene that uses the specified `behavior`.

#### Discussion

Use this modifier to control how the immersive environment behaves when an [`ImmersiveSpace`](immersivespace.md) is opened, that uses an immersion style that supports keeping the immersive environment visible.

For example, the following app defines an Immersive Space that displays an interactive car engine model, and by setting the system environment behavior to `.coexist`, the immersive environment can remain shown while inspecting the details of the engine:

```swift
@main
struct App: App {
    var body: some Scene {
        ImmersiveSpace {
            CarEngineModel()
        }
        .immersiveEnvironmentBehavior(.coexist)
    }
}
```

Note: The behavior is a preference and does not always have to be honored by the system.

## Parameters

- `behavior`: A immersive environment behavior that should be applied by   the system when this scene opens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/immersiveenvironmentbehavior(_:))*