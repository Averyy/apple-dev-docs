# forEach(descendantOf:inclusive:update:)

**Framework**: RealityKit  
**Kind**: method

Calls the provided closure on each element in the hierarchy rooted at the named joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
mutating func forEach(descendantOf rootJointName: String, inclusive: Bool = false, update: (inout IKRig.JointCollection.Element) -> Void)
```

#### Discussion

> **Note**: If the root joint is not found, the closure is not executed.

If the root joint is not found, the closure is not executed.

## Parameters

- `rootJointName`: The name of the root of the hierarchy.
- `inclusive`: Flag to include the root joint in the update list.
- `update`: Closure to update the joints in-place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection/foreach(descendantof:inclusive:update:))*