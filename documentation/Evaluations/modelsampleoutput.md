# ModelSampleOutput

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

The expected output value and evaluation expectations for a sample.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct ModelSampleOutput<Value, Expectation> where Value : Decodable, Value : Encodable, Value : Sendable, Expectation : Decodable, Expectation : Encodable, Expectation : Sendable
```

## Topics

### Initializers
- [init(value: Value?, expectations: Expectation?)](./modelsampleoutput/init%28value,expectations%29.md)
  Creates a model sample output with an optional expected value and expectations.
### Instance Properties
- [var expectations: Expectation?](./modelsampleoutput/expectations.md)
  The expected behavior, for example, tool-call trajectory.
- [var value: Value?](./modelsampleoutput/value.md)
  The expected output value for comparison.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bundled input and output
- [struct ModelSampleInput](./modelsampleinput.md)
  The data a language model receives for evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsampleoutput)*