# personSegmentation

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

An option that indicates that people occlude your app’s virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
static var personSegmentation: ARConfiguration.FrameSemantics { get }
```

```c
ARFrameSemanticPersonSegmentation
```

## Discussion

The [`personSegmentation`](./personsegmentation.md) frame semantic specifies that any person ARKit detects in the camera feed occludes virtual content, regardless of the person’s depth in the scene.

When this option is enabled, ARKit sets the [`estimatedDepthData`](../../arframe/estimateddepthdata.md) and [`segmentationBuffer`](../../arframe/segmentationbuffer.md) properties to serve as a foundation for people occlusion. The standard renderers ([`ARView`](../../../RealityKit/arview.md), and [`ARSCNView`](../../arscnview.md)) use those properties to implement people occlusion for you. See [`frameSemantics`](../framesemantics-swift.property.md) for more information.

## See Also

### Occluding Virtual Content with People
- [static var personSegmentationWithDepth: ARConfiguration.FrameSemantics](./personsegmentationwithdepth.md)
  An option that indicates that people occlude your app’s virtual content depending on depth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/personsegmentation)*