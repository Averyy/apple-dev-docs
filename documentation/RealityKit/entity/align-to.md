# align(_:to:)

**Framework**: RealityKit  
**Kind**: method

Moves and rotates the entity by a transformation from the origin pin to the target pin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func align(_ originPin: GeometricPin, to targetPin: GeometricPin) -> float4x4?
```

#### Return Value

Transformation matrix that has been applied to the `Entity`, in the frame or reference of the parent of the `Entity`. If either pin doesn’t exist, returns `nil`.

## Parameters

- `originPin`: The   to align. It should be one of the pins on the entity.
- `targetPin`: The   to align to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/align(_:to:))*