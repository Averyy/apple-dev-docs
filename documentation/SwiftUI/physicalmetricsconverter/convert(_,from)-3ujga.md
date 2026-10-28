# convert(_:from:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Converts a size, given in the specified unit, to a size in points suitable for use in the environment this converter is associated with.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func convert(_ size: Size3D, from unit: UnitLength) -> Size3D
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func convert(_ lengthValue: CGFloat, from unit: UnitLength) -> CGFloat
```

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
@preconcurrency func convert<V>(_ lengthValues: V, from unit: UnitLength) -> V where V : VectorArithmetic
```

## Return Value

A value in points. Use this value only in the scene this converter was associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:from:)-3ujga)*