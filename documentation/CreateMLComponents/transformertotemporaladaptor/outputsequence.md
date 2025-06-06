# TransformerToTemporalAdaptor.OutputSequence

**Framework**: Create ML Components  
**Kind**: typealias

The output sequence type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
typealias OutputSequence = AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>
```

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>](transformertotemporaladaptor/applied(to:eventhandler:).md)
  Performs the transformation on each element of the input sequence.
- [TransformerToTemporalAdaptor.Input](transformertotemporaladaptor/input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](transformertotemporaladaptor/output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor/outputsequence)*