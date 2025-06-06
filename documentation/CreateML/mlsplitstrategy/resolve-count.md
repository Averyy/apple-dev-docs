# resolve(count:)

**Framework**: Create ML  
**Kind**: method

Resolves this split strategy for a specific element count.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func resolve(count: Int) -> (ratio: Double, seed: Int)
```

#### Return Value

The split fraction and the random seed to use.

## Parameters

- `count`: The number of elements in the collection being split.

## See Also

- [MLSplitStrategy.automatic](mlsplitstrategy/automatic.md)
  Create ML automatically decides how much of your training dataset it uses for a validation dataset.
- [case fixed(ratio: Double, seed: Int?)](mlsplitstrategy/fixed(ratio:seed:).md)
  Create ML uses a portion of your training dataset to create a validation dataset based on the ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsplitstrategy/resolve(count:))*