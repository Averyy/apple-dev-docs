# symbolEffect(_:options:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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

## Parameters

- `effect`: The symbol effect value.
- `options`: A set of options that configure how effects apply to symbol-based images.

## See Also

### Getting content transitions
- [static let identity: ContentTransition](./identity.md)
  The identity content transition, which indicates that content changes shouldn’t animate.
- [static let interpolate: ContentTransition](./interpolate.md)
  A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [static func numericText(countsDown: Bool) -> ContentTransition](./numerictext%28countsdown%29.md)
  Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [static func numericText(value: Double) -> ContentTransition](./numerictext%28value%29.md)
  Creates a content transition intended to be used with `Text` views displaying numbers.
- [static let opacity: ContentTransition](./opacity.md)
  A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var symbolEffect: ContentTransition](./symboleffect.md)
  A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttransition/symboleffect(_:options:))*