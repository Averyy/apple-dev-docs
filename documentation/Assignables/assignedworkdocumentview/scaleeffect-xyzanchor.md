# scaleEffect(x:y:z:anchor:)

**Framework**: Assignables  
**Kind**: method

Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func scaleEffect(x: CGFloat = 1.0, y: CGFloat = 1.0, z: CGFloat = 1.0, anchor: UnitPoint3D = .center) -> some View
```

#### Return Value

A view that scales this view by `x`,`y`, and `z`.

#### Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `x`: The horizontal scale factor for this view.
- `y`: The vertical scale factor for this view.
- `z`: The depth scale factor for this view.
- `anchor`: The anchor point about which to scale the view. Defaults to center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/scaleeffect(x:y:z:anchor:))*