# Occluding virtual content with people

**Framework**: ARKit  
**Role**: Sample Code  
**Download**: [OccludingVirtualContentWithPeople.zip](https://docs-assets.developer.apple.com/published/738550aba62d/OccludingVirtualContentWithPeople.zip)

Cover your app’s virtual content with people that ARKit perceives in the camera feed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 16.0+

## Overview

By default, virtual content covers anything in the camera feed. For example, when a person passes in front of a virtual object, the object is drawn on top of the person, which can break the illusion of the AR experience.

![Screenshot of virtual books drawn on top of a person.](https://developer.apple.com/tutorials/images/com.apple.arkit/figure1-annotated.png)

To cover your app’s virtual content with people that ARKit perceives in the camera feed, you enable *people occlusion*. Your app can then render a virtual object behind people who pass in front of the camera. ARKit accomplishes the occlusion by identifying regions in the camera feed where people reside, and preventing virtual content from drawing into that region’s pixels.

![Screenshot of the virtual books behind the person.](https://developer.apple.com/tutorials/images/com.apple.arkit/figure2-annotated.png)

This sample renders its graphics using RealityKit, but you can follow the same steps to use people occlusion with SceneKit. To enable people occlusion in Metal apps, see [Effecting People Occlusion in Custom Renderers](./effecting-people-occlusion-in-custom-renderers.md).

## Verify device support for people occlusion

People occlusion is supported on Apple A12 and later devices. Before attempting to enable people occlusion, verify that the user’s device supports it.

```swift
guard ARWorldTrackingConfiguration.supportsFrameSemantics(.personSegmentationWithDepth) else {
    fatalError("People occlusion is not supported on this device.")
}
```

> **Note**: If your device doesn’t support people occlusion, the sample stops. However, if the user’s device doesn’t support people occlusion, you should continue your AR experience without it.

## Enable people occlusion

If the user’s device supports people occlusion, enable it by adding the

arconfiguration/framesemantics/3194576-personsegmentationwithdepth [`personSegmentationWithDepth`](./arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md) option to your configuration’s frame semantics.

```swift
config.frameSemantics.insert(.personSegmentationWithDepth)
```

Any time you change your session’s [`configuration`](./arsession/configuration.md), rerun the session to effect the configuration change.

```swift
arView.session.run(config)
```

The [`personSegmentationWithDepth`](./arconfiguration/framesemantics-swift.struct/personsegmentationwithdepth.md) option specifies that a person occludes a virtual object only when the person is closer to the camera than the virtual object.

![Screenshot of people occlusion with depth.](https://developer.apple.com/tutorials/images/com.apple.arkit/figure3-annotated.png)

Alternatively, the [`personSegmentation`](./arconfiguration/framesemantics-swift.struct/personsegmentation.md) frame semantic gives you the option of always occluding virtual content with any people that ARKit perceives in the camera feed irrespective of depth. This technique is useful, for example, in green-screen scenarios.

![Screenshot of people occlusion with virtual background.](https://developer.apple.com/tutorials/images/com.apple.arkit/figure4-annotated.png)

## Disable people occlusion

You might choose to disable people occlusion for performance reasons if, for example, no virtual content is present in the scene, or if the device has reached a serious or critical [`thermalState`](../Foundation/processinfo/thermalstate-swift.property.md) (see [`ProcessInfo.ThermalState`](../Foundation/processinfo/thermalstate-swift.enum.md)). To temporarily disable people occlusion, remove that option from your app’s [`frameSemantics`](./arconfiguration/framesemantics-swift.property.md).

```swift
config.frameSemantics.remove(.personSegmentationWithDepth)
```

Then, rerun your session to effect the configuration change.

```swift
arView.session.run(config)
```

## See Also

### Occlusion
- [Effecting People Occlusion in Custom Renderers](./effecting-people-occlusion-in-custom-renderers.md)
  Occlude your app’s virtual content where ARKit recognizes people in the camera feed by using matte generator.
- [Visualizing and interacting with a reconstructed scene](./visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [class ARMatteGenerator](./armattegenerator.md)
  An object that creates matte textures you use to occlude your app’s virtual content with people, that ARKit recognizes in the camera feed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/occluding-virtual-content-with-people)*