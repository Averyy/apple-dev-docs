# init(device:kernelWidth:kernelHeight:values:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes the kernel with a specified width, height, and weight values.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, values: UnsafePointer<Float>)
```

#### Return Value

Returns an initialized kernel object with specific width, height, and weight values.

#### Discussion

Each dilate shape probe defines a 3D surface of values. These are arranged in order left to right, then top to bottom in a 1D array. (`values[kernelWidth*y+x] = probe[y][x]`)

Values should be generally be in the range `[0,1]` with the center pixel tending towards `0` and edges towards `1`. However, any numerical value is allowed. Calculations are subject to the usual floating-point rounding error.

## Parameters

- `device`: The Metal device the filter will run on.
- `kernelWidth`: The width of the kernel. Must be an odd number.
- `kernelHeight`: The height of the kernel. Must be an odd number.
- `values`: The set of values to use as the dilate probe. The values are copied into the filter. To avoid image lightening or darkening, the center value should be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate/init(device:kernelwidth:kernelheight:values:))*