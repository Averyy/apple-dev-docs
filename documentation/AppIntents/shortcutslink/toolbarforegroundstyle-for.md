# toolbarForegroundStyle(_:for:)

**Framework**: App Intents  
**Kind**: method

Specifies the preferred foreground style of bars managed by SwiftUI.

**Availability**:
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarForegroundStyle<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

#### Discussion

This examples shows a view that renders the navigation bar with a blue foreground color.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Blue")
        .toolbarForegroundStyle(
            .blue, for: .navigationBar)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/toolbarforegroundstyle(_:for:))*