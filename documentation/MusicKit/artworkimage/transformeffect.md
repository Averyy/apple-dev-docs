# transformEffect(_:)

**Framework**: MusicKit  
**Kind**: method

Applies an affine transformation to this view’s rendered output.

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
func transformEffect(_ transform: CGAffineTransform) -> some View
```

#### Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform).

In the example below, the text is rotated at -30˚ on the `y` axis.

```swift
let transform = CGAffineTransform(rotationAngle: -30 * (.pi / 180))

Text("Projection effect using transforms")
    .transformEffect(transform)
    .border(Color.gray)
```

## Parameters

- `transform`: A    to   apply to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/transformeffect(_:))*