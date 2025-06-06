# MeshGradient.Locations

**Framework**: SwiftUI  
**Kind**: enum

An array of 2D locations and their control points.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Locations
```

## Topics

### Enumeration Cases
- [case bezierPoints([MeshGradient.BezierPoint])](meshgradient/locations-swift.enum/bezierpoints(_:).md)
  Vertices explicitly specifying their location and control points.
- [MeshGradient.Locations.points(_:)](meshgradient/locations-swift.enum/points(_:).md)
  Vertices are only specified as their location, their control points are inferred from the locations of their neighbors.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient/locations-swift.enum)*