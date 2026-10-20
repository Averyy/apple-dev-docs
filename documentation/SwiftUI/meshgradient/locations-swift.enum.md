# MeshGradient.Locations

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [case bezierPoints([MeshGradient.BezierPoint])](./locations-swift.enum/bezierpoints%28_%29.md)
  Vertices explicitly specifying their location and control points.
- [MeshGradient.Locations.points(_:)](./locations-swift.enum/points%28_%29.md)
  Vertices are only specified as their location, their control points are inferred from the locations of their neighbors.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient/locations-swift.enum)*