# alignsCorners

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var alignsCorners: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL alignsCorners;
```

## See Also

### Inspecting Upsample Layers
- [var shape: [Int]](./shape-61n1u.md)
  An array that contains the dimensions of the result tensor.
- [var sampleMode: MLCSampleMode](./samplemode.md)
  The upsampling algorithm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/alignscorners)*