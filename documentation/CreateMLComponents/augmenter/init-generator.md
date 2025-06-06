# init(generator:_:)

**Framework**: Create ML Components  
**Kind**: init

Creates an augmenter from a random number generator and an augmentation builder.

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
init<Input>(generator: RandomNumberGenerator = SystemRandomNumberGenerator(), @AugmentationBuilder<Input> _ builder: @escaping () -> RandomTransformer) where Input == RandomTransformer.Input
```

## Parameters

- `generator`: A random number generator.
- `builder`: An augmentation builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmenter/init(generator:_:))*