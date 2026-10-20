# init(coder:device:)

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
init?(coder aDecoder: NSCoder, device: any MTLDevice)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder device:(id<MTLDevice>) device;
```

## See Also

### Initializers
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./init%28device,kernelwidth,kernelheight,strideinpixelsx,strideinpixelsy%29.md)
  Initializes an L2-norm pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingl2norm/init(coder:device:))*