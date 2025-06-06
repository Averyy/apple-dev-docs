# transform3DEffect(_:)

**Framework**: Assignables  
**Kind**: method

Applies a 3D transformation to the receiver.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func transform3DEffect(_ transform: AffineTransform3D) -> some View
```

#### Return Value

A view that renders transformed according to the provided `transform`

## Parameters

- `transform`: The 3D transformation to apply to the view,   interpreting it as a 3D plane in space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/transform3deffect(_:))*