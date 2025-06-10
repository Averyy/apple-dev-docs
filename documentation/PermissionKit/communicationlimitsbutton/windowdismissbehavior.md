# windowDismissBehavior(_:)

**Framework**: PermissionKit  
**Kind**: method

Configures the dismiss functionality for the window enclosing `self`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func windowDismissBehavior(_ behavior: WindowInteractionBehavior) -> some View
```

#### Discussion

By default, the window dismiss functionality is determined by the scene, as well as any modifiers applied to it.

You can use this modifier to override the default behavior.

For example, you can create a welcome workflow window which disables the dismiss functionality:

```None
struct MyApp: App {
    var body: some Scene {
        ...
        Window("Welcome", id: "welcome") {
            WelcomeView()
                .windowDismissBehavior(.disabled)
        }
    }
}
```

## Parameters

- `behavior`: The dismiss behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/windowdismissbehavior(_:))*