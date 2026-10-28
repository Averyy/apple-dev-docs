# init(device:kernelWidth:kernelHeight:weights:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a convolution filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights kernelWeights: UnsafePointer<Float>)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight weights:(const float *) kernelWeights;
```

## Return Value

An initialized convolution filter object.

## Parameters

- `device`: The Metal device the filter will run on.
- `kernelWidth`: The width of the kernel. Must be an odd number.
- `kernelHeight`: The height of the kernel. Must be an odd number.
- `kernelWeights`: A pointer to an array of `kernelWidth * kernelHeight` values to be used as the kernel. These values should be in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/init(device:kernelwidth:kernelheight:weights:))*