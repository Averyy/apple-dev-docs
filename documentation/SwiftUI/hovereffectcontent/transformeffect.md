# transformEffect(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies an affine transformation to the view’s rendered output.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func transformEffect(_ transform: CGAffineTransform) -> some HoverEffectContent
```

#### Return Value

An effect that applies an affine transformation to the view’s rendered output.

#### Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform).

## Parameters

- `transform`: A    to   apply to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/transformeffect(_:))*