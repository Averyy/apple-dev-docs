# init(device:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a downwards 5-tap image pyramid with the default filter kernel and device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(device: any MTLDevice)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device;
```

#### Return Value

A valid [`MPSImagePyramid`](../mpsimagepyramid.md) object or `nil`, if failure.

#### Discussion

The filter kernel is the outer product of `w = [1/16, 1/4, 3/8, 1/4, 1/16]^T`, with itself.

## Parameters

- `device`: The device the filter will run on.

## See Also

### Methods
- [convenience init(device: any MTLDevice, centerWeight: Float)](./init%28device,centerweight%29.md)
  Initialize a downwards 5-tap image pyramid with a central weight parameter and device.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, weights: UnsafePointer<Float>)](./init%28device,kernelwidth,kernelheight,weights%29.md)
  Initialize a downwards n-tap image pyramid with a custom filter kernel and device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/init(device:))*