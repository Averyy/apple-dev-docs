# background(ignoresSafeAreaEdges:)

**Framework**: App Intents  
**Kind**: method

Sets the view’s background to the default background style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
```

#### Return Value

A view with the `ShapeStyle/background` shape style drawn behind it.

#### Discussion

This modifier behaves like `View/background(_:ignoresSafeAreaEdges:)`, except that it always uses the `ShapeStyle/background` shape style. For example, you can add a background to a `Label`:

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background()
}
```

Without the background modifier, the teal color behind the label shows through the label. With the modifier, the label’s text and icon appear backed by a region filled with a color that’s appropriate for light or dark appearance:

If you want to specify a `View` or a stack of views as the background, use `View/background(alignment:content:)` instead. To specify a `Shape` or `InsettableShape`, use `View/background(_:in:fillStyle:)`. To configure the background of a presentation, like a sheet, use `View/presentationBackground(_:)`.

## Parameters

- `edges`: The set of edges for which to ignore safe area insets   when adding the background. The default value is  .   Specify an empty set to respect safe area insets on all edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/background(ignoressafeareaedges:))*