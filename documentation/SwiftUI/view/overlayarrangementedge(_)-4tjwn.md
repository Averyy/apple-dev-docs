# overlayArrangementEdge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The vertical edge a view in an overlay arrangement aligns to when the arrangement transitions to a portrait orientation.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
nonisolated
func overlayArrangementEdge(_ edge: VerticalEdge?) -> some View
```

**Other overloads**:

```swift
nonisolated
func overlayArrangementEdge(_ edge: HorizontalEdge?) -> some View
```

## Discussion

Use this modifier to anchor the given view when its overlay layout transitions into a portrait orientation. For example, to move the view to the top side of the arrangement view, use the [`VerticalEdge.top`](../verticaledge/top.md) edge.

```swift
var body: some View {
    ArrangementView {
        ControlsView()
            .overlayArrangementEdge(.top)
    } secondary: {
        ContentView()
    }
}
```

## Parameters

- `edge`: The vertical edge against which the arrangement aligns the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlayarrangementedge(_:)-4tjwn)*