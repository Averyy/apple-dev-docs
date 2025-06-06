# repeat(_:)

**Framework**: Symbols  
**Kind**: method

A default set of effect options with a preferred repeat count.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func `repeat`(_ count: Int?) -> SymbolEffectOptions
```

#### Return Value

A new set of effect options with the preferred repeat count.

## Parameters

- `count`: The preferred number of times to play the effect, or   to request the default number of times. The function may clamp very large or small values.

## See Also

- [var repeating: SymbolEffectOptions](symboleffectoptions/repeating-swift.property.md)
  A set of effect options that prefers to repeat indefinitely.
- [static var repeating: SymbolEffectOptions](symboleffectoptions/repeating-swift.type.property.md)
  A default set of effect options that prefers to repeat indefinitely.
- [var nonRepeating: SymbolEffectOptions](symboleffectoptions/nonrepeating-swift.property.md)
  A set of effect options that prefers to not repeat.
- [static var nonRepeating: SymbolEffectOptions](symboleffectoptions/nonrepeating-swift.type.property.md)
  A default set of effect options that prefers to not repeat.
- [func `repeat`(Int?) -> SymbolEffectOptions](symboleffectoptions/repeat(_:)-314sv.md)
  Creates a set of effect options with a preferred repeat count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeat(_:)-33816)*