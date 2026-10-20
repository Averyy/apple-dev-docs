# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Synchronous variant of [`makeMaterialResource(descriptor:)`](./makematerialresource%28descriptor%29-2qjge.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource
```

**Other overloads**:

```swift
nonisolated
(nonsending) final func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makematerialresource(descriptor:)-2qjge)*