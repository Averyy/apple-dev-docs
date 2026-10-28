# ARMatteGenerator

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

An object that creates matte textures you use to occlude your app’s virtual content with people, that ARKit recognizes in the camera feed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class ARMatteGenerator
```

```objc
@interface ARMatteGenerator : NSObject
```

## Overview

Use this class when you want full control over occluding your app’s virtual content, based on people ARKit recognizes in the camera feed.

> **Note**:  Apps using one of the standard renderers  (`ARView` or [`ARSCNView`](./arscnview.md)) don’t need this class to effect people occlusion. See [`frameSemantics`](./arconfiguration/framesemantics-swift.property.md) for more information.

To assist your custom renderer with people occlusion, matte generator processes alpha and depth information in a frame’s [`segmentationBuffer`](./arframe/segmentationbuffer.md) and [`estimatedDepthData`](./arframe/estimateddepthdata.md) to provide you with matte and depth textures. You use these textures to layer people on top of your app’s virtual content.

## Topics

### Creating a Matte Generator
- [init(device: any MTLDevice, matteResolution: ARMatteGenerator.Resolution)](./armattegenerator/init%28device,matteresolution%29.md)
  Creates an AR matte generator.
### Creating an Alpha Matte Texture
- [func generateMatte(from: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture](./armattegenerator/generatematte%28from,commandbuffer%29.md)
  Generates alpha matte at either full resolution or half the resolution of the captured image.
### Creating a Depth Texture
- [func generateDilatedDepth(from: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture](./armattegenerator/generatedilateddepth%28from,commandbuffer%29.md)
  Generates dilated depth at the resolution of the segmentation stencil.
### Controlling Resolution
- [ARMatteGenerator.Resolution](./armattegenerator/resolution.md)
  A resolution for a matte texture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Occlusion
- [Occluding virtual content with people](./occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [Effecting People Occlusion in Custom Renderers](./effecting-people-occlusion-in-custom-renderers.md)
  Occlude your app’s virtual content where ARKit recognizes people in the camera feed by using matte generator.
- [Visualizing and interacting with a reconstructed scene](./visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator)*