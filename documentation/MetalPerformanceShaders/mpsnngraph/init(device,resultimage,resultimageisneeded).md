# init(device:resultImage:resultImageIsNeeded:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(device: any MTLDevice, resultImage: MPSNNImageNode, resultImageIsNeeded resultIsNeeded: Bool)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device resultImage:(MPSNNImageNode *) resultImage resultImageIsNeeded:(BOOL) resultIsNeeded;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
- [convenience init?(device: any MTLDevice, resultImage: MPSNNImageNode)](./init%28device,resultimage%29.md)
- [init?(device: any MTLDevice, resultImages: [MPSNNImageNode], resultsAreNeeded: UnsafeMutablePointer<ObjCBool>?)](./init%28device,resultimages,resultsareneeded%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/init(device:resultimage:resultimageisneeded:))*