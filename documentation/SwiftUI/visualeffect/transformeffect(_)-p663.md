# transformEffect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies a projection transformation to the view’s rendered output.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func transformEffect(_ transform: ProjectionTransform) -> some VisualEffect
```

**Other overloads**:

```swift
func transformEffect(_ transform: CGAffineTransform) -> some VisualEffect
```

## Return Value

An effect that applies a projection transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [`ProjectionTransform`](../projectiontransform.md).

## Parameters

- `transform`: A [`ProjectionTransform`](../projectiontransform.md) to apply to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/transformeffect(_:)-p663)*