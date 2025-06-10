# init(extruding:extrusionOptions:)

**Framework**: RealityKit  
**Kind**: init

Synchronously generates a 3D mesh by extruding a 2D path.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(extruding path: Path, extrusionOptions: MeshResource.ShapeExtrusionOptions = ShapeExtrusionOptions()) throws
```

#### Discussion

The filled area of the path is determined using the even-odd winding rule (see [`Filling a Path`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_paths/dq_paths.html#//apple_ref/doc/uid/TP30001066-CH211-TPXREF106) in the [`Quartz 2D Programming Guide Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html)). The provided path needs to satisfy the following conditions, or behavior is undefined:

1. Subpaths contains no self intersections.
2. Subpaths do not intersect each other.
3. All subpaths are closed.

## Parameters

- `path`: A path that contains the starting shape for the 3D mesh geometry.
- `extrusionOptions`: A configuration for extruding the path in 3D.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/init(extruding:extrusionoptions:))*