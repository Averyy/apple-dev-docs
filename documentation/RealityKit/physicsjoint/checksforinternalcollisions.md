# checksForInternalCollisions

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property  
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

## Discussion

> **Note**: This does not affect how collisions of the two entities referenced in [`pin0`](./pin0.md) and [`pin1`](./pin1.md) interact with other entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoint/checksforinternalcollisions)*