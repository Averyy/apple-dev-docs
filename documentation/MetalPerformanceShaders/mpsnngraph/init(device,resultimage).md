# init(device:resultImage:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+ - Deprecated in 11.3
- iPadOS 11.0+ - Deprecated in 11.3
- Mac Catalyst 11.0+ - Deprecated in 11.3
- macOS 10.13+ - Deprecated in 10.13.4
- tvOS 11.0+ - Deprecated in 11.3
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
convenience init?(device: any MTLDevice, resultImage: MPSNNImageNode)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device resultImage:(MPSNNImageNode *) resultImage;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
- [init?(device: any MTLDevice, resultImage: MPSNNImageNode, resultImageIsNeeded: Bool)](./init%28device,resultimage,resultimageisneeded%29.md)
- [init?(device: any MTLDevice, resultImages: [MPSNNImageNode], resultsAreNeeded: UnsafeMutablePointer<ObjCBool>?)](./init%28device,resultimages,resultsareneeded%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/init(device:resultimage:))*