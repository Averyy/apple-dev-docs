# iterative

**Framework**: Symbols  
**Kind**: property

An effect that momentarily enables each layer of a symbol-based image in sequence.

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
var iterative: VariableColorSymbolEffect { get }
```

#### Discussion

This effect enables each successive variable layer for a short period of time, and then disables the layer until the animation cycle ends. This effect cancels the [`cumulative`](variablecolorsymboleffect/cumulative.md) variant.

## See Also

- [var cumulative: VariableColorSymbolEffect](variablecolorsymboleffect/cumulative.md)
  An effect that enables each layer of a symbol-based image in sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/variablecolorsymboleffect/iterative)*