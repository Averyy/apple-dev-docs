# cumulative

**Framework**: Symbols  
**Kind**: property

An effect that enables each layer of a symbol-based image in sequence.

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
var cumulative: VariableColorSymbolEffect { get }
```

#### Discussion

This effect enables each successive variable layer, and the layer remains enabled until the end of the animation cycle. This effect cancels the [`iterative`](variablecolorsymboleffect/iterative.md) variant.

## See Also

- [var iterative: VariableColorSymbolEffect](variablecolorsymboleffect/iterative.md)
  An effect that momentarily enables each layer of a symbol-based image in sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/variablecolorsymboleffect/cumulative)*