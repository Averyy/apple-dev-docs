# padding(_:)

**Framework**: RealityKit  
**Kind**: method

Adds a specific padding amount to each edge of this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func padding(_ length: CGFloat) -> some View
```

#### Return Value

A view that’s padded by the amount you specify.

#### Discussion

Use this modifier to add padding all the way around a view.

```None
VStack {
    Text("Text padded by 10 points on each edge.")
        .padding(10)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

To independently control the amount of padding for each edge, use `View/padding(_:)-6pgqq`. To pad a select set of edges by the same amount, use `View/padding(_:_:)`.

## Parameters

- `length`: The amount, given in points, to pad this view on all   edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/padding(_:)-1i1bf)*