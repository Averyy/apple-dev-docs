# replace(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replace the contents of this mesh resource asynchronously.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func replace(with content: MeshResource.Contents) async throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func replace(with content: MeshResource.Contents) throws
```

## Discussion

> **Note**: The contents of the modified mesh resource will not be synced between network clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/replace(with:)-24xfg)*