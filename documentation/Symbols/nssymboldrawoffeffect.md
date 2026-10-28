# NSSymbolDrawOffEffect

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A symbol effect that applies the DrawOff animation to symbol images.

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
@interface NSSymbolDrawOffEffect : NSSymbolEffect
```

## Overview

The DrawOff animation makes the symbol hidden either as a whole, or one motion group at a time, animating parts of the symbol with draw data.

## Topics

### Instance Methods
- [- effectWithByLayer](./nssymboldrawoffeffect/effectwithbylayer.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group.
- [- effectWithIndividually](./nssymboldrawoffeffect/effectwithindividually.md)
  Returns a copy of the effect requesting an animation that applies separately to each motion group, where only one motion group is active at a time.
- [- effectWithNonReversed](./nssymboldrawoffeffect/effectwithnonreversed.md)
  Returns a copy of the effect that only animates forwards. This cancels the reversed variant.
- [- effectWithReversed](./nssymboldrawoffeffect/effectwithreversed.md)
  Returns a copy of the effect that animates in reverse. This cancels the nonReversed variant.
- [- effectWithWholeSymbol](./nssymboldrawoffeffect/effectwithwholesymbol.md)
  Returns a copy of the effect requesting an animation that applies to all motion groups simultaneously.
### Type Methods
- [+ effect](./nssymboldrawoffeffect/effect.md)
  The default draw off effect, determined by the system.

## Relationships

### Inherits From
- [NSSymbolEffect](./nssymboleffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboldrawoffeffect)*