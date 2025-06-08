# SparseMultiply(_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform the multiply operation `Y = Subfactor * X` in place for complex float values.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ XY: DenseMatrix_Complex_Float)
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .
- `XY`: (Input/Output) On input, the matrix  . On return it is overwritten   with the matrix  . If   is  , then   must have dimension   , where   and   is the number of right-hand   side vectors. If  , then only the first   entries are   used for input or output as approriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:)-34fp6)*