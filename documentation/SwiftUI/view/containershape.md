# containerShape(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the container shape to use for any container relative shape or concentric rectangle within this view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func containerShape(_ shape: some RoundedRectangularShape) -> some View
```

#### Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any [`ContainerRelativeShape`](containerrelativeshape.md) within the `content` matches the rounded rectangle shape from this container inset as appropriate. Any [`ConcentricRectangle`](concentricrectangle.md) within the `content` will match the corners to be concentric to the container corners.

```swift
struct PlatterContainer<Content: View> : View {
    @ViewBuilder var content: Content
    var body: some View {
        content
            .padding()
            .containerShape(shape)
            .background(shape.fill(.background))
    }
    var shape: RoundedRectangle { RoundedRectangle(cornerRadius: 20) }
}
```

> **Note**: [`containerShape(_:)`](view/containershape(_:)-qn9q.md)

## See Also

- [protocol InsettableShape](insettableshape.md)
  A shape type that is able to inset itself to produce another shape.
- [struct ContainerRelativeShape](containerrelativeshape.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/containershape(_:))*