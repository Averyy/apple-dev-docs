# minKernelDiameter()

**Framework**: Metal Performance Shaders  
**Kind**: method

Queries the minimum diameter, in pixels, of the filter window supported by the median filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func minKernelDiameter() -> Int
```

#### Return Value

Returns the minimum diameter, in pixels, of the filter window supported by the median filter.

## See Also

- [init(device: any MTLDevice, kernelDiameter: Int)](mpsimagemedian/init(device:kerneldiameter:).md)
  Initializes a filter for a particular kernel size and device.
- [class func maxKernelDiameter() -> Int](mpsimagemedian/maxkerneldiameter.md)
  Queries the maximum diameter, in pixels, of the filter window supported by the median filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/minkerneldiameter())*