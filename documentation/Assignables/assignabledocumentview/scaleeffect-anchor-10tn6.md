# scaleEffect(_:anchor:)

**Framework**: Assignables  
**Kind**: method

Scales this view uniformly by the specified factor, relative to an anchor point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view that scales this view by `s` in all dimensions.

#### Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `s`: The scale factor for this view.
- `anchor`: The anchor point about which to scale the view. Defaults to center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/scaleeffect(_:anchor:)-10tn6)*