# init(device:kernelWidth:kernelHeight:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a pooling filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight;
```

#### Return Value

A valid [`MPSCNNPooling`](../mpscnnpooling.md) object or `nil`, if failure.

## Parameters

- `device`: The device the kernel will run on.
- `kernelWidth`: The width of the kernel.

  This value can be odd or even.
- `kernelHeight`: The height of the kernel.

  This value can be odd or even.

## See Also

### Instance Methods
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
  Initializes a pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./init%28device,kernelwidth,kernelheight,strideinpixelsx,strideinpixelsy%29.md)
  Initializes a pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling/init(device:kernelwidth:kernelheight:))*