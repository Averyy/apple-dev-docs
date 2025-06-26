# containerShape(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the container shape to use for any container relative shape within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func containerShape<T>(_ shape: T) -> some View where T : InsettableShape
```

#### Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any `ContainerRelativeShape` within the `content` matches the rounded rectangle shape from this container inset as appropriate.

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

## See Also

- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](familyactivitypicker/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func clipped(antialiased: Bool) -> some View](familyactivitypicker/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](familyactivitypicker/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](familyactivitypicker/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/containershape(_:))*