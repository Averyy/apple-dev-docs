# RenderingOptions

**Framework**: PaperKit  
**Kind**: struct

The rendering options for drawing paper data models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderingOptions
```

## Topics

### Creating rendering options
- [init(darkUserInterfaceStyle: Bool, layoutRightToLeft: Bool)](renderingoptions/init(darkuserinterfacestyle:layoutrighttoleft:).md)
  Creates a new rendering options value.
- [init(traitCollection: UITraitCollection)](renderingoptions/init(traitcollection:).md)
  Creates the most suitable options for rendering on a device with the specified traits.
### Configuring style
- [var darkUserInterfaceStyle: Bool](renderingoptions/darkuserinterfacestyle.md)
  Use a dark user interface style for rendering.
- [var rightToLeftLayoutDirection: Bool](renderingoptions/righttoleftlayoutdirection.md)
  Use a right to left layout direction for rendering.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct FeatureSet](featureset.md)
  The features PaperKit supports in its UI and data models.
- [struct ShapeConfiguration](shapeconfiguration.md)
  A configuration that specifies the appearance of a shape.
- [struct MarkupAutoresizing](markupautoresizing.md)
  Automatic sizing behaviors for this markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/renderingoptions)*