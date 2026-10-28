# NSSymbolReplaceContentTransition

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

A type that replaces the layers of one symbol-based image with those of another.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface NSSymbolReplaceContentTransition : NSSymbolContentTransition
```

## Overview

A replace transition animates the change from one symbol image to another. You choose from one of the predefined scaling animations: Down-Up, Off-Up, and Up-Up.

- **Down-Up**: The initial symbol scales down as it’s removed, and the new symbol scales up as it’s added.
- **Off-Up**: The initial symbol is removed with no animation, and the new symbol scales up as it’s added.
- **Up-Up**: The initial symbol scales up as it’s removed, and the new symbol scales up as it’s added.

## Topics

### Accessing symbol effects
- [+ transition](./nssymbolreplacecontenttransition/transition.md)
  An effect that replaces the layers of one symbol-based image with those of another.
- [+ replaceDownUpTransition](./nssymbolreplacecontenttransition/replacedownuptransition.md)
  An effect that replaces a symbol by scaling it down, and scaling a different symbol up.
- [+ replaceOffUpTransition](./nssymbolreplacecontenttransition/replaceoffuptransition.md)
  An effect that replaces a symbol by removing it, and scaling a different symbol up.
- [+ replaceUpUpTransition](./nssymbolreplacecontenttransition/replaceupuptransition.md)
  An effect that replaces a symbol by scaling it up, and scaling a different symbol up.
### Determining effect scope
- [- transitionWithByLayer](./nssymbolreplacecontenttransition/transitionwithbylayer.md)
  An effect that replaces each layer separately.
- [- transitionWithWholeSymbol](./nssymbolreplacecontenttransition/transitionwithwholesymbol.md)
  An effect that replaces all layers simultaneously.
### Type Methods
- [+ magicTransitionWithFallback:](./nssymbolreplacecontenttransition/magictransitionwithfallback_.md)
  Convenience initializer for a MagicReplace content transition with a configured Replace fallback.

## Relationships

### Inherits From
- [NSSymbolContentTransition](./nssymbolcontenttransition.md)

## See Also

### Symbol content transitions
- [NSSymbolAutomaticContentTransition](./nssymbolautomaticcontenttransition.md)
  A type that applies the default animation to a symbol-based image in a context-sensitive manner.
- [NSSymbolMagicReplaceContentTransition](./nssymbolmagicreplacecontenttransition.md)
  A symbol effect applies the MagicReplace animation to symbol images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolreplacecontenttransition)*