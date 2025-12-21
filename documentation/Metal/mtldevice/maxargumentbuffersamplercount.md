# maxArgumentBufferSamplerCount

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The maximum number of unique argument buffer samplers per app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var maxArgumentBufferSamplerCount: Int { get }
```

#### Discussion

This limit only applies to samplers that support argument buffers (see [`supportArgumentBuffers`](mtlsamplerdescriptor/supportargumentbuffers.md)). An [`MTLSamplerState`](mtlsamplerstate.md) instance is only unique if the properties of the [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) instance that created it are unique. For example, two samplers with equal [`minFilter`](mtlsamplerdescriptor/minfilter.md) values but different [`magFilter`](mtlsamplerdescriptor/magfilter.md) values are unique.

See [`Improving CPU performance by using argument buffers`](improving-cpu-performance-by-using-argument-buffers.md) for more information about argument buffer tiers, limits, and capabilities.

## See Also

- [var argumentBuffersSupport: MTLArgumentBuffersTier](mtldevice/argumentbufferssupport.md)
  Returns the GPU device’s support tier for argument buffers.
- [func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?](mtldevice/makeargumentencoder(arguments:).md)
  Creates a new argument encoder for an array of arguments.
- [func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder](mtldevice/makeargumentencoder(bufferbinding:).md)
  Creates a new argument encoder for a buffer binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maxargumentbuffersamplercount)*