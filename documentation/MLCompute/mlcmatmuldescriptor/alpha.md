# alpha

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A scalar value you specify to scale the result in C = alpha x A x B.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var alpha: Float { get }
```

```objc
@property (nonatomic, readonly) float alpha;
```

#### Discussion

The default value is `1.0`.

## See Also

### Inspecting Matrix Multiplication Descriptors
- [var transposesX: Bool](./transposesx.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of x.
- [var transposesY: Bool](./transposesy.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of y.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor/alpha)*