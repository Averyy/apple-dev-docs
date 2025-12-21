# transform

**Framework**: RealityKit  
**Kind**: property

The custom projection RealityKit applies to objects in the scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var transform: float4x4
```

#### Discussion

The value defaults to `4x4` zero matrix. Swap the near and far values to use a reverse depth matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/projectivetransformcameracomponent/transform)*