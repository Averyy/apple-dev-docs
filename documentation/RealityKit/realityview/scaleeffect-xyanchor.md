# scaleEffect(x:y:anchor:)

**Framework**: RealityKit  
**Kind**: method

Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, anchor: UnitPoint = .center) -> some View
```

#### Discussion

Use `scaleEffect(x:y:anchor:)` to apply a scaling transform to a view by a specific horizontal and vertical amount.

```None
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(x: 0.5, y: 0.5, anchor: .bottomTrailing)
    .border(Color.gray)
```

## Parameters

- `x`: An amount that represents the horizontal amount to scale the   view. The default value is  .
- `y`: An amount that represents the vertical amount to scale the view.   The default value is  .
- `anchor`: The anchor point that indicates the starting position for   the scale operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/scaleeffect(x:y:anchor:))*