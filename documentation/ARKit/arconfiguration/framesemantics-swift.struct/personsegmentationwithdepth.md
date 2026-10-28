# personSegmentationWithDepth

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An option that indicates that people occlude your app’s virtual content depending on depth.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
static var personSegmentationWithDepth: ARConfiguration.FrameSemantics { get }
```

```c
ARFrameSemanticPersonSegmentationWithDepth
```

## Discussion

The [`personSegmentationWithDepth`](./personsegmentationwithdepth.md) frame semantic specifies that any person ARKit detects in the camera feed should occlude virtual content, depending on the person’s depth in the scene.

When this option is enabled, ARKit sets the [`estimatedDepthData`](../../arframe/estimateddepthdata.md) and [`segmentationBuffer`](../../arframe/segmentationbuffer.md) properties to serve as a foundation for people occlusion. The standard renderers ([`ARView`](../../../RealityKit/arview.md), and [`ARSCNView`](../../arscnview.md)) use those properties to implement people occlusion for you. See [`frameSemantics`](../framesemantics-swift.property.md) for more information.

## See Also

### Occluding Virtual Content with People
- [static var personSegmentation: ARConfiguration.FrameSemantics](./personsegmentation.md)
  An option that indicates that people occlude your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth)*