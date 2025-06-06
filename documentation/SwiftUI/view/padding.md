# padding(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an equal padding amount to specific edges of this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func padding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
```

## Mentions

- [Laying out a simple view](laying-out-a-simple-view.md)

#### Return Value

A view that’s padded by the specified amount on the specified edges.

#### Discussion

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from [`Edge.Set`](edge/set.md), or by specifying an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that contains edge values:

```swift
VStack {
    Text("Text padded by 20 points on the bottom and trailing edges.")
        .padding([.bottom, .trailing], 20)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

![A screenshot of two text strings arranged vertically, each surrounded](https://docs-assets.developer.apple.com/published/de51d2c2d529d3dacc60fbe0a17edf2e/View-padding-2-iOS%402x.png)

You can omit either or both of the parameters. If you omit the `length`, SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI applies the padding to all edges. Omit both to add a default padding all the way around a view. SwiftUI chooses a default amount of padding that’s appropriate for the platform and the presentation context.

```swift
VStack {
    Text("Text with default padding.")
        .padding()
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The example above looks like this in iOS under typical conditions:

![A screenshot of two text strings arranged vertically, each surrounded](https://docs-assets.developer.apple.com/published/a8d65b9d38c14fa85c243db7f6ca50f1/View-padding-2a-iOS%402x.png)

To control the amount of padding independently for each edge, use [`padding(_:)`](view/padding(_:)-6pgqq.md). To pad all outside edges of a view by a specified amount, use [`padding(_:)`](view/padding(_:)-68shk.md).

## Parameters

- `edges`: The set of edges to pad for this view. The default   is  .
- `length`: An amount, given in points, to pad this view on the   specified edges. If you set the value to  , SwiftUI uses   a platform-specific default amount. The default value of this   parameter is  .

## See Also

- [func padding(_:)](view/padding(_:).md)
  Adds a different padding amount to each edge of this view.
- [func padding3D(_:)](view/padding3d(_:).md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](view/padding3d(_:_:).md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](view/scenepadding(_:).md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](view/scenepadding(_:edges:).md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](scenepadding.md)
  The padding used to space a view from its containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/padding(_:_:))*