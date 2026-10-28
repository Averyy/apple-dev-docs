# cornerRadius(_:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Clips this view to its bounding frame, with the specified corner radius.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`clipShape(_:style:)`](./clipshape%28_,style%29.md) or [`fill(style:)`](../shape/fill%28style%29.md) instead.

## Declaration

```swift
nonisolated
func cornerRadius(_ radius: CGFloat, antialiased: Bool = true) -> some View
```

## Return Value

A view that clips this view to its bounding frame with the specified corner radius.

## Discussion

By default, a view’s bounding frame only affects its layout, so any content that extends beyond the edges of the frame remains visible. Use `cornerRadius(_:antialiased:)` to hide any content that extends beyond these edges while applying a corner radius.

The following code applies a corner radius of 25 to a text view:

```swift
Text("Rounded Corners")
    .frame(width: 175, height: 75)
    .foregroundColor(Color.white)
    .background(Color.black)
    .cornerRadius(25)
```

![A screenshot of a rectangle with rounded corners bounding a text](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-cornerRadius@2x.png)

## Parameters

- `radius`: A CGFloat value that specifies the corner radius to use when clipping the view to its bounding frame.
- `antialiased`: A Boolean value that indicates whether the rendering system applies smoothing to the edges of the clipping rectangle.

## See Also

### Graphics and rendering modifiers
- [func accentColor(Color?) -> some View](./accentcolor%28_%29.md)
  Sets the accent color for this view and the views it contains.
- [func mask<Mask>(Mask) -> some View](./mask%28_%29.md)
  Masks this view using the alpha channel of the given view.
- [func animation(Animation?) -> some View](./animation%28_%29-1hc0p.md)
  Applies the given animation to all animatable values within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/cornerradius(_:antialiased:))*