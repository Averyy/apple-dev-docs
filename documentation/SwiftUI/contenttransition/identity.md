# identity

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The identity content transition, which indicates that content changes shouldn’t animate.

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
static let identity: ContentTransition
```

## Discussion

You can pass this value to a [`contentTransition(_:)`](../view/contenttransition%28_%29.md) modifier to selectively disable animations that would otherwise be applied by a [`withAnimation(_:_:)`](../withanimation%28_,_%29.md) block.

## See Also

### Getting content transitions
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
- [static func symbolEffect<T>(T, options: SymbolEffectOptions) -> ContentTransition](./symboleffect%28_,options%29.md)
  Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttransition/identity)*