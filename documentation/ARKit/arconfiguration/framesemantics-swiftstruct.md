# ARConfiguration.FrameSemantics

**Framework**: ARKit  
**Kind**: struct

Types of optional frame features you can enable in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct FrameSemantics
```

#### Discussion

A frame semantic represents 2D information that ARKit extracts from a frame.

## Topics

### Creating a Feature
- [init(rawValue: UInt)](arconfiguration/framesemantics-swift.struct/init(rawvalue:).md)
  Creates a frame semantics feature.
### Tracking Bodies in 2D
- [static var bodyDetection: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/bodydetection.md)
  An option that indicates that 2D body detection is enabled.
### Occluding Virtual Content with People
- [static var personSegmentation: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/personsegmentation.md)
  An option that indicates that people occlude your app’s virtual content.
- [static var personSegmentationWithDepth: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md)
  An option that indicates that people occlude your app’s virtual content depending on depth.
### Accessing Depth
- [static var sceneDepth: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/scenedepth.md)
  An option that provides the distance from the device to real-world objects viewed through the camera.
- [static var smoothedSceneDepth: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/smoothedscenedepth.md)
  An option that provides the distance from the device to real-world objects, averaged across several frames.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var frameSemantics: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.property.md)
  The set of active semantics on the frame.
- [class func supportsFrameSemantics(ARConfiguration.FrameSemantics) -> Bool](arconfiguration/supportsframesemantics(_:).md)
  Checks whether a particular feature is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct)*