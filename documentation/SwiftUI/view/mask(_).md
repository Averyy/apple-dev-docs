# mask(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Masks this view using the alpha channel of the given view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`mask(alignment:_:)`](./mask%28alignment,_%29.md) instead.

## Declaration

```swift
nonisolated
func mask<Mask>(_ mask: Mask) -> some View where Mask : View
```

## Discussion

Use `mask(_:)` when you want to apply the alpha (opacity) value of another view to the current view.

This example shows an image masked by rectangle with a 10% opacity:

```swift
Image(systemName: "envelope.badge.fill")
    .foregroundColor(Color.blue)
    .font(.system(size: 128, weight: .regular))
    .mask(Rectangle().opacity(0.1))
```

![A screenshot of a view masked by a rectangle with 10% opacity.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-mask@2x.png)

## Parameters

- `mask`: The view whose alpha the rendering system applies to the specified view.

## See Also

### Graphics and rendering modifiers
- [func accentColor(Color?) -> some View](./accentcolor%28_%29.md)
  Sets the accent color for this view and the views it contains.
- [func animation(Animation?) -> some View](./animation%28_%29-1hc0p.md)
  Applies the given animation to all animatable values within this view.
- [func cornerRadius(CGFloat, antialiased: Bool) -> some View](./cornerradius%28_,antialiased%29.md)
  Clips this view to its bounding frame, with the specified corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/mask(_:))*