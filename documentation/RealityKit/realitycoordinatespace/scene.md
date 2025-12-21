# scene

**Framework**: RealityKit  
**Kind**: property

The coordinate space that represents ARKit world space.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
static var scene: SceneRealityCoordinateSpace { get }
```

#### Discussion

In a visionOS window or volume, or when using the [`virtual`](realityviewcamera/virtual.md) camera on any other platform, this space represents the center of the scene’s owning [`RealityView`](realityview.md).

When in a visionOS Immersive Space, or using the `RealityViewCamera/worldTracking` camera in iOS, the `scene` coordinate space is the [`ARKit`](https://developer.apple.com/documentation/ARKit) world origin.

> **Note**: This static type is equivalent to a [`SceneRealityCoordinateSpace`](scenerealitycoordinatespace.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitycoordinatespace/scene)*