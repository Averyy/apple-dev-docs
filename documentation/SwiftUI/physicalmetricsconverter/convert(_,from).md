# convert(_:from:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Converts a length in the specified unit to a length in points suitable for use in the environment this converter is associated with.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func convert(_ lengthValue: CGFloat, from unit: UnitLength) -> CGFloat
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func convert(_ point: CGPoint, from unit: UnitLength) -> CGPoint
```

```swift
@MainActor
@preconcurrency func convert(_ point: Point3D, from unit: UnitLength) -> Point3D
```

```swift
@MainActor
@preconcurrency func convert(_ rect: CGRect, from unit: UnitLength) -> CGRect
```

```swift
@MainActor
@preconcurrency func convert(_ rect: Rect3D, from unit: UnitLength) -> Rect3D
```

```swift
@MainActor
@preconcurrency func convert(_ size: CGSize, from unit: UnitLength) -> CGSize
```

```swift
@MainActor
@preconcurrency func convert(_ size: Size3D, from unit: UnitLength) -> Size3D
```

```swift
@MainActor
@preconcurrency func convert<V>(_ lengthValues: V, from unit: UnitLength) -> V where V : VectorArithmetic
```

#### Return Value

A value in points. Use this value only in the scene this converter was associated with.

## See Also

### Converting a unit length
- [func convert(_:to:)](./convert%28_,to%29.md)
  Converts a point’s coordinates to physical length measurements in the specified unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:from:))*