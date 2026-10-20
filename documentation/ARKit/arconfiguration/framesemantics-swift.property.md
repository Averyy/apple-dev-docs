# frameSemantics

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The set of active semantics on the frame.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var frameSemantics: ARConfiguration.FrameSemantics { get set }
```

```objc
@property (nonatomic, assign) ARFrameSemantics frameSemantics;
```

#### Discussion

You can choose whether ARKit reports information about a particular per-frame metric, or *semantic*. Before enabling a frame sementic, call [`supportsFrameSemantics(_:)`](./supportsframesemantics%28_%29.md) to ensure device support.

##### Enable 2D Body Detection

To get information about the 2D location of a person that ARKit recognizes in a frame, you enable the [`bodyDetection`](./framesemantics-swift.struct/bodydetection.md) frame semantic.

```swift
if let config = mySession.configuration as? ARBodyTrackingConfiguration {
    config.frameSemantics.insert(.bodyDetection)
    // Run the configuration to effect a frame semantics change.
    mySession.run(config)
}

```

##### Enable People Occlusion

People occlusion is a feature that enables people in the camera feed to cover your app’s virtual content.

![Illustration showing two people standing in front of a virtual object. On the left, the person is partially occluded by the virtual object, breaking the illusion that the virtual object is actually placed in the physical environment. On the right, the person occludes the virtual object which maintains the illusion that the virtual object is actually placed in the physical environment. ](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3541708@2x.png)

To indicate that a person should overlap your app’s virtual content when the person is closer to the camera than the virtual content, add the [`personSegmentationWithDepth`](./framesemantics-swift.struct/personsegmentationwithdepth.md) option to your configuration’s frame semantics.

```swift
if let config = mySession.configuration as? ARWorldTrackingConfiguration {
    config.frameSemantics.insert(.personSegmentationWithDepth)
    // Run the configuration to effect a frame semantics change.
    mySession.run(config)
}

```

![Screenshot of two people in the camera feed with a virtual object between them. The person who’s in front of the virtual object occludes the virtual object, and the person behind the virtual object is occluded by the virtual object.](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3541707@2x.png)

To indicate that a person should overlap your app’s virtual content regardless of the person’s depth in the scene, use the [`personSegmentation`](./framesemantics-swift.struct/personsegmentation.md) frame semantic instead. This option is particularly appropriate for green-screen scenarios.

![Screenshot of two people in the camera feed standing in front of a virtual background.](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3541705@2x.png)

Standard renderers ([`ARView`](../../RealityKit/arview.md), and [`ARSCNView`](../arscnview.md)) implement people occlusion for you. See [Occluding virtual content with people](../occluding-virtual-content-with-people.md) for a sample app that demonstrates people occlusion in RealityKit.

If you implement your own renderer, use [`segmentationBuffer`](../arframe/segmentationbuffer.md) and [`estimatedDepthData`](../arframe/estimateddepthdata.md) to implement people occlusion yourself. [`ARMatteGenerator`](../armattegenerator.md) helps you by providing masks. For a sample app that demonstrates matte generator and people occlusion, see [Effecting People Occlusion in Custom Renderers](../effecting-people-occlusion-in-custom-renderers.md).

If you enable Scene Reconstruction, ARKit adjusts the mesh according to any people ARKit may detect in the camera feed. ARKit removes any part of the scene mesh that overlaps with people, as defined by the with- or without-depth frame semantics. For more information about scene reconstruction, see [Visualizing and interacting with a reconstructed scene](../visualizing-and-interacting-with-a-reconstructed-scene.md).

## See Also

### Enabling frame features
- [ARConfiguration.FrameSemantics](./framesemantics-swift.struct.md)
  Types of optional frame features you can enable in your app.
- [class func supportsFrameSemantics(ARConfiguration.FrameSemantics) -> Bool](./supportsframesemantics%28_%29.md)
  Checks whether a particular feature is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.property)*