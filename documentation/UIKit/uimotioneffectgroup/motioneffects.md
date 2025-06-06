# motionEffects

**Framework**: UIKit  
**Kind**: property

An array of motion effect objects to apply as a group to the view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var motionEffects: [UIMotionEffect]? { get set }
```

#### Discussion

The array contains one or more [`UIMotionEffect`](uimotioneffect.md) objects. When the viewer offset changes, each object in the group is asked for its key paths and updated values. Those values are then applied simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimotioneffectgroup/motioneffects)*