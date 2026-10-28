# transposesY

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A Boolean that specifies whether you choose to transpose the last two dimensions of y.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var transposesY: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL transposesY;
```

## Discussion

The default value is `false`.

## See Also

### Inspecting Matrix Multiplication Descriptors
- [var alpha: Float](./alpha.md)
  A scalar value you specify to scale the result in C = alpha x A x B.
- [var transposesX: Bool](./transposesx.md)
  A Boolean that specifies whether you choose to transpose the last two dimensions of x.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor/transposesy)*