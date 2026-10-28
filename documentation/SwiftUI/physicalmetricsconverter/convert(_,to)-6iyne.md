# convert(_:to:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Converts a vector of values in points to corresponding physical length measurements in the specified unit.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func convert<V>(_ pointValues: V, to unit: UnitLength) -> V where V : VectorArithmetic
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func convert(_ point: CGPoint, to unit: UnitLength) -> CGPoint
```

```swift
@MainActor
@preconcurrency func convert(_ point: Point3D, to unit: UnitLength) -> Point3D
```

```swift
@MainActor
@preconcurrency func convert(_ pointsValue: CGFloat, to unit: UnitLength) -> CGFloat
```

```swift
@MainActor
@preconcurrency func convert(_ rect: CGRect, to unit: UnitLength) -> CGRect
```

```swift
@MainActor
@preconcurrency func convert(_ rect: Rect3D, to unit: UnitLength) -> Rect3D
```

```swift
@MainActor
@preconcurrency func convert(_ size: CGSize, to unit: UnitLength) -> CGSize
```

```swift
@MainActor
@preconcurrency func convert(_ size: Size3D, to unit: UnitLength) -> Size3D
```

## Return Value

A vector of physical length measurements, each converted from the points value in the input vector at the same position. converter was associated with.

## Discussion

The point values are assumed to be in the coordinate system of the scene that this converter is associated with. If the scene was scaled by user action, the physical measurement will take this scale into account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:to:)-6iyne)*