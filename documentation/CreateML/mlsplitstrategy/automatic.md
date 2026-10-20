# MLSplitStrategy.automatic

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Create ML automatically decides how much of your training dataset it uses for a validation dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

#### Discussion

Create ML creates a validation dataset by partitioning up to 10% from the training dataset, depending on its size:

| Training samples | % used for validation |
| --- | --- |
| < 50 | None |
| 50 to 199 | 10% |
| ≥ 200 | 5% |

## See Also

### Partitioning data
- [case fixed(ratio: Double, seed: Int?)](./fixed%28ratio,seed%29.md)
  Create ML uses a portion of your training dataset to create a validation dataset based on the ratio.
- [func resolve(count: Int) -> (ratio: Double, seed: Int)](./resolve%28count%29.md)
  Resolves this split strategy for a specific element count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsplitstrategy/automatic)*