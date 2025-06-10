# MLSplitStrategy

**Framework**: Create ML  
**Kind**: enum

Data partitioning approaches, typically for creating a validation dataset from a training dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MLSplitStrategy
```

## Topics

### Partitioning data
- [MLSplitStrategy.automatic](mlsplitstrategy/automatic.md)
  Create ML automatically decides how much of your training dataset it uses for a validation dataset.
- [case fixed(ratio: Double, seed: Int?)](mlsplitstrategy/fixed(ratio:seed:).md)
  Create ML uses a portion of your training dataset to create a validation dataset based on the ratio.
- [func resolve(count: Int) -> (ratio: Double, seed: Int)](mlsplitstrategy/resolve(count:).md)
  Resolves this split strategy for a specific element count.
### Creating a random seed
- [func timestampSeed() -> Int](timestampseed().md)
  Returns a number based on the current system time.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MLCreateError](mlcreateerror.md)
  The errors Create ML throws while performing various operations, such as training models, making predictions, writing models to a file system, and so on.
- [struct MLModelMetadata](mlmodelmetadata.md)
  Information about a model that’s stored in a Core ML model file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsplitstrategy)*