# pointSize

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The width of each point in the geometry element, as measured in the geometry’s local 3D coordinate space.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var pointSize: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat pointSize;
```

#### Discussion

Some visual effects call for rendering a geometry as a collection of individual points—that is, a point cloud, not a solid surface or wireframe mesh. When you use this option, SceneKit can render each point as a small 2D surface that always faces the camera. By applying a texture or custom shader to that surface, you can efficiently render many small objects at once.

To render a geometry element as a point cloud, you must set three properties: [`pointSize`](./pointsize.md), [`minimumPointScreenSpaceRadius`](./minimumpointscreenspaceradius.md), and [`maximumPointScreenSpaceRadius`](./maximumpointscreenspaceradius.md). Use [`pointSize`](./pointsize.md) to determine how large each point appears in world space, so that points farther away appear as smaller 2D surfaces. Use the minimum and maximum radius properties to ensure that the on-screen rendering of each point fits within a certain range of pixel sizes.

## See Also

### Rendering Point Clouds
- [var minimumPointScreenSpaceRadius: CGFloat](./minimumpointscreenspaceradius.md)
  The smallest radius, measured in screen points, at which to render any point in the geometry element.
- [var maximumPointScreenSpaceRadius: CGFloat](./maximumpointscreenspaceradius.md)
  The largest radius, measured in screen points, at which to render any point in the geometry element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometryelement/pointsize)*