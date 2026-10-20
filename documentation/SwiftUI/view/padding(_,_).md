# padding(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

- [Laying out a simple view](../laying-out-a-simple-view.md)

#### Return Value

A view that’s padded by the specified amount on the specified edges.

#### Discussion

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from [`Edge.Set`](../edge/set.md), or by specifying an [`OptionSet`](../../Swift/optionset.md) that contains edge values:

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

![A screenshot of two text strings arranged vertically, each surrounded](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-padding-2-iOS@2x.png)

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

![A screenshot of two text strings arranged vertically, each surrounded](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-padding-2a-iOS@2x.png)

To control the amount of padding independently for each edge, use [`padding(_:)`](./padding%28_%29-6pgqq.md). To pad all outside edges of a view by a specified amount, use [`padding(_:)`](./padding%28_%29-68shk.md).

## Parameters

- `edges`: The set of edges to pad for this view. The default is [`all`](../edge/set/all.md).
- `length`: An amount, given in points, to pad this view on the specified edges. If you set the value to `nil`, SwiftUI uses a platform-specific default amount. The default value of this parameter is `nil`.

## See Also

### Adding padding around a view
- [func padding(_:)](./padding%28_%29.md)
  Adds a different padding amount to each edge of this view.
- [func padding3D(_:)](./padding3d%28_%29.md)
  Pads this view using the edge insets you specify.
- [func padding3D(Edge3D.Set, CGFloat?) -> some View](./padding3d%28_,_%29.md)
  Pads this view using the edge insets you specify.
- [func scenePadding(Edge.Set) -> some View](./scenepadding%28_%29.md)
  Adds padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [func scenePadding(ScenePadding, edges: Edge.Set) -> some View](./scenepadding%28_,edges%29.md)
  Adds a specified kind of padding to the specified edges of this view using an amount that’s appropriate for the current scene.
- [struct ScenePadding](../scenepadding.md)
  The padding used to space a view from its containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/padding(_:_:))*