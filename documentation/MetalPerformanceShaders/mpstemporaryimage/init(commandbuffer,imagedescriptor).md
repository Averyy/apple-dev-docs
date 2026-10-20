# init(commandBuffer:imageDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a temporary image for use on a command buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)
```

```objc
+ (instancetype) temporaryImageWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer imageDescriptor:(const MPSImageDescriptor *) imageDescriptor;
```

#### Return Value

A valid [`MPSTemporaryImage`](../mpstemporaryimage.md) object.

#### Discussion

The temporary image will be released when the command buffer is committed. The underlying texture will become invalid before this time due to the action of the [`readCount`](./readcount.md) property.

## Parameters

- `commandBuffer`: The command buffer on which the temporary image will be exclusively used.
- `imageDescriptor`: An image descriptor that describes the image to create.

## See Also

### Initializers
- [class MPSImageDescriptor](../mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](../mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](./init%28commandbuffer,texturedescriptor%29.md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../../Metal/mtltexturedescriptor.md)
  An instance that you use to configure new Metal texture instances.
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)](./init%28commandbuffer,texturedescriptor,featurechannels%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/init(commandbuffer:imagedescriptor:))*