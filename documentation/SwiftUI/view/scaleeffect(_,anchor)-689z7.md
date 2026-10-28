# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales this view uniformly by the specified size in each dimension, relative to an anchor point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func scaleEffect(_ scale: Size3D, anchor: UnitPoint3D = .center) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some View
```

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> ModifiedContent<Self, _UniformScaleEffect>
```

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> some View
```

```swift
nonisolated
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some View
```

## Return Value

A view that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `scale`: The scale factor for this view in each dimension.
- `anchor`: The anchor point about which to scale the view. Defaults to center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaleeffect(_:anchor:)-689z7)*