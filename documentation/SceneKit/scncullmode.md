# SCNCullMode

**Framework**: SceneKit  
**Kind**: enum

The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.

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
enum SCNCullMode
```

#### Overview

The vertex data and normal vectors in a geometry designate which side of each polygon is to be considered its front face, and the geometry’s orientation with respect to the camera determines which front surfaces are currently visible. Typically, back-facing surfaces are found only on the interior of a closed geometry, obscured by front-facing surfaces, so rendering these surfaces has a performance cost but no visible effect.

## Topics

### Enumeration Cases
- [SCNCullMode.back](scncullmode/back.md)
- [SCNCullMode.front](scncullmode/front.md)
### Initializers
- [init?(rawValue: Int)](scncullmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isLitPerPixel: Bool](scnmaterial/islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var isDoubleSided: Bool](scnmaterial/isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](scnmaterial/cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)
- [enum SCNFillMode](scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncullmode)*