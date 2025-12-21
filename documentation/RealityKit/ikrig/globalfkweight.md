# globalFkWeight

**Framework**: RealityKit  
**Kind**: property

The solver global weight for the forward kinematics demands.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var globalFkWeight: Float
```

#### Discussion

This weight is a multiplier for each joint’s [`fkWeightPerAxis`](ikrig/joint/fkweightperaxis.md).

The recommended value range is the closed range `[0, 1]`, where `0` means no FK demands influence, and `1` is no rig level modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/globalfkweight)*