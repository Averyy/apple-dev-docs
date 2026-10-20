# init(commandBuffer:textureDescriptor:featureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor, featureChannels: Int)
```

```objc
+ (instancetype) temporaryImageWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer textureDescriptor:(const MTLTextureDescriptor *) textureDescriptor featureChannels:(NSUInteger) featureChannels;
```

## See Also

### Initializers
- [convenience init(commandBuffer: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](./init%28commandbuffer,imagedescriptor%29.md)
  Initializes a temporary image for use on a command buffer.
- [class MPSImageDescriptor](../mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](../mpsimage.md).
- [convenience init(commandBuffer: any MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](./init%28commandbuffer,texturedescriptor%29.md)
  Low-level interface for creating a temporary image using a texture descriptor.
- [class MTLTextureDescriptor](../../Metal/mtltexturedescriptor.md)
  An instance that you use to configure new Metal texture instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/init(commandbuffer:texturedescriptor:featurechannels:))*