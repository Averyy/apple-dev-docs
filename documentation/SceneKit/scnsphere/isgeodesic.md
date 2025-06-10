# isGeodesic

**Framework**: SceneKit  
**Kind**: property

A Boolean value specifying whether SceneKit uses a geodesic polygon mesh to render the sphere.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isGeodesic: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false), specifying that SceneKit constructs a sphere mesh using a rectangular grid, like the lines of latitude and longitude on a globe of the Earth. This type of sphere mesh is efficient for most uses, but can cause texture distortion in the areas near its poles.

A value of [`true`](https://developer.apple.com/documentation/swift/true) specifies that SceneKit constructs a sphere mesh by successively subdividing an icosahedron, creating a grid of uniformly sized triangles across the entire surface of the sphere, as shown below.

![None](https://docs-assets.developer.apple.com/published/b48fa37a7c8ec555f6b70091d7f50180/media-2929813%402x.png)

## See Also

- [var segmentCount: Int](scnsphere/segmentcount.md)
  A number determining the detail of the polygon mesh SceneKit uses to render the sphere. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnsphere/isgeodesic)*