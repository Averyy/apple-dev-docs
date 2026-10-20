# init(parentImage:sliceRange:featureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(parentImage parent: MPSImage, sliceRange: NSRange, featureChannels: Int)
```

```objc
- (instancetype) initWithParentImage:(MPSImage *) parent sliceRange:(NSRange) sliceRange featureChannels:(NSUInteger) featureChannels;
```

## See Also

### Initializers
- [convenience init(device: any MTLDevice, imageDescriptor: MPSImageDescriptor)](./init%28device,imagedescriptor%29.md)
  Initializes an empty image.
- [class MPSImageDescriptor](../mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](../mpsimage.md).
- [convenience init(texture: any MTLTexture, featureChannels: Int)](./init%28texture,featurechannels%29.md)
  Initializes an image from a texture. The user-allocated texture has been created for a specific number of feature channels and number of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/init(parentimage:slicerange:featurechannels:))*