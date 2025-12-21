# setForce(_:index:)

**Framework**: RealityKit  
**Kind**: method

Sets the force for each rigid body.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
func setForce(_ force: SIMD3<Float>, index: Int)
```

#### Discussion

Inside the force effect update function, you are responsible to compute and output the force by calling this function for each rigid body. If you omit this function for a rigid body, that rigid body gets zero force from the effect.

## Parameters

- `force`: The force value.
- `index`: The index to the rigid body. The index should be in the range [0,  ].


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectparameters/setforce(_:index:))*