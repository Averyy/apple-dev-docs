# dimension

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The dimension or axis along which to split the tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var dimension: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger dimension;
```

## See Also

### Inspecting Split Layers
- [var splitCount: Int](./splitcount.md)
  The number of splits.
- [var splitSectionLengths: [Int]?](./splitsectionlengths-5abch.md)
  An array that contains the lengths of each split section.
- [splitSectionLengths](./splitsectionlengths-32abw.md)
  An array that contains the lengths of each split section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/dimension)*