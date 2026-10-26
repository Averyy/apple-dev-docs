# replaceOffUpTransition

**Framework**: Symbols  
**Kind**: method  
**Role**: Type Method

An effect that replaces a symbol by removing it, and scaling a different symbol up.

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
+ (instancetype) replaceOffUpTransition;
```

#### Return Value

A new instance of the transition that uses the Off-Up animation.

#### Discussion

The initial symbol is removed with no animation, and the new symbol scales up as it’s added.

## See Also

### Accessing symbol effects
- [+ transition](./transition.md)
  An effect that replaces the layers of one symbol-based image with those of another.
- [+ replaceDownUpTransition](./replacedownuptransition.md)
  An effect that replaces a symbol by scaling it down, and scaling a different symbol up.
- [+ replaceUpUpTransition](./replaceupuptransition.md)
  An effect that replaces a symbol by scaling it up, and scaling a different symbol up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolreplacecontenttransition/replaceoffuptransition)*