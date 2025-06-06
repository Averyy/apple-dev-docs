# makeArgumentEncoder(bufferBinding:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new argument encoder for a buffer binding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder
```

## Parameters

- `bufferBinding`: An   instance.

## See Also

- [var argumentBuffersSupport: MTLArgumentBuffersTier](mtldevice/argumentbufferssupport.md)
  Returns the GPU device’s support tier for argument buffers.
- [var maxArgumentBufferSamplerCount: Int](mtldevice/maxargumentbuffersamplercount.md)
  The maximum number of unique argument buffer samplers per app.
- [func makeArgumentEncoder(arguments: [MTLArgumentDescriptor]) -> (any MTLArgumentEncoder)?](mtldevice/makeargumentencoder(arguments:).md)
  Creates a new argument encoder for an array of arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeargumentencoder(bufferbinding:))*