# generateSphere(radius:)

**Framework**: Realitykit  
**Kind**: method

Creates a sphere shape with the specified radius.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generateSphere(radius: Float) -> ShapeResource
```

#### Return Value

The new sphere centered at the local origin.

#### Discussion

> **Note**: Collision shape extents that fall below 2mm are forced to be 2mm in size - this includes, entities with negative scale values.

## Parameters

- `radius`: The radius of the sphere in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generatesphere(radius:))*