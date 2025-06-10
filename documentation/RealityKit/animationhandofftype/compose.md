# compose

**Framework**: RealityKit  
**Kind**: property

Adds the new animation to existing animations, and immediately starts the new animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
static var compose: AnimationHandoffType { get }
```

#### Discussion

Use this handoff for additive animations. If the new animation isn’t additive, then `compose` adds the new animation and removes the existing animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationhandofftype/compose)*