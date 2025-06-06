# depthMap

**Framework**: ARKit  
**Kind**: property

The estimated distance from the device to its environment, in meters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
unowned(unsafe) var depthMap: CVPixelBuffer { get }
```

#### Discussion

For custom renderers, if you create a texture to send depth data to the GPU, choose a [`MTLPixelFormat`](https://developer.apple.com/documentation/Metal/MTLPixelFormat) according to the [`depthMap`](ardepthdata/depthmap.md) pixel format. Call [`CVPixelBufferGetPixelFormatType(_:)`](https://developer.apple.com/documentation/CoreVideo/CVPixelBufferGetPixelFormatType(_:)) on the [`depthMap`](ardepthdata/depthmap.md) to get its format. For example, if at runtime the [`depthMap`](ardepthdata/depthmap.md) format is [`kCVPixelFormatType_DepthFloat32`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_DepthFloat32)  ([`OSType`](https://developer.apple.com/documentation/kernel/ostype) ``fdep``), use  [`MTLPixelFormat.r32Float`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/r32Float).

## See Also

- [var confidenceMap: CVPixelBuffer?](ardepthdata/confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.
- [enum ARConfidenceLevel](arconfidencelevel.md)
  Degrees to which the framework is confident about depth-data accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardepthdata/depthmap)*