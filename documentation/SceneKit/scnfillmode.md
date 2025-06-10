# SCNFillMode

**Framework**: SceneKit  
**Kind**: enum

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
enum SCNFillMode
```

## Topics

### Enumeration Cases
- [SCNFillMode.fill](scnfillmode/fill.md)
- [SCNFillMode.lines](scnfillmode/lines.md)
### Initializers
- [init?(rawValue: UInt)](scnfillmode/init(rawvalue:).md)

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
- [enum SCNCullMode](scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](scnmaterial/fillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfillmode)*