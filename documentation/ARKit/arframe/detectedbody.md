# detectedBody

**Framework**: ARKit  
**Kind**: property

The screen position information of a body that ARKit recognizes in the camera image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var detectedBody: ARBody2D? { get }
```

#### Discussion

To enable 2D body detection, you add the [`bodyDetection`](arconfiguration/framesemantics-swift.struct/bodydetection.md) frame semantic to your configuration’s [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) property, or run your session with an [`ARBodyTrackingConfiguration`](arbodytrackingconfiguration.md), in which body detection is enabled by default.

## See Also

- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [var segmentationBuffer: CVPixelBuffer?](arframe/segmentationbuffer.md)
  A buffer that contains pixel information identifying the shape of objects from the camera feed that you use to occlude virtual content.
- [var estimatedDepthData: CVPixelBuffer?](arframe/estimateddepthdata.md)
  A buffer that represents the estimated depth values from the camera feed that you use to occlude virtual content.
- [ARFrame.SegmentationClass](arframe/segmentationclass.md)
  A categorization of a pixel that defines a type of content you use to occlude your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/detectedbody)*