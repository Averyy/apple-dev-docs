# transform(input:)

**Framework**: Accelerate  
**Kind**: method

Returns the result of a double-precision discrete Fourier transform.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func transform<U>(input: U) -> [DSPDoubleComplex] where U : AccelerateBuffer, U.Element == DSPDoubleComplex
```

#### Return Value

An array of [`DSPDoubleComplex`](dspdoublecomplex.md) structures.

## Parameters

- `input`: An array of   structures that contains the input.

## See Also

- [func transform<U>(input: U) -> [DSPComplex]](vdsp/discretefouriertransform/transform(input:)-92b3l.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U, V>(input: U, output: inout V)](vdsp/discretefouriertransform/transform(input:output:)-1k3hd.md)
  Computes a single-precision discrete Fourier transform.
- [func transform<U, V>(input: U, output: inout V)](vdsp/discretefouriertransform/transform(input:output:)-1tsod.md)
  Computes a double-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(input:)-5si4h)*