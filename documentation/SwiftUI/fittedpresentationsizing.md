# FittedPresentationSizing

**Framework**: SwiftUI  
**Kind**: struct

The size of the presentation is dictated by the ideal size of the content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct FittedPresentationSizing
```

#### Overview

The presentation is sized by proposing `nil` in the horizontal and vertical dimensions.

> **Note**: [`fitted`](presentationsizing/fitted.md)

[`fitted`](presentationsizing/fitted.md)

## Relationships

### Conforms To
- [PresentationSizing](presentationsizing.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AutomaticPresentationSizing](automaticpresentationsizing.md)
  The default presentation sizing, appropriate for the platform.
- [struct FormPresentationSizing](formpresentationsizing.md)
  The size is appropriate for forms and slightly less wide than`.page`
- [struct PagePresentationSizing](pagepresentationsizing.md)
  The size is roughly the size of a page of paper, appropriate for informational or compositional content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fittedpresentationsizing)*