# splitSectionLengths

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the lengths of each split section.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * splitSectionLengths;
```

#### Discussion

The layer splits the tensor into chunks along dimensions with sizes given in `splitSectionLengths`.

## See Also

### Inspecting Split Layers
- [var dimension: Int](./dimension.md)
  The dimension or axis along which to split the tensor.
- [var splitCount: Int](./splitcount.md)
  The number of splits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/splitsectionlengths-32abw)*