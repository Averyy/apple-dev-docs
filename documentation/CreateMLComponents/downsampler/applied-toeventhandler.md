# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Down samples the input sequence

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
func applied<S>(to input: S, eventHandler: EventHandler?) throws -> Downsampler<Input>.DownStreamSequence where Input == S.Feature, S : TemporalSequence
```

#### Return Value

An async sequence of down sampled outputs.

## Parameters

- `input`: An async sequence of inputs.
- `eventHandler`: An event handler.

## See Also

- [Downsampler.Input](downsampler/input.md)
  The input type.
- [Downsampler.Output](downsampler/output.md)
  The output type.
- [Downsampler.DownStreamSequence](downsampler/downstreamsequence.md)
  An async sequence of down stream elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/downsampler/applied(to:eventhandler:))*