# clipped(antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Clips this view to its bounding rectangular frame.

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
func clipped(antialiased: Bool = false) -> some View
```

## Mentions

- [Fitting images into available space](../fitting-images-into-available-space.md)

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

![Screenshot showing text clipped to its](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-clipped@2x.png)

## Parameters

- `antialiased`: A Boolean value that indicates whether the rendering system applies smoothing to the edges of the clipping rectangle.

## See Also

### Masking and clipping
- [func mask<Mask>(alignment: Alignment, () -> Mask) -> some View](./mask%28alignment,_%29.md)
  Masks this view using the alpha channel of the given view.
- [func clipShape<S>(S, style: FillStyle) -> some View](./clipshape%28_,style%29.md)
  Sets a clipping shape for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/clipped(antialiased:))*