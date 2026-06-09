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
    frame: CGRect(x: 0, y: 0, width: 100, height: 50),
    shape: .rectangle,
    attributedText: AttributedString("Short"),
    autoresizing: [.flexibleWidth]
)

textBox.attributedText = AttributedString("This is much longer text")
// textBox.frame.width is unaffected, but textBox.renderFrame.width has automatically increased
```

## Topics

### Type Properties
- [static let flexibleHeight: MarkupAutoresizing](markupautoresizing/flexibleheight.md)
  Automatically adjust height to fit content changes.
- [static let flexibleWidth: MarkupAutoresizing](markupautoresizing/flexiblewidth.md)
  Automatically adjust width to fit content changes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupautoresizing)*