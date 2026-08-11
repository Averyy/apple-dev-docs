# makeMaterialResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource
```

#### Return Value

A newly compiled [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

#### Discussion

> **Note**: An error if shader compilation fails.

## Parameters

- `descriptor`: The geometry modifier, surface shader, and lighting function to compile into a material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makematerialresource(descriptor:)-8pruc)*