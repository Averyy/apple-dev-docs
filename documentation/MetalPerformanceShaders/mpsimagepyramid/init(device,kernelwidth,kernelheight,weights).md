# init(device:kernelWidth:kernelHeight:weights:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initialize a downwards n-tap image pyramid with a custom filter kernel and device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights kernelWeights: UnsafePointer<Float>)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device kernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight weights:(const float *) kernelWeights;
```

## Return Value

A valid [`MPSImagePyramid`](../mpsimagepyramid.md) object or `nil`, if failure.

## Parameters

- `device`: The device the filter will run on.
- `kernelWidth`: The width of the filter kernel.
- `kernelHeight`: The height of the filter kernel.
- `kernelWeights`: A pointer to an array of `kernelWidth*kernelHeight` values to be used as the kernel. These values are in row-major order.

## See Also

### Methods
- [convenience init(device: any MTLDevice)](./init%28device%29.md)
  Initializes a downwards 5-tap image pyramid with the default filter kernel and device.
- [convenience init(device: any MTLDevice, centerWeight: Float)](./init%28device,centerweight%29.md)
  Initialize a downwards 5-tap image pyramid with a central weight parameter and device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/init(device:kernelwidth:kernelheight:weights:))*