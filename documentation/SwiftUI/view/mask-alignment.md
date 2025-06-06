# mask(alignment:_:)

**Framework**: SwiftUI  
**Kind**: method

Masks this view using the alpha channel of the given view.

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
func mask<Mask>(alignment: Alignment = .center, @ViewBuilder _ mask: () -> Mask) -> some View where Mask : View
```

#### Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask {
        Rectangle().opacity(0.1)
    }
```

![A screenshot of a view masked by a rectangle with 10%](https://docs-assets.developer.apple.com/published/eb80d49199cb4ce05352313feb4e29e5/SwiftUI-View-mask%402x.png)

## Parameters

- `alignment`: The alignment for   in relation to this view.
- `mask`: The view whose alpha the rendering system applies to   the specified view.

## See Also

- [func clipped(antialiased: Bool) -> some View](view/clipped(antialiased:).md)
  Clips this view to its bounding rectangular frame.
- [func clipShape<S>(S, style: FillStyle) -> some View](view/clipshape(_:style:).md)
  Sets a clipping shape for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mask(alignment:_:))*