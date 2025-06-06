# UILetterformAwareSizingRule

**Framework**: UIKit  
**Kind**: enum

Constants that specify typographic bounds-sizing behavior to handle text in fonts with oversize characters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum UILetterformAwareSizingRule
```

#### Overview

For more information on typographic bounds sizing behavior, see [`UILetterformAwareAdjusting`](uiletterformawareadjusting.md).

## Topics

### Setting bounds-sizing behavior
- [UILetterformAwareSizingRule.oversize](uiletterformawaresizingrule/oversize.md)
  Bounds-sizing behavior that displays oversize characters fully but may negatively impact typographic alignment.
- [UILetterformAwareSizingRule.typographic](uiletterformawaresizingrule/typographic.md)
  Standard typographic bounds-sizing behavior, which may clip oversize characters.
### Initializers
- [init?(rawValue: Int)](uiletterformawaresizingrule/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiletterformawaresizingrule)*