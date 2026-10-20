# windowToolbarLabelStyle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the label style of items in a toolbar and enables user customization.

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
func windowToolbarLabelStyle(_ toolbarLabelStyle: Binding<ToolbarLabelStyle>) -> some Scene
```

#### Discussion

Use this modifier to bind a [`ToolbarLabelStyle`](../toolbarlabelstyle.md) to [`AppStorage`](../appstorage.md). The toolbar will default to the label style specified but will also be user configurable.

```swift
    @main
    struct MyApp: App {
        @AppStorage("ToolbarLabelStyle")
        private var labelStyle: ToolbarLabelStyle = .iconOnly

        var body: some Scene {
            WindowGroup {
                ContentView()
                    .toolbar(id: "browserToolbar") {
                        ...
                    }
            }
            .windowToolbarLabelStyle($labelStyle)
        }
    }
```

## Parameters

- `toolbarLabelStyle`: The label style to apply.

## See Also

### Styling the associated toolbar
- [func windowToolbarStyle<S>(S) -> some Scene](./windowtoolbarstyle%28_%29.md)
  Sets the style for the toolbar defined within this scene.
- [func windowToolbarLabelStyle(fixed: ToolbarLabelStyle) -> some Scene](./windowtoolbarlabelstyle%28fixed%29.md)
  Sets the label style of items in a toolbar.
- [protocol WindowToolbarStyle](../windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/windowtoolbarlabelstyle(_:))*