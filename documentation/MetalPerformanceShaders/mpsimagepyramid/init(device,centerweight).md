# init(device:centerWeight:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initialize a downwards 5-tap image pyramid with a central weight parameter and device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice, centerWeight: Float)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device centerWeight:(float) centerWeight;
```

#### Return Value

A valid [`MPSImagePyramid`](../mpsimagepyramid.md) object or `nil`, if failure.

## Parameters

- `device`: The device the filter will run on.
- `centerWeight`: Defines the form of the filter kernel through the outer product `ww^T`, where `w = [(1/4 - a/2), 1/4, a, 1/4, (1/4 - a/2)]^T` and `a` is the value of `centerWeight`.

## See Also

### Methods
- [convenience init(device: any MTLDevice)](./init%28device%29.md)
  Initializes a downwards 5-tap image pyramid with the default filter kernel and device.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights: UnsafePointer<Float>)](./init%28device,kernelwidth,kernelheight,weights%29.md)
  Initialize a downwards n-tap image pyramid with a custom filter kernel and device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/init(device:centerweight:))*