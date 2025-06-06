# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on each element of the input sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output> where S : TemporalSequence, Base.Input == S.Feature
```

## See Also

- [TransformerToTemporalAdaptor.Input](transformertotemporaladaptor/input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](transformertotemporaladaptor/output.md)
  The output type.
- [TransformerToTemporalAdaptor.OutputSequence](transformertotemporaladaptor/outputsequence.md)
  The output sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor/applied(to:eventhandler:))*