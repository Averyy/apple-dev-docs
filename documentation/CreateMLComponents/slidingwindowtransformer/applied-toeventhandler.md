# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Extracts a window sequence from the input sequence

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func applied<S>(to input: S, eventHandler: EventHandler?) throws -> SlidingWindowTransformer<Input>.WindowSequence where Input == S.Feature, S : TemporalSequence
```

#### Return Value

An async sequence of windowed outputs.

## Parameters

- `input`: An async sequence of inputs.
- `eventHandler`: An event handler.

## See Also

- [SlidingWindowTransformer.Input](slidingwindowtransformer/input.md)
  The input type.
- [SlidingWindowTransformer.Output](slidingwindowtransformer/output.md)
  The output type.
- [SlidingWindowTransformer.WindowSequence](slidingwindowtransformer/windowsequence.md)
  An async sequence of windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer/applied(to:eventhandler:))*