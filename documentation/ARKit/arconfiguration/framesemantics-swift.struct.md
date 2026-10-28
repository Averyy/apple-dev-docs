# ARConfiguration.FrameSemantics

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Types of optional frame features you can enable in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
struct FrameSemantics
```

```c
enum ARFrameSemantics : NSUInteger;
```

## Discussion

A frame semantic represents 2D information that ARKit extracts from a frame.

## Topics

### Creating a Feature
- [init(rawValue: UInt)](./framesemantics-swift.struct/init%28rawvalue%29.md)
  Creates a frame semantics feature.
### Tracking Bodies in 2D
- [static var bodyDetection: ARConfiguration.FrameSemantics](./framesemantics-swift.struct/bodydetection.md)
  An option that indicates that 2D body detection is enabled.
### Occluding Virtual Content with People
- [static var personSegmentation: ARConfiguration.FrameSemantics](./framesemantics-swift.struct/personsegmentation.md)
  An option that indicates that people occlude your app’s virtual content.
- [static var personSegmentationWithDepth: ARConfiguration.FrameSemantics](./framesemantics-swift.struct/personsegmentationwithdepth.md)
  An option that indicates that people occlude your app’s virtual content depending on depth.
### Accessing Depth
- [static var sceneDepth: ARConfiguration.FrameSemantics](./framesemantics-swift.struct/scenedepth.md)
  An option that provides the distance from the device to real-world objects viewed through the camera.
- [static var smoothedSceneDepth: ARConfiguration.FrameSemantics](./framesemantics-swift.struct/smoothedscenedepth.md)
  An option that provides the distance from the device to real-world objects, averaged across several frames.
### Disabling Features
- [ARFrameSemanticNone](../arframesemantics/arframesemanticnone.md)
  An option that indicates no frame features are enabled.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Enabling frame features
- [var frameSemantics: ARConfiguration.FrameSemantics](./framesemantics-swift.property.md)
  The set of active semantics on the frame.
- [class func supportsFrameSemantics(ARConfiguration.FrameSemantics) -> Bool](./supportsframesemantics%28_%29.md)
  Checks whether a particular feature is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct)*