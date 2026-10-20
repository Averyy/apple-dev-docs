# encode(commandBuffer:sourceImage:destinationMatrix:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationMatrix: MPSMatrix)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImage:(MPSImage *) sourceImage destinationMatrix:(MPSMatrix *) destinationMatrix;
```

## See Also

### Instance Methods
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationMatrix: MPSMatrix)](./encodebatch%28commandbuffer,sourceimages,destinationmatrix%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecopytomatrix/encode(commandbuffer:sourceimage:destinationmatrix:))*