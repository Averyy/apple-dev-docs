# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform the multiply operation `Y = Subfactor * X` for complex double values.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Y: DenseMatrix_Complex_Double)
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .
- `X`: (Input) The right-hand side vectors  . If   is  , then    must have dimension  , where nrhs is the number of right-hand   side vectors.
- `Y`: (Output) The result vectors  . If   is  , and   is   , then   must have dimension  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-7q8gs)*