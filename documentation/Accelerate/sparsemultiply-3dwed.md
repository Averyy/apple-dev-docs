# SparseMultiply(_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform the multiply operation `y = Subfactor * x` for complex floatr values, in place.

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
func SparseMultiply(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ XY: DenseVector_Complex_Float)
```

## Parameters

- `Subfactor`: (Input) The subfactor to multiply by, as returned by   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:)-3dwed)*