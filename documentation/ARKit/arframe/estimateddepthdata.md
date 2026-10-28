# estimatedDepthData

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A buffer that represents the estimated depth values from the camera feed that you use to occlude virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var estimatedDepthData: CVPixelBuffer? { get }
```

```objc
@property (nonatomic, readonly, nullable) CVPixelBufferRef estimatedDepthData;
```

## Discussion

Each non-background pixel in the segmentation buffer maps to a depth value in this buffer. Use this to occlude people from the rendering of your app’s virtual content.

If you implement a custom renderer, you apply this property by using alpha and depth mattes provided with [`ARMatteGenerator`](../armattegenerator.md).

Apps using one of the standard renderers don’t need this property to occlude virtual content with people. The standard renderers ([`ARView`](../../RealityKit/arview.md), [`ARSCNView`](../arscnview.md), and [`ARSKView`](../arskview.md)) enable people occlusion when you add [`personSegmentation`](../arconfiguration/framesemantics-swift.struct/personsegmentation.md) or [`personSegmentationWithDepth`](../arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md) to your configuration’s [`frameSemantics`](../arconfiguration/framesemantics-swift.property.md).

## See Also

### Checking for people
- [var detectedBody: ARBody2D?](./detectedbody.md)
  The screen position information of a body that ARKit recognizes in the camera image.
- [class ARBody2D](../arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [var segmentationBuffer: CVPixelBuffer?](./segmentationbuffer.md)
  A buffer that contains pixel information identifying the shape of objects from the camera feed that you use to occlude virtual content.
- [ARFrame.SegmentationClass](./segmentationclass.md)
  A categorization of a pixel that defines a type of content you use to occlude your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/estimateddepthdata)*