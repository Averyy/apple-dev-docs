# init(device:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes an L2-norm pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight strideInPixelsX:(NSUInteger) strideInPixelsX strideInPixelsY:(NSUInteger) strideInPixelsY;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
  Initializes an L2-norm pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingl2norm/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:))*