# swapElements(_:_:)

**Framework**: Accelerate  
**Kind**: method

Swaps the elements of two double-precision vectors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func swapElements<T, U>(_ vectorA: inout T, _ vectorB: inout U) where T : AccelerateMutableBuffer, U : AccelerateMutableBuffer, T.Element == Double, U.Element == Double
```

#### Discussion

The following code swaps the elements in `vectorA` with those in `vectorB`:

```swift
var vectorA: [Double] = [1, 3, 5, 7]
var vectorB: [Double] = [2, 4, 6, 8]

vDSP.swapElements(&vectorA,
                  &vectorB)

// Prints "[2.0, 4.0, 6.0, 8.0]".
print(vectorA)

// Prints "[1.0, 3.0, 5.0, 7.0]".
print(vectorB)
```

## Parameters

- `vectorA`: The first vector.
- `vectorB`: The second vector.

## See Also

- [static func swapElements<T, U>(inout T, inout U)](vdsp/swapelements(_:_:)-96xn7.md)
  Swaps the elements of two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/swapelements(_:_:)-62wvt)*