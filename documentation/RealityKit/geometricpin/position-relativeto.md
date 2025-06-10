# position(relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Calculates and returns the current position of the pin relative to a reference entity, adjusted by the optional offset position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
func position(relativeTo referenceEntity: Entity?) -> SIMD3<Float>?
```

## Parameters

- `referenceEntity`: Reference   which defines the frame of reference for the returned position.   Can be  , which is equivalent to “world space”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/geometricpin/position(relativeto:))*