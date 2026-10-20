# init(device:kernelWidth:kernelHeight:dilationRateX:dilationRateY:strideInPixelsX:strideInPixelsY:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a dilated max pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, dilationRateX: Int, dilationRateY: Int, strideInPixelsX: Int, strideInPixelsY: Int)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight dilationRateX:(NSUInteger) dilationRateX dilationRateY:(NSUInteger) dilationRateY strideInPixelsX:(NSUInteger) strideInPixelsX strideInPixelsY:(NSUInteger) strideInPixelsY;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
  Initializes a dilated max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmax/init(device:kernelwidth:kernelheight:dilationratex:dilationratey:strideinpixelsx:strideinpixelsy:))*