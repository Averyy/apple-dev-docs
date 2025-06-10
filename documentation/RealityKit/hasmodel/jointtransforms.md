# jointTransforms

**Framework**: RealityKit  
**Kind**: property

The relative joint transforms of the model entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var jointTransforms: [Transform] { get set }
```

#### Discussion

Call `RealityKit/BodyTrackedEntity/jointNames` to determine the name and order of the joints.

> **Note**: Active animations may override the joint transforms set using this property.

## See Also

- [var jointNames: [String]](hasmodel/jointnames.md)
  The names of all the joints in the model entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasmodel/jointtransforms)*