# makeMeshResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Creates a mesh resource from the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource
```

#### Return Value

A newly created [`LowLevelMeshResource`](lowlevelmeshresource.md).

#### Discussion

> **Note**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The vertex and index buffer layout to allocate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makemeshresource(descriptor:))*