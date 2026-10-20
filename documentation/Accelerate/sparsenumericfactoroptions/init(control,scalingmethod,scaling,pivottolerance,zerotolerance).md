# init(control:scalingMethod:scaling:pivotTolerance:zeroTolerance:)

**Framework**: Accelerate  
**Kind**: init

Returns a new numeric factor options structure with the specified properties.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(control: SparseControl_t, scalingMethod: SparseScaling_t, scaling: UnsafeMutableRawPointer?, pivotTolerance: Double, zeroTolerance: Double)
```

#### Discussion

> **Note**:  Only the symmetric factorization algorithms use the [`pivotTolerance`](sparsenumericfactoroptions/pivottolerance.md) and [`zeroTolerance`](sparsenumericfactoroptions/zerotolerance.md) parameters. [`SparseFactorizationQR`](sparsefactorizationqr.md) ignores the pivot and zero tolerance values.

## Parameters

- `control`: The flags that control the computation.
- `scalingMethod`: The scaling method.
- `scaling`: An array that scales the matrix before factorization.
- `pivotTolerance`: The pivot tolerance that threshold partial pivoting uses.
- `zeroTolerance`: The zero tolerance that some pivoting modes use.

## See Also

- [init()](sparsenumericfactoroptions/init.md)
  Returns a new numeric factor options structure with default properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsenumericfactoroptions/init(control:scalingmethod:scaling:pivottolerance:zerotolerance:))*