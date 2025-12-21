# meshPartIndex(modelID:partID:)

**Framework**: RealityKit  
**Kind**: method

Get the mesh part index for a given model and part identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func meshPartIndex(modelID: String, partID: String) -> Int?
```

#### Discussion

You can use this to resolve string names to part indices for use in [`MeshInstancesComponent`](meshinstancescomponent.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/meshpartindex(modelid:partid:))*