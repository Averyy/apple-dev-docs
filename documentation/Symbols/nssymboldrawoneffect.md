# NSSymbolDrawOnEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A symbol effect that applies the DrawOn animation to symbol images.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```objc
@interface NSSymbolDrawOnEffect : NSSymbolEffect
```

#### Overview

The DrawOn animation makes the symbol visible either as a whole, or one motion group at a time, animating parts of the symbol with draw data.

## Topics

### Instance Methods
- [- effectWithByLayer](./nssymboldrawoneffect/effectwithbylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [- effectWithIndividually](./nssymboldrawoneffect/effectwithindividually.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group, where only one motion group is active at a time.
- [- effectWithWholeSymbol](./nssymboldrawoneffect/effectwithwholesymbol.md)
  Returns a copy of the effect requesting an animation that applies to all motion groups simultaneously.
### Type Methods
- [+ effect](./nssymboldrawoneffect/effect.md)
  The default draw on effect, determined by the system.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboldrawoneffect)*