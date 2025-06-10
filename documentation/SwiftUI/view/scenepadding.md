# scenePadding(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func scenePadding(_ edges: Edge.Set = .all) -> some View
```

#### Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

#### Discussion

Use this modifier to add a scene-appropriate amount of padding to a view. Specify either a single edge value from [`Edge.Set`](edge/set.md), or an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root view of a window. In watchOS, use scene padding to align elements of your user interface with top level elements, like the title of a navigation view. For example, compare the effects of different kinds of padding on text views presented inside a [`NavigationView`](navigationview.md) in watchOS:

```swift
VStack(alignment: .leading, spacing: 10) {
    Text("Scene padding")
        .scenePadding(.horizontal)
        .border(.red) // Border added for reference.
    Text("Regular padding")
        .padding(.horizontal)
        .border(.green)
    Text("Text with no padding")
        .border(.blue)
    Button("Button") { }
}
.navigationTitle("Hello World")
```

The text with scene padding automatically aligns with the title, unlike the text that uses the default padding or the text without padding:

![A watchOS screenshot with the title Hello World and a back button](https://docs-assets.developer.apple.com/published/e40f288e48faa506338094961752349f/View-scenePadding-1-watchOS%402x.png)

Scene padding in watchOS also ensures that your content avoids the curved edges of a device like Apple Watch Series 7. In other platforms, scene padding produces the same default padding that you get from the [`padding(_:_:)`](view/padding(_:_:).md) modifier.

> ❗ **Important**: Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even if you specify those edges as part of the input. For example, if you specify [`vertical`](edge/set/vertical.md) instead of [`horizontal`](edge/set/horizontal.md) in the example above, the modifier would have no effect in watchOS. It does, however, apply to all the edges that you specify in other platforms.

## Parameters

- `edges`: The set of edges along which to pad this view.

## See Also

- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding(Edge.Set, CGFloat?) -> some View](view/padding(_:_:).md)
  Adds an equal padding amount to specific edges of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](view/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](scenepadding.md)
  The padding used to space a view from its containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scenepadding(_:))*