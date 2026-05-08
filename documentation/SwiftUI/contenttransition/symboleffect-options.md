# symbolEffect(_:options:)

**Framework**: SwiftUI  
**Kind**: method

Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func symbolEffect<T>(_ effect: T, options: SymbolEffectOptions = .default) -> ContentTransition where T : ContentTransitionSymbolEffect, T : SymbolEffect
```

#### Return Value

A new content transition.

## See Also

- [static let identity: ContentTransition](contenttransition/identity.md)
  The identity content transition, which indicates that content changes shouldn’t animate.
- [static let interpolate: ContentTransition](contenttransition/interpolate.md)
  A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [static func numericText(countsDown: Bool) -> ContentTransition](contenttransition/numerictext(countsdown:).md)
  Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [static func numericText(value: Double) -> ContentTransition](contenttransition/numerictext(value:).md)
  Creates a content transition intended to be used with `Text` views displaying numbers.
- [static let opacity: ContentTransition](contenttransition/opacity.md)
  A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var symbolEffect: ContentTransition](contenttransition/symboleffect.md)
  A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttransition/symboleffect(_:options:))*