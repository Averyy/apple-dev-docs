# mask(_:)

**Framework**: SwiftUI  
**Kind**: method

Masks this view using the alpha channel of the given view.

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
func mask<Mask>(_ mask: Mask) -> some View where Mask : View
```

#### Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask(Rectangle().opacity(0.1))
```

![A screenshot of a view masked by a rectangle with 10% opacity.](https://docs-assets.developer.apple.com/published/eb80d49199cb4ce05352313feb4e29e5/SwiftUI-View-mask%402x.png)

## Parameters

- `mask`: The view whose alpha the rendering system applies to   the specified view.

## See Also

- [func accentColor(Color?) -> some View](view/accentcolor(_:).md)
  Sets the accent color for this view and the views it contains.
- [func animation(Animation?) -> some View](view/animation(_:)-1hc0p.md)
  Applies the given animation to all animatable values within this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](view/cornerradius(_:antialiased:).md)
  Clips this view to its bounding frame, with the specified corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mask(_:))*