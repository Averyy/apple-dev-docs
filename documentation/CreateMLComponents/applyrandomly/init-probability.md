# init(probability:_:)

**Framework**: Create ML Components  
**Kind**: init

Creates an apply randomly augmentation.

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
init<Input>(probability: Double = 0.5, @AugmentationBuilder<Input> _ augmentation: () -> RandomTransformer) where Input == RandomTransformer.Input
```

## Parameters

- `probability`: The probability of applying the transformation. Must be greater than or equal to 0 and less   than or equal to 1, the default value is 0.5.
- `augmentation`: The transformer to apply randomly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/applyrandomly/init(probability:_:))*