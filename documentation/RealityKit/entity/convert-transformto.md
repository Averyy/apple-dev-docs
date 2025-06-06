# convert(transform:to:)

**Framework**: RealityKit  
**Kind**: method

Converts the scale, rotation, and position of a transform from the local space of the entity on which you called this method to the local space of a reference entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func convert(transform: Transform, to referenceEntity: Entity?) -> Transform
```

#### Return Value

The transform specified relative to `referenceEntity`.

## Parameters

- `transform`: The transform given in the local space of the entity.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/convert(transform:to:))*