# splitCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of splits.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var splitCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger splitCount;
```

#### Discussion

The layer splits the tensor into equally sized chunks, however the last chunk may be smaller in size.

## See Also

### Inspecting Split Layers
- [var dimension: Int](./dimension.md)
  The dimension or axis along which to split the tensor.
- [var splitSectionLengths: [Int]?](./splitsectionlengths-5abch.md)
  An array that contains the lengths of each split section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/splitcount)*