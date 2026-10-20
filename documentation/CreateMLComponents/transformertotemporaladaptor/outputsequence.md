# TransformerToTemporalAdaptor.OutputSequence

**Framework**: Create ML Components  
**Kind**: typealias  
**Role**: Type Alias

The output sequence type.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- iPadOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- Mac Catalyst 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- macOS 13.0+ - Deprecated in 15.0 (renamed: TemporalAdaptor)
- tvOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: TemporalAdaptor)

## Declaration

```swift
typealias OutputSequence = AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>
```

## See Also

### Applying
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>](./applied%28to,eventhandler%29.md)
  Performs the transformation on each element of the input sequence.
- [TransformerToTemporalAdaptor.Input](./input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](./output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor/outputsequence)*