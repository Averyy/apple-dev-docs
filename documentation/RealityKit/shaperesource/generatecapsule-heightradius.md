# generateCapsule(height:radius:)

**Framework**: Realitykit  
**Kind**: method

Creates a capsule shape with the specified height and radius.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func generateCapsule(height: Float, radius: Float) -> ShapeResource
```

#### Return Value

The new capsule.

#### Discussion

> **Note**: Collision shape extents that fall below 2mm are forced to be 2mm in size - this includes, entities with negative scale values.

## Parameters

- `height`: The height of the capsule including the spherical caps in meters, measured along the local y-axis.
- `radius`: The radius of the capsule in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/generatecapsule(height:radius:))*