# SCNFillMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

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
enum SCNFillMode
```

```c
enum SCNFillMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [SCNFillMode.fill](./scnfillmode/fill.md)
- [SCNFillMode.lines](./scnfillmode/lines.md)
### Initializers
- [init?(rawValue: UInt)](./scnfillmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing Rendered Appearance
- [var isLitPerPixel: Bool](./scnmaterial/islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var isDoubleSided: Bool](./scnmaterial/isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](./scnmaterial/cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](./scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](./scnmaterial/cullmode.md) property.
- [var fillMode: SCNFillMode](./scnmaterial/fillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfillmode)*