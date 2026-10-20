# multiply(subtraction:_:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Calculates the double-precision element-wise product of a vector and the differences of two vectors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func multiply<S, T, U, V>(subtraction: (a: S, b: T), _ vector: U, result: inout V) where S : AccelerateBuffer, T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, S.Element == Double, T.Element == Double, U.Element == Double, V.Element == Double
```

#### Discussion

This function calculates the differences of the first `N` elements of `A` and `B`, multiplies each difference by the corresponding value in `C`, and writes the result to `D`, as follows:

```swift
 for (n = 0; n < N; ++n)
    D[n] = (A[n] - B[n]) * C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that subtracts B from A, as well as the input vector C, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4337013@2x.png)

The following code shows an example of using this function:

```swift
    let count = 5
    
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: [Double] = [10, 20, 30, 40, 50]
    let c: [Double] = [ 5,  4,  3,  2,  1]
    
    let d = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP.multiply(subtraction: (a, b),
                      c,
                      result: &buffer)

        initializedCount = count
    }
    
    // Prints "[-45.0, -72.0, -81.0, -72.0, -45.0]".
    print(d)

```

## Parameters

- `subtraction`: A tuple that contains the vectors `A` and `B` in `D = (A - B) * C`.
- `vector`: The input vector `C` in `D = (A - B) * C`.
- `result`: The output vector `D` in `D = (A - B) * C`.

## See Also

### Multiplication
- [static func multiply<U>(Double, U) -> [Double]](./multiply%28_,_%29-9dxnc.md)
  Returns the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Double]](./multiply%28_,_%29-1ckqt.md)
  Returns the double-precision element-wise product of two vectors.
- [static func multiply<U>(Float, U) -> [Float]](./multiply%28_,_%29-993yp.md)
  Returns the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U>(T, U) -> [Float]](./multiply%28_,_%29-9zgw.md)
  Returns the single-precision element-wise product of two vectors.
- [static func multiply<U, V>(Double, U, result: inout V)](./multiply%28_,_,result%29-4xorc.md)
  Calculates the double-precision element-wise product of a vector and a scalar value.
- [static func multiply<U, V>(Float, U, result: inout V)](./multiply%28_,_,result%29-358cn.md)
  Calculates the single-precision element-wise product of a vector and a scalar value.
- [static func multiply<T, U, V>(T, U, result: inout V)](./multiply%28_,_,result%29-3ptjl.md)
  Calculates the double-precision element-wise product of two vectors.
- [static func multiply<T, U, V>(T, U, result: inout V)](./multiply%28_,_,result%29-155f3.md)
  Calculates the single-precision element-wise product of two vectors.
- [static func multiply(DSPSplitComplex, by: DSPSplitComplex, count: Int, useConjugate: Bool, result: inout DSPSplitComplex)](./multiply%28_,by,count,useconjugate,result%29-4idx8.md)
  Calculates the product of two complex single-precision vectors, optionally conjugating one of them.
- [static func multiply(DSPDoubleSplitComplex, by: DSPDoubleSplitComplex, count: Int, useConjugate: Bool, result: inout DSPDoubleSplitComplex)](./multiply%28_,by,count,useconjugate,result%29-79r8u.md)
  Calculates the element-wise product of two complex double-precision vectors, optionally conjugating one of them.
- [static func multiply<U>(DSPSplitComplex, by: U, result: inout DSPSplitComplex)](./multiply%28_,by,result%29-8b9eq.md)
  Calculates the double-precision element-wise product of a complex vector and a real vector.
- [static func multiply<U>(DSPDoubleSplitComplex, by: U, result: inout DSPDoubleSplitComplex)](./multiply%28_,by,result%29-8jyhd.md)
  Calculates the single-precision element-wise product of a complex vector and a real vector.
- [static func multiply<T, U>(addition: (a: T, b: U), Double) -> [Double]](./multiply%28addition,_%29-4c9in.md)
  Returns the double-precision element-wise product of the sum of two vectors and a scalar value.
- [static func multiply<S, T, U>(addition: (a: S, b: T), U) -> [Double]](./multiply%28addition,_%29-1wt61.md)
  Returns the double-precision element-wise product of a vector and the sum of two vectors.
- [static func multiply<T, U>(addition: (a: T, b: U), Float) -> [Float]](./multiply%28addition,_%29-4fnbx.md)
  Returns the single-precision element-wise product of the sum of two vectors and a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/multiply(subtraction:_:result:)-ziw4)*