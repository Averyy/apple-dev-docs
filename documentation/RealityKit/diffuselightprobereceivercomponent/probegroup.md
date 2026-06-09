# probeGroup

**Framework**: RealityKit  
**Kind**: property

The entity providing diffuse probe lighting to this receiver.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var probeGroup: Entity
```

#### Discussion

The referenced entity must have a [`DiffuseLightProbeGroupComponent`](diffuselightprobegroupcomponent.md) attached and must exist within the scene hierarchy. The receiver’s diffuse lighting is interpolated from probes in this group based on the receiver entity’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/diffuselightprobereceivercomponent/probegroup)*