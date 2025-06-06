# convert(_:to:)

**Framework**: SwiftUI  
**Kind**: method

Converts a point’s coordinates to physical length measurements in the specified unit.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func convert(_ point: CGPoint, to unit: UnitLength) -> CGPoint
```

#### Return Value

A point value with physical length measurements, in the given unit

#### Discussion

The point is assumed to be in the coordinate system of the scene that this converter is associated with. If the scene is scaled, the physical measurement will take this scale into account.

## See Also

- [func convert(_:from:)](physicalmetricsconverter/convert(_:from:).md)
  Converts a length in the specified unit to a length in points suitable for use in the environment this converter is associated with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:to:))*