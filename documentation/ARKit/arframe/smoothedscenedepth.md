# smoothedSceneDepth

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An average of distance measurements between a device’s rear camera and real-world objects that creates smoother visuals in an AR experience.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var smoothedSceneDepth: ARDepthData? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) ARDepthData * smoothedSceneDepth;
```

## Discussion

This property describes the distance between a device’s camera and objects or areas in the real world, including ARKit’s confidence in the estimated distance. This is similar to [`sceneDepth`](./scenedepth.md) except that the framework smoothes the depth data over time to lessen its frame-to-frame delta.

This property is `nil` by default. Add the [`smoothedSceneDepth`](../arconfiguration/framesemantics-swift.struct/smoothedscenedepth.md) frame semantic to your configuration’s [`frameSemantics`](../arconfiguration/framesemantics-swift.property.md) to instruct the framework to populate this value with [`ARDepthData`](../ardepthdata.md) captured by the LiDAR scanner.

Call [`supportsFrameSemantics(_:)`](../arconfiguration/supportsframesemantics%28_%29.md) on your app’s configuration to support smoothed scene depth on select devices and configurations.

## See Also

### Accessing scene data
- [var lightEstimate: ARLightEstimate?](./lightestimate.md)
  An estimate of lighting conditions based on the camera image.
- [var rawFeaturePoints: ARPointCloud?](./rawfeaturepoints.md)
  The current intermediate results of the scene analysis ARKit uses to perform world tracking.
- [var capturedDepthData: AVDepthData?](./captureddepthdata.md)
  Depth data captured in front-camera experiences.
- [var capturedDepthDataTimestamp: TimeInterval](./captureddepthdatatimestamp.md)
  The time at which depth data for the frame (if any) was captured.
- [var sceneDepth: ARDepthData?](./scenedepth.md)
  Data on the distance between a device’s rear camera and real-world objects in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/smoothedscenedepth)*