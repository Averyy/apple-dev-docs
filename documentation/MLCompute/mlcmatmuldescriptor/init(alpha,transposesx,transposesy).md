# init(alpha:transposesX:transposesY:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a batched matrix multiplication descriptor with the alpha value and transpose options you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(alpha: Float, transposesX: Bool, transposesY: Bool)
```

```objc
+ (instancetype) descriptorWithAlpha:(float) alpha transposesX:(BOOL) transposesX transposesY:(BOOL) transposesY;
```

## Parameters

- `alpha`: A scalar value you specify to scale the left-hand side, `C = alpha x A x B`.
- `transposesX`: A Boolean that specifies whether you choose to transpose the last two dimensions of x.
- `transposesY`: A Boolean that specifies whether you choose to transpose the last two dimensions of y.

## See Also

### Creating Matrix Multiplication Descriptors
- [convenience init()](./init%28%29.md)
  Creates a batched matrix multiplication descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor/init(alpha:transposesx:transposesy:))*