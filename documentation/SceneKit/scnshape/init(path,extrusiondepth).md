# init(path:extrusionDepth:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a shape geometry with the specified path and extrusion depth.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
convenience init(path: UIBezierPath?, extrusionDepth: CGFloat)
```

*macOS*

```swift
convenience init(path: NSBezierPath?, extrusionDepth: CGFloat)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) shapeWithPath:(UIBezierPath *) path extrusionDepth:(CGFloat) extrusionDepth;
```

*macOS*

```objc
+ (instancetype) shapeWithPath:(NSBezierPath *) path extrusionDepth:(CGFloat) extrusionDepth;
```

#### Return Value

A shape geometry.

#### Discussion

SceneKit determines the filled area of the path using the even-odd winding rule (see [Winding Rules](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html#//apple_ref/doc/uid/TP40003290-CH206-BAJIJJGD) in [Cocoa Drawing Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)) and extrudes this area to create a three-dimensional geometry. The result of extruding a self-intersecting path is undefined.

The extruded shape is centered at the zero point of its z-axis. For example, an extrusion depth of `1.0` creates a shape that extends from `-0.5` to `0.5` along the z-axis. An extrusion depth of zero creates a flat, one-sided shape.

The path’s flatness (see [`flatness`](../../AppKit/nsbezierpath/flatness.md) in [`NSBezierPath`](../../AppKit/nsbezierpath.md)) determines the level of detail SceneKit uses in building a three-dimensional shape from the path. A larger flatness value results in fewer polygons to render, increasing performance, and a smaller flatness value increases the smoothness of curves at a cost to performance.

## Parameters

- `path`: The two-dimensional path forming the basis of the shape.
- `extrusionDepth`: The thickness of the extruded shape along the z-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/init(path:extrusiondepth:))*