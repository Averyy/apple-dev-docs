# splitCount

**Framework**: ML Compute  
**Kind**: property

The number of splits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var splitCount: Int { get }
```

#### Discussion

The layer splits the tensor into equally sized chunks, however the last chunk may be smaller in size.

## See Also

- [var dimension: Int](mlcsplitlayer/dimension.md)
  The dimension or axis along which to split the tensor.
- [var splitSectionLengths: [Int]?](mlcsplitlayer/splitsectionlengths-5abch.md)
  An array that contains the lengths of each split section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/splitcount)*