# bufferIndex

**Framework**: RealityKit  
**Kind**: property

The index of the buffer to use for this layout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var bufferIndex: Int { get set }
```

#### Discussion

Most usage scenarios use only one buffer. Use an index less than `LowLevelMeshResource.Descriptor.vertexBufferCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/layout/bufferindex)*