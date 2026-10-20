# fillMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

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
var fillMode: SCNFillMode { get set }
```

```objc
@property (nonatomic) SCNFillMode fillMode;
```

## See Also

### Customizing Rendered Appearance
- [var isLitPerPixel: Bool](./islitperpixel.md)
  A Boolean value that determines whether SceneKit performs lighting calculations per vertex or per pixel. Animatable.
- [var isDoubleSided: Bool](./isdoublesided.md)
  A Boolean value that determines whether SceneKit renders both front and back faces of a surface.
- [var cullMode: SCNCullMode](./cullmode.md)
  The mode determining which faces of a surface SceneKit renders. Animatable.
- [enum SCNCullMode](../scncullmode.md)
  The modes SceneKit uses to determine which polygons to render in a surface, used by the [`cullMode`](./cullmode.md) property.
- [enum SCNFillMode](../scnfillmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/fillmode)*