# ComputeNodeGraph.Assembly.Location

**Framework**: ComputeGraph  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
enum Location
```

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Assembly.Location.buffer(index:sizeOffset:)](computenodegraph/assembly/location/buffer(index:sizeoffset:).md)
  Buffer that’s bound separately from other data. Size of buffer is stored at sizeOffset in uniforms
- [ComputeNodeGraph.Assembly.Location.constant(value:)](computenodegraph/assembly/location/constant(value:).md)
  Value is a fixed 64-bit constant
- [ComputeNodeGraph.Assembly.Location.constantBuffer(index:offset:)](computenodegraph/assembly/location/constantbuffer(index:offset:).md)
  Value is in the constantBuffers table at the specified index and offset
- [ComputeNodeGraph.Assembly.Location.context](computenodegraph/assembly/location/context.md)
  Value is a context type
- [ComputeNodeGraph.Assembly.Location.deviceBuffer(index:offset:)](computenodegraph/assembly/location/devicebuffer(index:offset:).md)
  Value is in the deviceBuffers table at the specified index and offset
- [ComputeNodeGraph.Assembly.Location.port(node:index:)](computenodegraph/assembly/location/port(node:index:).md)
  Value is the output of another node
- [ComputeNodeGraph.Assembly.Location.state(index:offset:length:)](computenodegraph/assembly/location/state(index:offset:length:).md)
  A context-dependent state value.
- [ComputeNodeGraph.Assembly.Location.texture(index:)](computenodegraph/assembly/location/texture(index:).md)
  Value is a texture with the given index
- [ComputeNodeGraph.Assembly.Location.unbound](computenodegraph/assembly/location/unbound.md)
  Attribute which is a default value and should be considered “not bound”
- [ComputeNodeGraph.Assembly.Location.uniform(offset:length:)](computenodegraph/assembly/location/uniform(offset:length:).md)
  Value is located in uniforms. Its value is located at `offset` in the uniforms with length `length`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/location)*