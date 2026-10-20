# vvatanhf(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the inverse hyperbolic tangent of each element in an array of single-precision values.

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
func vvatanhf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

```c
void vvatanhf(float *, const float *, const int *);
```

#### Discussion

##### Parameters:

- **parameter 1**: The output array, *y*.
- **parameter 2**: The input array, *x*.
- **parameter 3**: The number of elements in the arrays.

If `x` is `+/-0`, the result preserves the signed zero.

If `x` is `+/-1`, the result is `+/-inf`.

If `|x|>1`, the result is `NaN`.

The following code shows an example of using this function:

**Swift**:

```swift
var x: [Float] = [-0.5, 0, 0.5]
var y = [Float](repeating: 0, count: x.count)
var n = Int32(x.count)

// Calculate the inverse hyperbolic tangent of each element in `x`.
vvatanhf(&y, &x, &n)

// Prints "[-0.54930615, 0.0, 0.54930615]".
print(y)
```

**Objective-C**:

```objc
float x[3] = {-0.5, 0, 0.5};
float y[3];
int n = 3;

// Calculate the inverse hyperbolic tangent of each element in `x`.
vvatanhf(y, x, &n);

// Prints "[-0.549306, 0, 0.549306]".
printf("[%g, %g, %g]\n", y[0], y[1], y[2]);
```

## See Also

### Array-Oriented Hyperbolic Functions
- [static func acosh<U>(U) -> [Double]](./vforce/acosh%28_%29-1j3qt.md)
  Returns the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U>(U) -> [Float]](./vforce/acosh%28_%29-8zjay.md)
  Returns the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func acosh<U, V>(U, result: inout V)](./vforce/acosh%28_,result%29-4cip0.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U, V>(U, result: inout V)](./vforce/acosh%28_,result%29-2r23w.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func asinh<U>(U) -> [Double]](./vforce/asinh%28_%29-ue6b.md)
  Returns the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U>(U) -> [Float]](./vforce/asinh%28_%29-284n7.md)
  Returns the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func asinh<U, V>(U, result: inout V)](./vforce/asinh%28_,result%29-7wn57.md)
  Calculates the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U, V>(U, result: inout V)](./vforce/asinh%28_,result%29-17vv4.md)
  Calculates the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func atanh<U>(U) -> [Double]](./vforce/atanh%28_%29-922d.md)
  Returns the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U>(U) -> [Float]](./vforce/atanh%28_%29-2t372.md)
  Returns the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func atanh<U, V>(U, result: inout V)](./vforce/atanh%28_,result%29-6waj3.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U, V>(U, result: inout V)](./vforce/atanh%28_,result%29-596wg.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func cosh<U>(U) -> [Double]](./vforce/cosh%28_%29-4dmhm.md)
  Returns the hyperbolic cosine of each element in a vector of double-precision values.
- [static func cosh<U>(U) -> [Float]](./vforce/cosh%28_%29-5ax3f.md)
  Returns the hyperbolic cosine of each element in a vector of single-precision values.
- [static func cosh<U, V>(U, result: inout V)](./vforce/cosh%28_,result%29-4f7in.md)
  Calculates the hyperbolic cosine of each element in a vector of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvatanhf(_:_:_:))*