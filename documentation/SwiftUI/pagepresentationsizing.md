# PagePresentationSizing

**Framework**: SwiftUI  
**Kind**: struct

The size is roughly the size of a page of paper, appropriate for informational or compositional content.

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
struct PagePresentationSizing
```

#### Overview

On iOS, `.page` sizing enforces a platform-defined floor for the vertical and horizontal dimensions. On macOS, no floor is enforced, however a maximum proposed height is derived from the presenter height. To achieve presentations outside of these bounds, see `PresentationSizing.fitted` or implement your own custom [`PresentationSizing`](presentationsizing.md).

> **Note**: [`page`](presentationsizing/page.md)

## Relationships

### Conforms To
- [PresentationSizing](presentationsizing.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AutomaticPresentationSizing](automaticpresentationsizing.md)
  The default presentation sizing, appropriate for the platform.
- [struct FittedPresentationSizing](fittedpresentationsizing.md)
  The size of the presentation is dictated by the ideal size of the content.
- [struct FormPresentationSizing](formpresentationsizing.md)
  The size is appropriate for forms and slightly less wide than`.page`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pagepresentationsizing)*