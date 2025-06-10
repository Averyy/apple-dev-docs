# SymbolEffectOptions

**Framework**: Symbols  
**Kind**: struct

Options that configure how effects apply to symbol-based images.

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
struct SymbolEffectOptions
```

## Topics

### Accessing effect options
- [static var `default`: SymbolEffectOptions](symboleffectoptions/default.md)
  The default set of effect options.
### Configuring repeating effects
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
- [static func `repeat`(Int?) -> SymbolEffectOptions](symboleffectoptions/repeat(_:)-33816.md)
  A default set of effect options with a preferred repeat count.
### Configuring effect speed
- [func speed(Double) -> SymbolEffectOptions](symboleffectoptions/speed(_:)-swift.method.md)
  Creates a set of effect options with a preferred speed multiplier.
- [static func speed(Double) -> SymbolEffectOptions](symboleffectoptions/speed(_:)-swift.type.method.md)
  A default set of effect options with a preferred speed multiplier.
### Structures
- [SymbolEffectOptions.RepeatBehavior](symboleffectoptions/repeatbehavior.md)
### Instance Methods
- [func `repeat`(SymbolEffectOptions.RepeatBehavior) -> SymbolEffectOptions](symboleffectoptions/repeat(_:)-316cr.md)
### Type Methods
- [static func `repeat`(SymbolEffectOptions.RepeatBehavior) -> SymbolEffectOptions](symboleffectoptions/repeat(_:)-3klm2.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/symboleffectoptions)*