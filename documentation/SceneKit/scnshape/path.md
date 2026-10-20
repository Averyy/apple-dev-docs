# path

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The two-dimensional path forming the basis of the shape.

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
@NSCopying
var path: UIBezierPath? { get set }
```

*macOS*

```swift
@NSCopying
var path: NSBezierPath? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) UIBezierPath * path;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSBezierPath * path;
```

#### Discussion

SceneKit determines the filled area of the path using the even-odd winding rule (see [Winding Rules](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Paths/Paths.html#//apple_ref/doc/uid/TP40003290-CH206-BAJIJJGD) in [Cocoa Drawing Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)) and extrudes this area to create a three-dimensional geometry. The result of extruding a self-intersecting path is undefined.

The path’s flatness (see [`flatness`](../../AppKit/nsbezierpath/flatness.md) in [`NSBezierPath`](../../AppKit/nsbezierpath.md)) determines the level of detail SceneKit uses in building a three-dimensional shape from the path—a larger flatness value results in fewer polygons to render, increasing performance.

## See Also

### Modifying a Shape
- [var extrusionDepth: CGFloat](./extrusiondepth.md)
  The thickness of the extruded shape along the z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/path)*