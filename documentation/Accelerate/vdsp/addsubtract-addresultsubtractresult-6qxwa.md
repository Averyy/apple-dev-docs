# addSubtract(_:_:addResult:subtractResult:)

**Framework**: Accelerate  
**Kind**: method

Calculates the single-precision element-wise sum and subtraction of two vectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func addSubtract<S, T, U, V>(_ vectorA: S, _ vectorB: T, addResult: inout U, subtractResult: inout V) where S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateMutableBuffer, V : AccelerateMutableBuffer, S.Element == Float, T.Element == Float, U.Element == Float, V.Element == Float
```

#### Discussion

This function calculates the addition and subtraction of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`.

```swift
 for (i = 0; i < N; ++i)
 {
     i1 = I1[i*I1S];
     i0 = I0[i*I0S];
     O0[i*O0S] = i0 + i1;
     O1[i*O1S] = i0 - i1;
 }

```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation, addition and subtraction, with three boxes of each. The bottom row represents the output vectors, O0 and O1, as three boxes of each. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.](https://docs-assets.developer.apple.com/published/f97bb670a3213865fedc136f36c35060/media-4336937%402x.png)

The following code shows an example of using this function:

```swift
    let count = 5
    
    let a: [Float] = [10, 20, 30, 40, 50]
    let b: [Float] = [ 1,  2,  3,  4,  5]
    
    var o0 = [Float](repeating: 0, count: count)
    var o1 = [Float](repeating: 0, count: count)
    
    vDSP.addSubtract(a, b, addResult: &o0, subtractResult: &o1)
    
    // Prints the addition result: "[11.0, 22.0, 33.0, 44.0, 55.0]".
    print(o0)
    
    // Prints the subtraction result: "[9.0, 18.0, 27.0, 36.0, 45.0]".
    print(o1)
```

## Parameters

- `vectorA`: The first input vector,  .
- `vectorB`: The second input vector,  .
- `addResult`: The addition output vector,  .
- `subtractResult`: The subtraction output vector,  .

## See Also

- [static func addSubtract<S, T, U, V>(S, T, addResult: inout U, subtractResult: inout V)](vdsp/addsubtract(_:_:addresult:subtractresult:)-avzd.md)
  Calculates the double-precision element-wise sum and subtraction of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/addsubtract(_:_:addresult:subtractresult:)-6qxwa)*