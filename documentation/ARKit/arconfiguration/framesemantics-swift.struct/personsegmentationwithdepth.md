# personSegmentationWithDepth

**Framework**: ARKit  
**Kind**: property

An option that indicates that people occlude your app’s virtual content depending on depth.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var personSegmentationWithDepth: ARConfiguration.FrameSemantics { get }
```

#### Discussion

The [`personSegmentationWithDepth`](arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md) frame semantic specifies that any person ARKit detects in the camera feed should occlude virtual content, depending on the person’s depth in the scene.

When this option is enabled, ARKit sets the [`estimatedDepthData`](arframe/estimateddepthdata.md) and [`segmentationBuffer`](arframe/segmentationbuffer.md) properties to serve as a foundation for people occlusion. The standard renderers ([`ARView`](https://developer.apple.com/documentation/RealityKit/ARView), and [`ARSCNView`](arscnview.md)) use those properties to implement people occlusion for you. See [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) for more information.

## See Also

- [static var personSegmentation: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/personsegmentation.md)
  An option that indicates that people occlude your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth)*