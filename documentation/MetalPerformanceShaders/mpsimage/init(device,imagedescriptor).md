# init(device:imageDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes an empty image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice, imageDescriptor: MPSImageDescriptor)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device imageDescriptor:(const MPSImageDescriptor *) imageDescriptor;
```

#### Return Value

A valid [`MPSImage`](../mpsimage.md) object or `nil`, if failure.

#### Discussion

Storage for the image data is allocated lazily on the first use of the [`MPSImage`](../mpsimage.md) object, or when the [`texture`](./texture.md) property is first read.

## Parameters

- `device`: The device on which the image will be used.
- `imageDescriptor`: The image descriptor.

## See Also

### Initializers
- [class MPSImageDescriptor](../mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](../mpsimage.md).
- [convenience init(texture: any MTLTexture, featureChannels: Int)](./init%28texture,featurechannels%29.md)
  Initializes an image from a texture. The user-allocated texture has been created for a specific number of feature channels and number of images.
- [init(parentImage: MPSImage, sliceRange: NSRange, featureChannels: Int)](./init%28parentimage,slicerange,featurechannels%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/init(device:imagedescriptor:))*