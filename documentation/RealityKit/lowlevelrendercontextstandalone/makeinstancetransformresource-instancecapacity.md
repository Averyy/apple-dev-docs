# makeInstanceTransformResource(instanceCapacity:)

**Framework**: RealityKit  
**Kind**: method

Creates a transform buffer resource for GPU instancing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource
```

#### Return Value

A newly created [`LowLevelInstanceTransformResource`](lowlevelinstancetransformresource.md).

#### Discussion

The buffer stores up to `instanceCapacity` model-to-local transforms as `float4x4` values. Assign the result to a [`LowLevelMeshInstance`](lowlevelmeshinstance.md) via [`setInstanceTransforms(_:)`](lowlevelmeshinstance/setinstancetransforms(_:).md) to enable GPU instancing.

> **Note**: An error if the allocation fails.

## Parameters

- `instanceCapacity`: The maximum number of instances the buffer holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makeinstancetransformresource(instancecapacity:))*