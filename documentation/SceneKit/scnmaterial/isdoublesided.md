# isDoubleSided

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether SceneKit renders both front and back faces of a surface.

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
var isDoubleSided: Bool { get set }
```

```objc
@property (nonatomic, getter=isDoubleSided) BOOL doubleSided;
```

#### Discussion

Polygons in a SceneKit mesh are, by default, single-sided. Each one contain a *normal vector*, which identifies the side of the polygon that’s the visible side. SceneKit uses that normal vector to determine which polygons are *front faces* that point toward the camera, and which are *back faces* that point away from it. When `doubleSided` is [`false`](../../Swift/false.md) (the default value), SceneKit only renders front faces to improve performance.

If you change this property’s value to [`true`](../../Swift/true.md), SceneKit renders both the front and back surfaces of every polygon.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

## See Also

### Customizing Rendered Appearance
- [var isLitPerPixel: Bool](./islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var cullMode: SCNCullMode](./cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](../scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](./cullmode.md) property.
- [var fillMode: SCNFillMode](./fillmode.md)
- [enum SCNFillMode](../scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/isdoublesided)*