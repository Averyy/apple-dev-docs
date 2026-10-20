# vvtanpi(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the tangent of pi multiplied by each element in an array of double-precision values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvtanpi(_: UnsafeMutablePointer<Double>, _: UnsafePointer<Double>, _: UnsafePointer<Int32>)
```

```c
void vvtanpi(double *, const double *, const int *);
```

##### Parameters

- **parameter 1**: The output array, *y*.
- **parameter 2**: The input array, *x*.
- **parameter 3**: The number of elements in the arrays.

The following code shows an example of using this function:

**Swift**:

```swift
var x: [Double] = [0, 0.25, -0.25]
var y = [Double](repeating: 0, count: x.count)
var n = Int32(x.count)

// Calculate the tangent of π times each element in `x`.
vvtanpi(&y, &x, &n)

// Prints "[0.0, 1.0, -1.0]".
print(y)
```

**Objective-C**:

```objc
double x[3] = {0, 0.25, -0.25};
double y[3];
int n = 3;

// Calculate the tangent of π times each element in `x`.
vvtanpi(y, x, &n);

// Prints "[0, 1, -1]".
printf("[%g, %g, %g]\n", y[0], y[1], y[2]);
```

## See Also

### Array-Oriented Trigonometric Functions
- [static func acos<U>(U) -> [Double]](./vforce/acos%28_%29-8srk.md)
  Returns the arccosine of each element in a vector of double-precision values.
- [static func acos<U>(U) -> [Float]](./vforce/acos%28_%29-3hl5t.md)
  Returns the arccosine of each element in a vector of single-precision values.
- [static func acos<U, V>(U, result: inout V)](./vforce/acos%28_,result%29-3c9qz.md)
  Calculates the arccosine of each element in a vector of double-precision values.
- [static func acos<U, V>(U, result: inout V)](./vforce/acos%28_,result%29-6rc2f.md)
  Calculates the arccosine of each element in a vector of single-precision values.
- [static func asin<U>(U) -> [Double]](./vforce/asin%28_%29-454ds.md)
  Returns the arcsine of each element in a vector of double-precision values.
- [static func asin<U>(U) -> [Float]](./vforce/asin%28_%29-8vvt1.md)
  Returns the arcsine of each element in a vector of single-precision values.
- [static func asin<U, V>(U, result: inout V)](./vforce/asin%28_,result%29-94jmy.md)
  Calculates the arcsine of each element in a vector of double-precision values.
- [static func asin<U, V>(U, result: inout V)](./vforce/asin%28_,result%29-ooti.md)
  Calculates the arcsine of each element in a vector of single-precision values.
- [static func atan<U>(U) -> [Double]](./vforce/atan%28_%29-1ghr3.md)
  Returns the arctangent of each element in a vector of double-precision values.
- [static func atan<U>(U) -> [Float]](./vforce/atan%28_%29-5ejvk.md)
  Returns the arctangent of each element in a vector of single-precision values.
- [static func atan<U, V>(U, result: inout V)](./vforce/atan%28_,result%29-691jp.md)
  Calculates the arctangent of each element in a vector of double-precision values.
- [static func atan<U, V>(U, result: inout V)](./vforce/atan%28_,result%29-6bb8n.md)
  Calculates the arctangent of each element in a vector of single-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Double]](./vforce/atan2%28x,y%29-h54u.md)
  Returns the arctangent of each pair of elements in two vectors of double-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Float]](./vforce/atan2%28x,y%29-3lku3.md)
  Returns the arctangent of each pair of elements in two vectors of single-precision values.
- [static func atan2<T, U, V>(x: T, y: U, result: inout V)](./vforce/atan2%28x,y,result%29-184b6.md)
  Calculates the arctangent of each pair of elements in two vectors of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvtanpi(_:_:_:))*