# MarkupAutoresizing

**Framework**: PaperKit  
**Kind**: struct

Automatic sizing behaviors for this markup.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MarkupAutoresizing
```

#### Overview

Controls whether the markup automatically adjusts its dimensions to fit content changes.

```swift
var textBox = ShapeMarkup(
    shape: .rectangle,
    frame: CGRect(x: 0, y: 0, width: 100, height: 50),
    attributedText: AttributedString("Short"),
    autoresizing: [.flexibleWidth]
)

textBox.attributedText = AttributedString("This is much longer text")
// textBox.frame.width is unaffected, but textBox.renderFrame.width has automatically increased
```

## Topics

### Resizing options
- [static let flexibleHeight: MarkupAutoresizing](markupautoresizing/flexibleheight.md)
  Automatically adjust height to fit content changes.
- [static let flexibleWidth: MarkupAutoresizing](markupautoresizing/flexiblewidth.md)
  Automatically adjust width to fit content changes.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [struct FeatureSet](featureset.md)
  The features PaperKit supports in its UI and data models.
- [struct ShapeConfiguration](shapeconfiguration.md)
  A configuration that specifies the appearance of a shape.
- [struct RenderingOptions](renderingoptions.md)
  The rendering options for drawing paper data models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupautoresizing)*