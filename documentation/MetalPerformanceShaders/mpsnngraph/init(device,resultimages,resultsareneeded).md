# init(device:resultImages:resultsAreNeeded:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(device: any MTLDevice, resultImages: [MPSNNImageNode], resultsAreNeeded areResultsNeeded: UnsafeMutablePointer<ObjCBool>?)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device resultImages:(NSArray<MPSNNImageNode *> *) resultImages resultsAreNeeded:(BOOL *) areResultsNeeded;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
- [convenience init?(device: any MTLDevice, resultImage: MPSNNImageNode)](./init%28device,resultimage%29.md)
- [init?(device: any MTLDevice, resultImage: MPSNNImageNode, resultImageIsNeeded: Bool)](./init%28device,resultimage,resultimageisneeded%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngraph/init(device:resultimages:resultsareneeded:))*