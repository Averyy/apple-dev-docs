# toolbarForegroundStyle(_:for:)

**Framework**: FinanceKitUI  
**Kind**: method

Specifies the preferred foreground style of bars managed by SwiftUI.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarForegroundStyle<S>(_ style: S, for bars: ToolbarPlacement...) -> some View where S : ShapeStyle
```

#### Discussion

This examples shows a view that renders the navigation bar with a blue foreground color.

```None
NavigationStack {
    ContentView()
        .navigationTitle("Blue")
        .toolbarForegroundStyle(
            .blue, for: .navigationBar)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/toolbarforegroundstyle(_:for:))*