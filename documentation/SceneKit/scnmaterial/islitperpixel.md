# isLitPerPixel

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.

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
var isLitPerPixel: Bool { get set }
```

```objc
@property (nonatomic, getter=isLitPerPixel) BOOL litPerPixel;
```

#### Discussion

When this property’s value is [`true`](../../Swift/true.md) (the default), SceneKit performs lighting calculations independently for each rendered pixel. This approach provides better rendering quality, but can adversely impact rendering performance.

If you change this property’s value to [`false`](../../Swift/false.md), SceneKit performs lighting calculations for each vertex in a geometry, and allows the GPU to interpolate lighting results across the pixels in between vertices. Depending on the shape and vertex count of a geometry’s surface and the material properties being rendered, this approach may improve rendering performance without much noticeable impact on visual quality.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

## See Also

### Customizing Rendered Appearance
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](./cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](../scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](./cullmode.md) property.
- [var fillMode: SCNFillMode](./fillmode.md)
- [enum SCNFillMode](../scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/islitperpixel)*