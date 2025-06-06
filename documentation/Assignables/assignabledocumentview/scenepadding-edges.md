# scenePadding(_:edges:)

**Framework**: Assignables  
**Kind**: method

Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func scenePadding(_ padding: ScenePadding, edges: Edge.Set = .all) -> some View
```

#### Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

#### Discussion

Use this modifier to add a scene-appropriate amount of padding to a view. Specify either a single edge value from `Edge/Set`, or an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root view of a window. In watchOS, use scene padding to align elements of your user interface with top level elements, like the title of a navigation view. For example, compare the effects of different kinds of padding on text views presented inside a `NavigationView` in watchOS:

```None
VStack(alignment: .leading, spacing: 10) {
    Text("Minimum Scene padding")
        .scenePadding(.minimum, edges: .horizontal)
        .border(.red) // Border added for reference.
    Text("Navigation Bar Scene padding")
        .scenePadding(.navigationBar, edges: .horizontal)
        .border(.yellow)
    Text("Regular padding")
        .padding(.horizontal)
        .border(.green)
    Text("Text with no padding")
        .border(.blue)
    Button("Button") { }
}
.navigationTitle("Hello World")
```

The text with minimum scene padding uses the system minimum padding and the text with navigation bar scene padding automatically aligns with the navigation bar content. In contrast, the text that uses the default padding and the text without padding do not align with scene elements.

Scene padding in watchOS also ensures that your content avoids the curved edges of a device like Apple Watch Series 7. In other platforms, scene padding produces the same default padding that you get from the `View/padding(_:_:)` modifier.

> ❗ **Important**: Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even if you specify those edges as part of the input. For example, if you specify `Edge/Set/vertical` instead of `Edge/Set/horizontal` in the example above, the modifier would have no effect in watchOS. It does, however, apply to all the edges that you specify in other platforms.

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even if you specify those edges as part of the input. For example, if you specify `Edge/Set/vertical` instead of `Edge/Set/horizontal` in the example above, the modifier would have no effect in watchOS. It does, however, apply to all the edges that you specify in other platforms.

## Parameters

- `padding`: The kind of padding to add.
- `edges`: The set of edges along which to pad this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/scenepadding(_:edges:))*