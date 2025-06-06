# globalFkWeight

**Framework**: RealityKit  
**Kind**: property

The solver global forward kinematics demand’s weight.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var globalFkWeight: Float { get set }
```

#### Discussion

Multiplied with the per-joint per-axis forward kinematics weight [`fkWeightPerAxis`](ikcomponent/joint/fkweightperaxis.md).

The initial value is from the respective [`globalFkWeight`](ikrig/globalfkweight.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/solver/globalfkweight)*