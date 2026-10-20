# depthMap

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The estimated distance from the device to its environment, in meters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
unowned(unsafe) var depthMap: CVPixelBuffer { get }
```

```objc
@property (nonatomic, assign, readonly) CVPixelBufferRef depthMap;
```

#### Discussion

For custom renderers, if you create a texture to send depth data to the GPU, choose a [`MTLPixelFormat`](../../Metal/mtlpixelformat.md) according to the [`depthMap`](./depthmap.md) pixel format. Call [`CVPixelBufferGetPixelFormatType(_:)`](../../CoreVideo/cvpixelbuffergetpixelformattype%28_%29.md) on the [`depthMap`](./depthmap.md) to get its format. For example, if at runtime the [`depthMap`](./depthmap.md) format is [`kCVPixelFormatType_DepthFloat32`](../../CoreVideo/kcvpixelformattype_depthfloat32.md)  ([`OSType`](../../kernel/ostype.md) ``fdep``), use  [`MTLPixelFormat.r32Float`](../../Metal/mtlpixelformat/r32float.md).

## See Also

### Depth Information
- [var confidenceMap: CVPixelBuffer?](./confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.
- [enum ARConfidenceLevel](../arconfidencelevel.md)
  Degrees to which the framework is confident about depth-data accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardepthdata/depthmap)*