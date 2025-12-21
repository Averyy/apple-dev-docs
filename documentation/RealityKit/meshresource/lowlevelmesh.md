# lowLevelMesh

**Framework**: RealityKit  
**Kind**: property

The low-level mesh that this mesh is built from, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var lowLevelMesh: LowLevelMesh? { get }
```

#### Discussion

If this mesh is not built from a [`LowLevelMesh`](lowlevelmesh.md), it returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/lowlevelmesh)*