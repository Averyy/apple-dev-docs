# windowToolbarLabelStyle(fixed:)

**Framework**: SwiftUI  
**Kind**: method

Sets the label style of items in a toolbar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func windowToolbarLabelStyle(fixed: ToolbarLabelStyle) -> some Scene
```

#### Discussion

Use this modifier to set a static [`ToolbarLabelStyle`](toolbarlabelstyle.md) the toolbar should use. The style will not be configurable by the user.

```swift
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .toolbar(id: "browserToolbar") {
                        ...
                    }
            }
            .windowToolbarLabelStyle(fixed: .iconOnly)
        }
    }
```

## See Also

- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [func windowToolbarLabelStyle(Binding<ToolbarLabelStyle>) -> some Scene](scene/windowtoolbarlabelstyle(_:).md)
  Sets the label style of items in a toolbar and enables user customization.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowtoolbarlabelstyle(fixed:))*