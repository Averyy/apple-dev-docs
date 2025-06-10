# addingProduct(_:_:)

**Framework**: Swift  
**Kind**: method

Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func addingProduct(_ lhs: Self, _ rhs: Self) -> Self
```

#### Return Value

The product of `lhs` and `rhs`, added to this value.

#### Discussion

This method is equivalent to the C `fma` function and implements the `fusedMultiplyAdd` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: One of the values to multiply before adding to this value.
- `rhs`: The other value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/addingproduct(_:_:))*