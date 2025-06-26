# meshPartIndex(modelID:partID:)

**Framework**: RealityKit  
**Kind**: method

Get the MeshPartIndex for a given model and part identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func meshPartIndex(modelID: String, partID: String) -> Int?
```

#### Discussion

This can be used to resolve string names to part indices for use in MeshInstancesComponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/meshpartindex(modelid:partid:))*