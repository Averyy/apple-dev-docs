# containerShape(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
nonisolated
func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
```

## Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any [`ContainerRelativeShape`](../containerrelativeshape.md) within the `content` matches the rounded rectangle shape from this container inset as appropriate. Any [`ConcentricRectangle`](../concentricrectangle.md) within the `content` will match the corners to be concentric to the container corners.

```swift
struct PlatterContainer<Content: View> : View {
    @ContentBuilder var content: Content
    var body: some View {
        content
            .padding()
            .containerShape(shape)
            .background(shape.fill(.background))
    }
    var shape: RoundedRectangle { RoundedRectangle(cornerRadius: 20) }
}
```

> **See Also**: [`containerShape(_:)`](./containershape%28_%29-qn9q.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/containershape(_:)-3br47)*