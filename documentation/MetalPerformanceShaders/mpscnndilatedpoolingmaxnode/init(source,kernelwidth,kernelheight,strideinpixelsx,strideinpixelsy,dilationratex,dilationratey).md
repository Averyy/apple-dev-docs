# init(source:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:dilationRateX:dilationRateY:)

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
init(source sourceNode: MPSNNImageNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int, dilationRateX: Int, dilationRateY: Int)
```

```objc
- (instancetype) initWithSource:(MPSNNImageNode *) sourceNode kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight strideInPixelsX:(NSUInteger) strideInPixelsX strideInPixelsY:(NSUInteger) strideInPixelsY dilationRateX:(NSUInteger) dilationRateX dilationRateY:(NSUInteger) dilationRateY;
```

## See Also

### Initializers
- [init(source: MPSNNImageNode, filterSize: Int)](./init%28source,filtersize%29.md)
- [init(source: MPSNNImageNode, filterSize: Int, stride: Int, dilationRate: Int)](./init%28source,filtersize,stride,dilationrate%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmaxnode/init(source:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:dilationratex:dilationratey:))*