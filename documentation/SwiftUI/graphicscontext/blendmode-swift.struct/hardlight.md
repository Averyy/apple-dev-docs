# hardLight

**Framework**: SwiftUI  
**Kind**: property

A mode that either multiplies or screens colors, depending on the source image sample color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var hardLight: GraphicsContext.BlendMode { get }
```

#### Discussion

If the source image sample color is lighter than 50% gray, the background is lightened, similar to screening. If the source image sample color is darker than 50% gray, the background is darkened, similar to multiplying. If the source image sample color is equal to 50% gray, the source image is not changed. Image samples that are equal to pure black or pure white result in pure black or white. The overall effect is similar to what you’d achieve by shining a harsh spotlight on the source image. Use this to add highlights to a scene.

## See Also

- [static var overlay: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/overlay.md)
  A mode that either multiplies or screens the source image samples with the background image samples, depending on the background color.
- [static var softLight: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct/softlight.md)
  A mode that either darkens or lightens colors, depending on the source image sample color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.struct/hardlight)*