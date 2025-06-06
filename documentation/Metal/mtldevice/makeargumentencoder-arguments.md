# makeArgumentEncoder(arguments:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new argument encoder for an array of arguments.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?
```

## Parameters

- `arguments`: An array of   instances that you must sort by their   properties in monotonically increasing order.

## See Also

- [var argumentBuffersSupport: MTLArgumentBuffersTier](mtldevice/argumentbufferssupport.md)
  Returns the GPU device’s support tier for argument buffers.
- [var maxArgumentBufferSamplerCount: Int](mtldevice/maxargumentbuffersamplercount.md)
  The maximum number of unique argument buffer samplers per app.
- [func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder](mtldevice/makeargumentencoder(bufferbinding:).md)
  Creates a new argument encoder for a buffer binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeargumentencoder(arguments:))*