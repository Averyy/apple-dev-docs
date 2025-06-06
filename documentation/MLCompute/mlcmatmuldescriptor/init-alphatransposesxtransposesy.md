# init(alpha:transposesX:transposesY:)

**Framework**: ML Compute  
**Kind**: init

Creates a batched matrix multiplication descriptor with the alpha value and transpose options you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(alpha: Float, transposesX: Bool, transposesY: Bool)
```

## Parameters

- `alpha`: A scalar value you specify to scale the left-hand side,  .
- `transposesX`: A Boolean that specifies whether you choose to transpose the last two dimensions of x.
- `transposesY`: A Boolean that specifies whether you choose to transpose the last two dimensions of y.

## See Also

- [convenience init()](mlcmatmuldescriptor/init.md)
  Creates a batched matrix multiplication descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmuldescriptor/init(alpha:transposesx:transposesy:))*