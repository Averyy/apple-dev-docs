# globalLimitsWeight

**Framework**: RealityKit  
**Kind**: property

The solver global weight for the joint rotation limits.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var globalLimitsWeight: Float
```

#### Discussion

This weight is a multiplier for each joint’s [`weight`](ikrig/joint/limitsdefinition/weight.md).

The recommended value range is the closed range `[0, 1]`, where `0` means no limits influence, and `1` is no rig level modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/globallimitsweight)*