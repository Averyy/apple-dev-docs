# interpolate

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let interpolate: ContentTransition
```

#### Discussion

Text views can interpolate transitions when the text views have identical strings. Matching glyph pairs can animate changes to their color, position, size, and any variable properties. Interpolation can apply within a [`Font.Design`](../font/design.md) case, but not between cases, or between entirely different fonts. For example, you can interpolate a change between [`thin`](../font/weight/thin.md) and [`black`](../font/weight/black.md) variations of a font, since these are both cases of [`Font.Weight`](../font/weight.md). However, you can’t interpolate between the default design of a font and its Italic version, because these are different fonts. Any changes that can’t show an interpolated animation use an opacity animation instead.

Symbol images created with the [`init(systemName:)`](../image/init%28systemname%29.md) initializer work the same way as text: changes within the same symbol attempt to interpolate the symbol’s paths. When interpolation is unavailable, the system uses an opacity transition instead.

## See Also

### Getting content transitions
- [static let identity: ContentTransition](./identity.md)
  The identity content transition, which indicates that content changes shouldn’t animate.
- [static func numericText(countsDown: Bool) -> ContentTransition](./numerictext%28countsdown%29.md)
  Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [static func numericText(value: Double) -> ContentTransition](./numerictext%28value%29.md)
  Creates a content transition intended to be used with `Text` views displaying numbers.
- [static let opacity: ContentTransition](./opacity.md)
  A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [static var symbolEffect: ContentTransition](./symboleffect.md)
  A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [static func symbolEffect<T>(T, options: SymbolEffectOptions) -> ContentTransition](./symboleffect%28_,options%29.md)
  Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttransition/interpolate)*