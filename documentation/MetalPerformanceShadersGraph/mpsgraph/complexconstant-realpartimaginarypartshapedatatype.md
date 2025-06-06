# complexConstant(realPart:imaginaryPart:shape:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a complex constant op with a given shape and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func complexConstant(realPart: Double, imaginaryPart: Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `realPart`: The real part of the complex scalar to fill the entire tensor values with.
- `imaginaryPart`: The imaginary part of the complex scalar to fill the entire tensor values with.
- `shape`: The shape of the output tensor. This has to be statically shaped.
- `dataType`: The dataType of the constant tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/complexconstant(realpart:imaginarypart:shape:datatype:))*