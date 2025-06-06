# windowResizeBehavior(_:)

**Framework**: RealityKit  
**Kind**: method

Configures the resize functionality for the window enclosing `self`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowResizeBehavior(_ behavior: WindowInteractionBehavior) -> some View
```

#### Discussion

By default, the window resizability functionality is determined by the scene, as well as any modifiers applied to it. Additionally, when using the `Scene/windowResizability(_:)` modifier, the minimum and maximum size of the window’s contents will also determine the resizability behavior.

You can use this modifier to override the default behavior.

For example, you can create a custom “About” window which only allows for dismissal:

```None
struct MyApp: App {
    var body: some Scene {
        ...
        Window("About MyApp", id: "about") {
            AboutView()
                .windowResizeBehavior(.disabled)
                .windowMinimizeBehavior(.disabled)
        }
        .windowResizability(.contentSize)
    }
}
```

## Parameters

- `behavior`: The resize behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/windowresizebehavior(_:))*