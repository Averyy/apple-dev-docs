# inner(color:radius:x:y:)

**Framework**: SwiftUI  
**Kind**: method

Creates a custom inner shadow style.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func inner(color: Color = .init(.sRGBLinear, white: 0, opacity: 0.55), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> ShadowStyle
```

#### Return Value

A new shadow style.

#### Discussion

Inner shadows draw on top of the source content by blurring, tinting, inverting and offsetting its per-pixel alpha values.

## Parameters

- `color`: The shadow’s color.
- `radius`: The shadow’s size.
- `x`: A horizontal offset you use to position the shadow   relative to this view.
- `y`: A vertical offset you use to position the shadow   relative to this view.

## See Also

- [static func drop(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> ShadowStyle](shadowstyle/drop(color:radius:x:y:).md)
  Creates a custom drop shadow style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shadowstyle/inner(color:radius:x:y:))*