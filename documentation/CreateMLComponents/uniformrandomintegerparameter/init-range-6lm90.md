# init(range:_:)

**Framework**: Create ML Components  
**Kind**: init

Creates a Random Parameter transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init<Input>(range: Range<Parameter>, @AugmentationBuilder<Input> _ augmentation: @escaping (Parameter) -> RandomTransformer) where Input == RandomTransformer.Input
```

## Parameters

- `range`: The range of a random number to use as input to the transformer.
- `augmentation`: An augmentation builder.

## See Also

- [init<Input>(range: ClosedRange<Parameter>, (Parameter) -> RandomTransformer)](uniformrandomintegerparameter/init(range:_:)-23ddz.md)
  Creates a Random Parameter transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/uniformrandomintegerparameter/init(range:_:)-6lm90)*