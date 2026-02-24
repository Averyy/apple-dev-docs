# init(device:linearGrayColorTransform:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a Sobel filter on a given device using a specific color transform.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, linearGrayColorTransform transform: UnsafePointer<Float>)
```

#### Return Value

An initialized Sobel filter object.

## Parameters

- `device`: The Metal device the filter will run on.
- `transform`: The color transform to use. This matrix is an array of 3 floats that describes the RGB-to-grayscale color transform: `Luminance = transform[0] * pixel.x + transform[1] * pixel.y + transform[2] * pixel.z`

## See Also

- [convenience init(device: any MTLDevice)](mpsimagesobel/init(device:).md)
  Initializes a Sobel filter on a given device using the default color transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/init(device:lineargraycolortransform:))*