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
func scaleEffect(_ scale: Size3D, anchor: UnitPoint3D = .center) -> some VisualEffect
```

**Other overloads**:

```swift
@export(implementation)
func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some VisualEffect
```

```swift
func scaleEffect(_ scale: CGFloat, anchor: UnitPoint = .center) -> some VisualEffect
```

```swift
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some VisualEffect
```

## Return Value

An effect that scales this view by `scale`.

## Discussion

The original dimensions of the view are considered to be unchanged by scaling the contents. To change the dimensions of the view, use a modifier like `frame()` instead.

## Parameters

- `scale`: The scale factor for this view in each dimension.
- `anchor`: The anchor point about which to scale the view. Defaults to center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(_:anchor:)-5dxyh)*