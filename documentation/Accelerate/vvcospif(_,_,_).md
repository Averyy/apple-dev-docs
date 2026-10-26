# vvcospif(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the cosine of pi multiplied by each element in an array of single-precision values.

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
func vvcospif(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

```c
void vvcospif(float *, const float *, const int *);
```

#### Discussion

##### Parameters:

- **parameter 1**: The output array, *y*.
- **parameter 2**: The input array, *x*.
- **parameter 3**: The number of elements in the arrays.

The following code shows an example of using [`vvcospif(_:_:_:)`](./vvcospif%28_,_,_%29.md):

**Swift**:

```swift
var x: [Float] = [-0.5, 0, 0.5]
var y = [Float](repeating: 0, count: x.count)
var n = Int32(x.count)
 
vvcospif(&y, &x, &n)
 
print(y) // [0.0, 1.0, 0.0]
```

**Objective-C**:

```objc
float x[] = {-0.5, 0, 0.5};
float y[3];
int n = 3;
 
vvcospif(y, x, &n);
 
printf("y: [%f, %f, %f]\n", y[0], y[1], y[2]);
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
- [vvsin](./vvsin%28_,_,_%29.md)
  Calculates the sine of each element in an array of double-precision values.
- [vvsinf](./vvsinf%28_,_,_%29.md)
  Calculates the sine of each element in an array of single-precision values.
- [vvsinpi](./vvsinpi%28_,_,_%29.md)
  Calculates the sine of pi multiplied by each element in an array of double-precision values.
- [vvsinpif](./vvsinpif%28_,_,_%29.md)
  Calculates the sine of pi multiplied by each element in an array of single-precision values.
- [vvcos](./vvcos%28_,_,_%29.md)
  Calculates the cosine of each element in an array of double-precision values.
- [vvcosf](./vvcosf%28_,_,_%29.md)
  Calculates the cosine of each element in an array of single-precision values.
- [vvcospi](./vvcospi%28_,_,_%29.md)
  Calculates the cosine of pi multiplied by each element in an array of double-precision values.
- [vvcosisin](./vvcosisin%28_,_,_%29.md)
  Calculates the cosine and sine of each element in an array of double-precision values.
- [vvcosisinf](./vvcosisinf%28_,_,_%29.md)
  Calculates the cosine and sine of each element in an array of single-precision values.
- [vvsincos](./vvsincos%28_,_,_,_%29.md)
  Calculates the cosine and sine of each element in an array of double-precision values.
- [vvsincosf](./vvsincosf%28_,_,_,_%29.md)
  Calculates the cosine and sine of each element in an array of single-precision values.
- [vvtan](./vvtan%28_,_,_%29.md)
  Calculates the tangent of each element in an array of double-precision values.
- [vvtanf](./vvtanf%28_,_,_%29.md)
  Calculates the tangent of each element in an array of single-precision values.
- [vvtanpi](./vvtanpi%28_,_,_%29.md)
  Calculates the tangent of pi multiplied by each element in an array of double-precision values.
- [vvtanpif](./vvtanpif%28_,_,_%29.md)
  Calculates the tangent of pi multiplied by each element in an array of single-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvcospif(_:_:_:))*