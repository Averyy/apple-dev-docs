# cullMode

**Framework**: SceneKit  
**Kind**: property

The mode determining which faces of a surface SceneKit renders. Animatable.

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
var cullMode: SCNCullMode { get set }
```

#### Discussion

The vertex data and normal vectors in a geometry designate which side of each polygon is to be considered its front face, and the geometry’s orientation with respect to the camera determines which front surfaces are currently visible. Typically, back-facing surfaces are found only on the interior of a closed geometry, obscured by front-facing surfaces, so rendering these surfaces has a performance cost but no visible effect.

This property’s default value is [`SCNCullBack`](scncullback.md), specifying that SceneKit should cull, or not render, back-facing surfaces. You can change this property’s value to cause SceneKit to render only the back surfaces of a material instead. See [`SCNCullMode`](scncullmode.md) for available values.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md). Animating this property fades between the results of rendering with each state

## See Also

- [var isLitPerPixel: Bool](scnmaterial/islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var isDoubleSided: Bool](scnmaterial/isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [enum SCNCullMode](scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)
- [enum SCNFillMode](scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/cullmode)*