# vvexpf(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates *e* raised to the power of each element in an array of single-precision values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvexpf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

```c
void vvexpf(float *, const float *, const int *);
```

### Parameters:

- **parameter 1**: The output array, *y*.
- **parameter 2**: The input array, *x*.
- **parameter 3**: The number of elements in the arrays.

The following code shows an example of using this function:

**Swift**:

```swift
var x: [Float] = [0, 1, 2]
var y = [Float](repeating: 0, count: x.count)
var n = Int32(x.count)

// Calculate `e` raised to the power of each element in `x`.
vvexpf(&y, &x, &n)

// Prints "[1.0, 2.7182817, 7.389056]".
print(y)
```

**Objective-C**:

```objc
float x[3] = {0, 1, 2};
float y[3];
int n = 3;

// Calculate `e` raised to the power of each element in `x`.
vvexpf(y, x, &n);

// Prints "[1, 2.71828, 7.38906]".
printf("[%g, %g, %g]\n", y[0], y[1], y[2]);
```

## See Also

### Array-Oriented Exponential and Logarithmic Functions
- [static func exp<U>(U) -> [Double]](./vforce/exp%28_%29-76nrd.md)
  Returns the *e*, raised to the power of each element in a vector of double-precision values.
- [static func exp<U>(U) -> [Float]](./vforce/exp%28_%29-5iaun.md)
  Returns the *e*, raised to the power of each element in a vector of single-precision values.
- [static func exp<U, V>(U, result: inout V)](./vforce/exp%28_,result%29-34nxw.md)
  Calculates the *e*, raised to the power of each element in a vector of double-precision values.
- [static func exp<U, V>(U, result: inout V)](./vforce/exp%28_,result%29-4k85n.md)
  Calculates the *e*, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U>(U) -> [Double]](./vforce/exp2%28_%29-2m5q.md)
  Returns the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U>(U) -> [Float]](./vforce/exp2%28_%29-4mm9y.md)
  Returns the 2, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U, V>(U, result: inout V)](./vforce/exp2%28_,result%29-6ru6m.md)
  Calculates the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U, V>(U, result: inout V)](./vforce/exp2%28_,result%29-8m564.md)
  Calculates the 2, raised to the power of each element in a vector of single-precision values.
- [static func expm1<U>(U) -> [Double]](./vforce/expm1%28_%29-xkzx.md)
  Returns the *eˣ-1* for each element in a vector of double-precision values.
- [static func expm1<U>(U) -> [Float]](./vforce/expm1%28_%29-mfq5.md)
  Returns the *eˣ-1* for each element in a vector of single-precision values.
- [static func expm1<U, V>(U, result: inout V)](./vforce/expm1%28_,result%29-4dpl4.md)
  Calculates the *eˣ-1* for each element in a vector of double-precision values.
- [static func expm1<U, V>(U, result: inout V)](./vforce/expm1%28_,result%29-2yhs3.md)
  Calculates the *eˣ-1* for each element in a vector of single-precision values.
- [static func log10<U>(U) -> [Double]](./vforce/log10%28_%29-9wr68.md)
  Returns the base 10 logarithm of each element in a vector of double-precision values.
- [static func log<U>(U) -> [Double]](./vforce/log%28_%29-2gh9a.md)
  Returns the natural logarithm for each element in a vector of double-precision values.
- [static func log<U>(U) -> [Float]](./vforce/log%28_%29-5ffby.md)
  Returns the natural logarithm for each element in a vector of single-precision values.
- [vvexp](./vvexp%28_,_,_%29.md)
  Calculates *e* raised to the power of each element in an array of double-precision values.
- [vvexp2](./vvexp2%28_,_,_%29.md)
  Calculates 2 raised to the power of each element in an array of double-precision values.
- [vvexp2f](./vvexp2f%28_,_,_%29.md)
  Calculates 2 raised to the power of each element in an array of single-precision values.
- [vvexpm1](./vvexpm1%28_,_,_%29.md)
  Calculates *eˣ-1* for each element in an array of double-precision values.
- [vvexpm1f](./vvexpm1f%28_,_,_%29.md)
  Calculates *eˣ-1* for each element in an array of single-precision values.
- [vvlog](./vvlog%28_,_,_%29.md)
  Calculates the natural logarithm for each element in an array of double-precision values.
- [vvlogf](./vvlogf%28_,_,_%29.md)
  Calculates the natural logarithm for each element in an array of single-precision values.
- [vvlog1p](./vvlog1p%28_,_,_%29.md)
  Calculates *log(1+x)* for each element in an array of double-precision values.
- [vvlog1pf](./vvlog1pf%28_,_,_%29.md)
  Calculates *log(1+x)* for each element in an array of single-precision values.
- [vvlog2](./vvlog2%28_,_,_%29.md)
  Calculates the base 2 logarithm of each element in an array of double-precision values.
- [vvlog2f](./vvlog2f%28_,_,_%29.md)
  Calculates the base 2 logarithm of each element in an array of single-precision values.
- [vvlog10](./vvlog10%28_,_,_%29.md)
  Calculates the base 10 logarithm of each element in an array of double-precision values.
- [vvlog10f](./vvlog10f%28_,_,_%29.md)
  Calculates the base 10 logarithm of each element in an array of single-precision values.
- [vvlogb](./vvlogb%28_,_,_%29.md)
  Calculates the unbiased exponent of each element in an array of double-precision values.
- [vvlogbf](./vvlogbf%28_,_,_%29.md)
  Calculates the unbiased exponent of each element in an array of single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvexpf(_:_:_:))*