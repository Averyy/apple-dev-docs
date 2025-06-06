# ARFrame.SegmentationClass

**Framework**: ARKit  
**Kind**: enum

A categorization of a pixel that defines a type of content you use to occlude your app’s virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum SegmentationClass
```

#### Overview

ARKit applies the categories defined in this class based on its interpretation of the camera feed’s pixel data. Only people are identified in a camera feed, and therefore the available pixel classifications are either [`ARFrame.SegmentationClass.person`](arframe/segmentationclass/person.md) or [`ARFrame.SegmentationClass.none`](arframe/segmentationclass/none.md).

## Topics

### Classifying Pixels
- [ARFrame.SegmentationClass.person](arframe/segmentationclass/person.md)
  A classification of a pixel in the segmentation buffer as part of a person.
- [ARFrame.SegmentationClass.none](arframe/segmentationclass/none.md)
  A classification of a pixel in the segmentation buffer as unidentified.
### Initializers
- [init?(rawValue: UInt8)](arframe/segmentationclass/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var detectedBody: ARBody2D?](arframe/detectedbody.md)
  The screen position information of a body that ARKit recognizes in the camera image.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [var segmentationBuffer: CVPixelBuffer?](arframe/segmentationbuffer.md)
  A buffer that contains pixel information identifying the shape of objects from the camera feed that you use to occlude virtual content.
- [var estimatedDepthData: CVPixelBuffer?](arframe/estimateddepthdata.md)
  A buffer that represents the estimated depth values from the camera feed that you use to occlude virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/segmentationclass)*