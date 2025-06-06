# clipped(antialiased:)

**Framework**: FamilyControls  
**Kind**: method

Clips this view to its bounding rectangular frame.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func clipped(antialiased: Bool = false) -> some View
```

#### Return Value

A view that clips this view to its bounding frame.

#### Discussion

Use the `clipped(antialiased:)` modifier to hide any content that extends beyond the layout bounds of the shape.

By default, a view’s bounding frame is used only for layout, so any content that extends beyond the edges of the frame is still visible.

```swift
Text("This long text string is clipped")
    .fixedSize()
    .frame(width: 175, height: 100)
    .clipped()
    .border(Color.gray)
```

## Parameters

- `antialiased`: A Boolean value that indicates whether the   rendering system applies smoothing to the edges of the clipping   rectangle.

## See Also

- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](familyactivitypicker/mask(alignment:_:).md)
  Masks this view using the alpha channel of the given view.
- [func clipShape<S>(S, style: FillStyle) -> some View](familyactivitypicker/clipshape(_:style:).md)
  Sets a clipping shape for this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](familyactivitypicker/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.
- [func containerShape<T>(T) -> some View](familyactivitypicker/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/clipped(antialiased:))*