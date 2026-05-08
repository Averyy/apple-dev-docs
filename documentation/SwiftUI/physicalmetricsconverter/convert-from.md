# convert(_:from:)

**Framework**: SwiftUI  
**Kind**: method

Converts a length in the specified unit to a length in points suitable for use in the environment this converter is associated with.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func convert(_ lengthValue: CGFloat, from unit: UnitLength) -> CGFloat
```

#### Return Value

A value in points. Use this value only in the scene this converter was associated with.

## See Also

- [func convert(_:to:)](physicalmetricsconverter/convert(_:to:).md)
  Converts a point’s coordinates to physical length measurements in the specified unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/physicalmetricsconverter/convert(_:from:))*