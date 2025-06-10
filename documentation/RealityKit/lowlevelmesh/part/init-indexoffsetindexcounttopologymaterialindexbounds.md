# init(indexOffset:indexCount:topology:materialIndex:bounds:)

**Framework**: RealityKit  
**Kind**: init

Creates a low-level mesh part.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(indexOffset: Int = 0, indexCount: Int = 0, topology: MTLPrimitiveType = .triangle, materialIndex: Int = 0, bounds: BoundingBox)
```

## Parameters

- `indexOffset`: The offset, in bytes, of the first index.
- `indexCount`: The number of indices to use for this part.
- `topology`: The geometric primitive to use when rendering this part.
- `materialIndex`: The material index this part associates with.
- `bounds`: The model-space bounding box of the part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/part/init(indexoffset:indexcount:topology:materialindex:bounds:))*