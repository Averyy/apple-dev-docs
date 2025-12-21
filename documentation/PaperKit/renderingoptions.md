# RenderingOptions

**Framework**: PaperKit  
**Kind**: struct

The rendering options for drawing paper data models.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderingOptions
```

## Topics

### Initializers
- [init(darkUserInterfaceStyle: Bool, layoutRightToLeft: Bool)](renderingoptions/init(darkuserinterfacestyle:layoutrighttoleft:).md)
  Creates a new rendering options value.
- [init(traitCollection: UITraitCollection)](renderingoptions/init(traitcollection:).md)
  Creates the most suitable options for rendering on a device with the specified traits.
### Instance Properties
- [var darkUserInterfaceStyle: Bool](renderingoptions/darkuserinterfacestyle.md)
  Use a dark user interface style for rendering.
- [var rightToLeftLayoutDirection: Bool](renderingoptions/righttoleftlayoutdirection.md)
  Use a right to left layout direction for rendering.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FeatureSet](featureset.md)
  The features supported by PaperKit UI / data models.
- [struct ShapeConfiguration](shapeconfiguration.md)
  A configuration that specifies the appearance of a shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/renderingoptions)*