# containerShape(_:)

**Framework**: PermissionKit  
**Kind**: method

Sets the container shape to use for any container relative shape within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 8.0+

## Declaration

```swift
nonisolated
func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
```

#### Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any `ContainerRelativeShape` within the `content` matches the rounded rectangle shape from this container inset as appropriate.

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/containershape(_:))*