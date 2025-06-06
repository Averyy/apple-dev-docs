# scaleEffect(x:y:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

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
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some VisualEffect
```

#### Return Value

An effect that scales the view’s rendered output.

## Parameters

- `x`: An amount that represents the horizontal amount to scale the   view. The default value is  .
- `y`: An amount that represents the vertical amount to scale the view.   The default value is  .
- `anchor`: The point with a default of   that   defines the location within the view from which to apply the   transformation.

## See Also

- [func scaleEffect(_:anchor:)](visualeffect/scaleeffect(_:anchor:).md)
  Scales this view uniformly by the specified factor.
- [func scaleEffect(x: CGFloat, y: CGFloat, z: CGFloat, anchor: UnitPoint3D) -> some VisualEffect](visualeffect/scaleeffect(x:y:z:anchor:).md)
  Scales this view by the specified horizontal, vertical, and depth factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(x:y:anchor:))*