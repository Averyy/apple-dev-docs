# maxKernelDiameter()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Type Method

Queries the maximum diameter, in pixels, of the filter window supported by the median filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func maxKernelDiameter() -> Int
```

```objc
+ (NSUInteger) maxKernelDiameter;
```

#### Return Value

Returns the maximum diameter, in pixels, of the filter window supported by the median filter.

## See Also

### Methods
- [init(device: any MTLDevice, kernelDiameter: Int)](./init%28device,kerneldiameter%29.md)
  Initializes a filter for a particular kernel size and device.
- [class func minKernelDiameter() -> Int](./minkerneldiameter%28%29.md)
  Queries the minimum diameter, in pixels, of the filter window supported by the median filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/maxkerneldiameter())*