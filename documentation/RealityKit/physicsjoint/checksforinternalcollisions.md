# checksForInternalCollisions

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var checksForInternalCollisions: Bool { get }
```

#### Discussion

> **Note**: This does not affect how collisions of the two entities referenced in [`pin0`](physicsjoint/pin0.md) and [`pin1`](physicsjoint/pin1.md) interact with other entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoint/checksforinternalcollisions)*