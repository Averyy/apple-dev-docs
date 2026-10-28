# init(wrappedValue:from:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a value that maps the specified rectangle, whose dimensions are specified in physical length measurements in the given unit, to the corresponding value in points in the associated scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(wrappedValue rect: CGRect, from unit: UnitLength) where Value == CGRect
```

**Other overloads**:

```swift
init(wrappedValue point: CGPoint, from unit: UnitLength) where Value == CGPoint
```

```swift
init(wrappedValue point: Point3D, from unit: UnitLength) where Value == Point3D
```

```swift
init(wrappedValue rect: Rect3D, from unit: UnitLength) where Value == Rect3D
```

```swift
init(wrappedValue size: CGSize, from unit: UnitLength) where Value == CGSize
```

```swift
init(wrappedValue size: Size3D, from unit: UnitLength) where Value == Size3D
```

```swift
init(wrappedValue value: Value, from unit: UnitLength) where Value : VectorArithmetic
```

```swift
init(wrappedValue value: Value, from unit: UnitLength) where Value == CGFloat
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetric/init(wrappedvalue:from:)-acph)*