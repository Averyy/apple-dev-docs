# initWithRank:values:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates an extents object with the rank and values you provide.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (instancetype) initWithRank:(NSUInteger) rank values:(const NSInteger *) values;
```

#### Return Value

A new extents instance, or `nil` if `rank` exceeds 0 and `values` is `nil`, or if `rank` exceeds [`MTL_TENSOR_MAX_RANK`](../mtl_tensor_max_rank.md).

#### Discussion

Zero rank extents represent scalars. `values` can only be `nil` if `rank` is 0.

## Parameters

- `rank`: The number of values in the extents. Pass `0` to create a scalar (rank-zero) extents.
- `values`: A C array of `rank` integer values, or `nil` when `rank` is `0`. The first element corresponds to the innermost dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorextents/initwithrank:values:)*