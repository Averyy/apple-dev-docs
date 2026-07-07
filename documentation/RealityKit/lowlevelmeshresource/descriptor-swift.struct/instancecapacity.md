# instanceCapacity

**Framework**: RealityKit  
**Kind**: property

The maximum number of instances the mesh supports when using per-instance vertex data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var instanceCapacity: Int { get set }
```

#### Discussion

Set this to the maximum number of instances you intend to draw when any `Layout` in `vertexLayouts` uses a `stepFunction` of `.perInstance`. Defaults to `0`.

Corresponds to `MTLVertexDescriptor`’s per-instance buffer layout capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/descriptor-swift.struct/instancecapacity)*