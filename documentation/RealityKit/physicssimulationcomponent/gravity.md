# gravity

**Framework**: RealityKit  
**Kind**: property

The gravity for the simulation relative to the simulation entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var gravity: SIMD3<Float>
```

#### Discussion

The value stored in this property is the gravitational acceleration applied to dynamic physics body entities every frame along the negative world y-axis. The default value is `-9.81` meters per second squared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationcomponent/gravity)*