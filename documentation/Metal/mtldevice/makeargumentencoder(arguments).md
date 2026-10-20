# makeArgumentEncoder(arguments:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLArgumentEncoder>) newArgumentEncoderWithArguments:(NSArray<MTLArgumentDescriptor *> *) arguments;
```

## Parameters

- `arguments`: An array of [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instances that you need to sort by their [`index`](../mtlargumentdescriptor/index.md) properties in monotonically increasing order.

## See Also

### Creating argument buffer encoders
- [var argumentBuffersSupport: MTLArgumentBuffersTier](./argumentbufferssupport.md)
  Returns the GPU device’s support tier for argument buffers.
- [var maxArgumentBufferSamplerCount: Int](./maxargumentbuffersamplercount.md)
  The maximum number of unique argument buffer samplers per app.
- [func makeArgumentEncoder(bufferBinding: any MTLBufferBinding) -> any MTLArgumentEncoder](./makeargumentencoder%28bufferbinding%29.md)
  Creates a new argument encoder for a buffer binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeargumentencoder(arguments:))*