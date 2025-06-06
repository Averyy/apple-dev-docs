# init(_:)

**Framework**: Create ML Components  
**Kind**: init

Creates a choose randomly augmentation.

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
init<RandomTransformer>(@AugmentationBuilder<Element> _ augmentation: () -> RandomTransformer) where Element == RandomTransformer.Input, RandomTransformer : RandomTransformer, RandomTransformer.Input == RandomTransformer.Output
```

## Parameters

- `augmentation`: An augmentation builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/chooserandomly/init(_:))*