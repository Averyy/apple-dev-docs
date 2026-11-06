# contentMargins(for:edges:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The insets of a content margin guide for the given edges.

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
func contentMargins(for guide: ContentMarginGuide, edges: Edge.Set = .all) -> EdgeInsets
```

## Return Value

The insets `guide` provides for `edges`. Edges not in the set have a value of zero.

## Discussion

Read a guide when you need its value rather than the inset, like a view that draws its own content:

```swift
GeometryReader { proxy in
    Canvas { context, size in
        drawChart(
            in: context, size: size,
            insets: proxy.contentMargins(for: .container, edges: .horizontal))
    }
}
```

## Parameters

- `guide`: The guide that provides the insets.
- `edges`: The edges to read insets for.

## See Also

### Accessing geometry characteristics
- [func bounds(of: NamedCoordinateSpace) -> CGRect?](./bounds%28of%29.md)
  Returns the given coordinate space’s bounds rectangle, converted to the local coordinate space.
- [var concentricCornerRadii: RectangleCornerRadii?](./concentriccornerradii.md)
  The concentric corner radii for this view’s bounds relative to the container shape.
- [func concentricCornerRadii(in: CGRect) -> RectangleCornerRadii?](./concentriccornerradii%28in%29.md)
  Returns the concentric corner radii for the specified frame relative to the container shape.
- [var containerCornerInsets: RectangleCornerInsets](./containercornerinsets.md)
  Returns the corner insets of the container view. Use this value to adjust the geometry of a view based on the overlapping corner insets of the container view. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations.
- [var size: CGSize](./size.md)
  The size of the container view.
- [var safeAreaInsets: EdgeInsets](./safeareainsets.md)
  The safe area inset of the container view.
- [subscript<T>(Anchor<T>) -> T](./subscript%28_%29.md)
  Resolves the value of an anchor to the container view.
- [func transform(in: some CoordinateSpaceProtocol) -> AffineTransform3D?](./transform%28in%29.md)
  The container view’s 3D transform converted to a defined coordinate space.
- [func frame(in:)](./frame%28in%29.md)
  Returns the container view’s bounds rectangle, converted to a defined coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/geometryproxy/contentmargins(for:edges:))*