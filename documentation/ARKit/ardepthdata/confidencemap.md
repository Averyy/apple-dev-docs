# confidenceMap

**Framework**: ARKit  
**Kind**: property

The framework’s confidence in the accuracy of the depth-map data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
unowned(unsafe) var confidenceMap: CVPixelBuffer? { get }
```

#### Discussion

The natural light of the physical environment affects the [`depthMap`](ardepthdata/depthmap.md) property such that ARKit is less confident about the accuracy of the LiDAR Scanner’s depth measurements for surfaces that are highly reflective, or that have high light absorption. This property measures the accuracy of the scene depth-data by containing an [`ARConfidenceLevel`](arconfidencelevel.md) raw-value for every component in [`depthMap`](ardepthdata/depthmap.md).

Custom renderers that process confidence data on the GPU should choose a [`MTLPixelFormat`](https://developer.apple.com/documentation/Metal/MTLPixelFormat) according to the [`confidenceMap`](ardepthdata/confidencemap.md) pixel format the app reads at runtime. Call [`CVPixelBufferGetPixelFormatType(_:)`](https://developer.apple.com/documentation/CoreVideo/CVPixelBufferGetPixelFormatType(_:)) on the [`confidenceMap`](ardepthdata/confidencemap.md) to get its format. If, for example, the [`confidenceMap`](ardepthdata/confidencemap.md) format is [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8) ([`OSType`](https://developer.apple.com/documentation/kernel/ostype) ``L008``), create a Metal texture with format [`MTLPixelFormat.r8Uint`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/r8Uint) to send confidence data to the GPU.

## See Also

- [var depthMap: CVPixelBuffer](ardepthdata/depthmap.md)
  The estimated distance from the device to its environment, in meters.
- [enum ARConfidenceLevel](arconfidencelevel.md)
  Degrees to which the framework is confident about depth-data accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardepthdata/confidencemap)*