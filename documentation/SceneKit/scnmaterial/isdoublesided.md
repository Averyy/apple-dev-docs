# isDoubleSided

**Framework**: SceneKit  
**Kind**: property

A Boolean value that determines whether SceneKit renders both front and back faces of a surface.

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
var isDoubleSided: Bool { get set }
```

#### Discussion

Polygons in a SceneKit mesh are, by default, single-sided. Each one contain a , which identifies the side of the polygon that’s the visible side. SceneKit uses that normal vector to determine which polygons are  that point toward the camera, and which are  that point away from it. When `doubleSided` is [`false`](https://developer.apple.com/documentation/swift/false) (the default value), SceneKit only renders front faces to improve performance.

If you change this property’s value to [`true`](https://developer.apple.com/documentation/swift/true), SceneKit renders both the front and back surfaces of every polygon.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md). Animating this property fades between the results of rendering with each state.

## See Also

- [var isLitPerPixel: Bool](scnmaterial/islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var cullMode: SCNCullMode](scnmaterial/cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)
- [enum SCNFillMode](scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/isdoublesided)*