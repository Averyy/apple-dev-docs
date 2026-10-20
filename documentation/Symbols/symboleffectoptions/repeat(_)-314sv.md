# repeat(_:)

**Framework**: Symbols  
**Kind**: method  
**Role**: Instance Method

Creates a set of effect options with a preferred repeat count.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- iPadOS 17.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- Mac Catalyst 17.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- macOS 14.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- tvOS 17.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))
- watchOS 10.0+ - Deprecated in 27.2 (renamed: SymbolEffectOptions.RepeatBehavior.periodic(_:delay:))

## Declaration

```swift
func `repeat`(_ count: Int?) -> SymbolEffectOptions
```

#### Return Value

A new set of effect options with the preferred repeat count.

## Parameters

- `count`: The preferred number of times to play the effect, or `nil` to request the default number of repeats. The function may clamp very large or small values.

## See Also

### Configuring repeating effects
- [var repeating: SymbolEffectOptions](./repeating-swift.property.md)
  A set of effect options that prefers to repeat indefinitely.
- [static var repeating: SymbolEffectOptions](./repeating-swift.type.property.md)
  A default set of effect options that prefers to repeat indefinitely.
- [var nonRepeating: SymbolEffectOptions](./nonrepeating-swift.property.md)
  A set of effect options that prefers to not repeat.
- [static var nonRepeating: SymbolEffectOptions](./nonrepeating-swift.type.property.md)
  A default set of effect options that prefers to not repeat.
- [static func `repeat`(Int?) -> SymbolEffectOptions](./repeat%28_%29-33816.md)
  A default set of effect options with a preferred repeat count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffectoptions/repeat(_:)-314sv)*