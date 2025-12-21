# isLitPerPixel

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.

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
var isLitPerPixel: Bool { get set }
```

#### Discussion

When this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), SceneKit performs lighting calculations independently for each rendered pixel. This approach provides better rendering quality, but can adversely impact rendering performance.

If you change this property’s value to [`false`](https://developer.apple.com/documentation/Swift/false), SceneKit performs lighting calculations for each vertex in a geometry, and allows the GPU to interpolate lighting results across the pixels in between vertices. Depending on the shape and vertex count of a geometry’s surface and the material properties being rendered, this approach may improve rendering performance without much noticeable impact on visual quality.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

## See Also

- [var isDoubleSided: Bool](scnmaterial/isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](scnmaterial/cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)
- [enum SCNFillMode](scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/islitperpixel)*