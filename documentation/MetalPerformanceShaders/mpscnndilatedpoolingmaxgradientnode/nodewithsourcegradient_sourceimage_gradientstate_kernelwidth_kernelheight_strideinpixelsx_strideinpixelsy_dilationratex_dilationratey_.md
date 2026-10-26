# nodeWithSourceGradient:sourceImage:gradientState:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:dilationRateX:dilationRateY:

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) nodeWithSourceGradient:(MPSNNImageNode *) sourceGradient sourceImage:(MPSNNImageNode *) sourceImage gradientState:(MPSNNGradientStateNode *) gradientState kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight strideInPixelsX:(NSUInteger) strideInPixelsX strideInPixelsY:(NSUInteger) strideInPixelsY dilationRateX:(NSUInteger) dilationRateX dilationRateY:(NSUInteger) dilationRateY;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmaxgradientnode/nodewithsourcegradient:sourceimage:gradientstate:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:dilationratex:dilationratey:)*