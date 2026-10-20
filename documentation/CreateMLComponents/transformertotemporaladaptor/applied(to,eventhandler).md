# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs the transformation on each element of the input sequence.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- iPadOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- Mac Catalyst 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- macOS 13.0+ - Deprecated in 15.0 (renamed: TemporalAdaptor)
- tvOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: TemporalAdaptor)

## Declaration

```swift
func applied<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output> where S : TemporalSequence, Base.Input == S.Feature
```

## See Also

### Applying
- [TransformerToTemporalAdaptor.Input](./input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](./output.md)
  The output type.
- [TransformerToTemporalAdaptor.OutputSequence](./outputsequence.md)
  The output sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor/applied(to:eventhandler:))*