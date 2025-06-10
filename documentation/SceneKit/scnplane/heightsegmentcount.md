# heightSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions in the plane’s surface along its vertical axis. Animatable.

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
var heightSegmentCount: Int { get set }
```

#### Discussion

A larger number of segments adds more vertex data to the geometry. Although the plane is flat, extra vertices can be useful for lighting or other special effects. For example, you can add a GLSL source code snippet to the plane’s [`shaderModifiers`](scnshadable/shadermodifiers.md) property that modulates the position of each vertex. Adding vertices increases rendering cost, so use the minimal segment count that produces your desired visual effect.

The default segment count is `1`. Setting this property’s value to a number less than `1` results in undefined behavior. If the [`cornerRadius`](scnplane/cornerradius.md) property’s value is greater than zero, the segment count applies to the area between corners.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var cornerSegmentCount: Int](scnplane/cornersegmentcount.md)
  The number of line segments used to create each rounded corner of the plane. Animatable.
- [var widthSegmentCount: Int](scnplane/widthsegmentcount.md)
  The number of subdivisions in the plane’s surface along its horizontal axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane/heightsegmentcount)*