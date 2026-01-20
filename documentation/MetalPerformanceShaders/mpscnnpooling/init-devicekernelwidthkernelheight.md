# init(device:kernelWidth:kernelHeight:)

**Framework**: Metal Performance Shaders  
**Kind**: init

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

#### Return Value

A valid [`MPSCNNPooling`](mpscnnpooling.md) object or `nil`, if failure.

## Parameters

- `device`: The device the kernel will run on.
- `kernelWidth`: This value can be odd or even.
- `kernelHeight`: This value can be odd or even.

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpooling/init(coder:device:).md)
  Initializes a pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpooling/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
  Initializes a pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling/init(device:kernelwidth:kernelheight:))*