# scaleEffect(x:y:anchor:)

**Framework**: SwiftUI  
**Kind**: method

Scales the view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some HoverEffectContent
```

#### Return Value

An effect that scales the view’s rendered output.

## Parameters

- `x`: An amount that represents the horizontal amount to scale the   view. The default value is  .
- `y`: An amount that represents the vertical amount to scale the view.   The default value is  .
- `anchor`: The point with a default of   that   defines the location within the view from which to apply the   transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/scaleeffect(x:y:anchor:))*