# transform(input:output:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Computes a double-precision discrete Fourier transform.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func transform<U, V>(input: U, output: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == DSPDoubleComplex, V.Element == DSPDoubleComplex
```

Available when `T` is `DSPDoubleComplex`.

## Parameters

- `input`: An array of [`DSPDoubleComplex`](../../dspdoublecomplex.md) structures that contains the input.
- `output`: An array of [`DSPDoubleComplex`](../../dspdoublecomplex.md) structures that contains the output.

## See Also

### Performing Interleaved Discrete Fourier Transforms
- [func transform<U>(input: U) -> [DSPComplex]](./transform%28input%29-92b3l.md)
  Returns the result of a single-precision discrete Fourier transform.
- [func transform<U>(input: U) -> [DSPDoubleComplex]](./transform%28input%29-5si4h.md)
  Returns the result of a double-precision discrete Fourier transform.
- [func transform<U, V>(input: U, output: inout V)](./transform%28input,output%29-1k3hd.md)
  Computes a single-precision discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/transform(input:output:)-1tsod)*