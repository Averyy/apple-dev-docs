# BNNSDataLayout6DFirstMajor

**Framework**: Accelerate  
**Kind**: var

A constant that represents a 6D first-major tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSDataLayout6DFirstMajor: BNNSDataLayout { get }
```

#### Discussion

The value `(i, j, k, l, m, n)` is at index:

`n * stride[0] + m * stride[1] + l * stride[2] + k * stride[3] +`

`j * stride[4] + i * stride[5]`.

- `size[0]` is the size of the first dimension (`i`).
- `size[1]` is the size of the second dimension (`j`).
- `size[2]` is the size of the third dimension (`k`).
- `size[3]` is the size of the fourth dimension (`l`).
- `size[4]` is the size of the fifth dimension (`m`).
- `size[5]` is the size of the sixth dimension (`n`).

## See Also

- [var BNNSDataLayout6DLastMajor: BNNSDataLayout](bnnsdatalayout6dlastmajor.md)
  A constant that represents a 6D last-major tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdatalayout6dfirstmajor)*