# offset(x:y:)

**Framework**: SwiftUI  
**Kind**: method

Offsets the view by the specified horizontal and vertical distances.

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
func offset(x: CGFloat = 0, y: CGFloat = 0) -> some VisualEffect
```

#### Return Value

An effect that offsets the view by `x` and `y`.

## Parameters

- `x`: The horizontal distance to offset the view.
- `y`: The vertical distance to offset the view.

## See Also

- [func offset(CGSize) -> some VisualEffect](visualeffect/offset(_:).md)
  Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [func offset(z: CGFloat) -> some VisualEffect](visualeffect/offset(z:).md)
  Brings a view forward in Z by the provided distance in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/offset(x:y:))*