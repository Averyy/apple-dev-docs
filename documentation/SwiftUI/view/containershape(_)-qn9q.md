# containerShape(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the container shape to use for any container relative shape within this view.

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
func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
```

**Other overloads**:

```swift
nonisolated
func containerShape(_ shape: some RoundedRectangularShape) -> some View
```

## Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any [`ContainerRelativeShape`](../containerrelativeshape.md) within the `content` matches the rounded rectangle shape from this container inset as appropriate.

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

> **See Also**: [`containerShape(_:)`](./containershape%28_%29-3br47.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/containershape(_:)-qn9q)*