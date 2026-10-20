# vvrsqrtf(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the reciprocal square root of each element in an array of single-precision values.

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
func vvrsqrtf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

```c
void vvrsqrtf(float *, const float *, const int *);
```

#### Discussion

##### Parameters:

- **parameter 1**: The output array, *y*.
- **parameter 2**: The input array, *x*.
- **parameter 3**: The number of elements in the arrays.

The following code shows an example of using [`vvrsqrtf(_:_:_:)`](./vvrsqrtf%28_,_,_%29.md):

**Swift**:

```swift
var x: [Float] = [100, 10000, 64, 144]
var y = [Float](repeating: 0, count: x.count)
var n = Int32(x.count)
 
vvrsqrtf(&y, &x, &n)
 
print(y) // [0.1, 0.01, 0.125, 0.0833]
```

**Objective-C**:

```objc
float x[] = {100, 10000, 64, 144};
float y[4];
int n = 4;
 
vvrsqrtf(y, x, &n);
 
printf("y: [%lf, %lf, %lf, %lf]\n", y[0], y[1], y[2], y[3]);
```

## See Also

### Array-Oriented Arithmetic and Auxiliary Functions
- [static func ceil<U>(U) -> [Double]](./vforce/ceil%28_%29-9dsdt.md)
  Returns the ceiling of each element in a vector of double-precision values.
- [static func ceil<U>(U) -> [Float]](./vforce/ceil%28_%29-57grr.md)
  Returns the ceiling of each element in a vector of single-precision values.
- [static func ceil<U, V>(U, result: inout V)](./vforce/ceil%28_,result%29-4wev4.md)
  Calculates the ceiling of each element in a vector of double-precision values.
- [static func ceil<U, V>(U, result: inout V)](./vforce/ceil%28_,result%29-6zm3u.md)
  Calculates the ceiling of each element in a vector of single-precision values.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Double]](./vforce/copysign%28magnitudes,signs%29-s0r3.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Float]](./vforce/copysign%28magnitudes,signs%29-3jhf0.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](./vforce/copysign%28magnitudes,signs,result%29-3zoya.md)
  Calculates each double-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](./vforce/copysign%28magnitudes,signs,result%29-5umya.md)
  Calculates each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func floor<U>(U) -> [Double]](./vforce/floor%28_%29-64hyu.md)
  Returns the floor of each element in a vector of double-precision values.
- [static func floor<U>(U) -> [Float]](./vforce/floor%28_%29-5awna.md)
  Returns the floor of each element in a vector of single-precision values.
- [static func floor<U, V>(U, result: inout V)](./vforce/floor%28_,result%29-61veb.md)
  Calculates the floor of each element in a vector of double-precision values.
- [static func floor<U, V>(U, result: inout V)](./vforce/floor%28_,result%29-4mf4q.md)
  Calculates the floor of each element in a vector of single-precision values.
- [static func nearestInteger<U>(U) -> [Double]](./vforce/nearestinteger%28_%29-5mppu.md)
  Returns the nearest integer to each element in a vector of double-precision values.
- [static func nearestInteger<U>(U) -> [Float]](./vforce/nearestinteger%28_%29-386dx.md)
  Returns the nearest integer to each element in a vector of single-precision values.
- [static func nearestInteger<U, V>(U, result: inout V)](./vforce/nearestinteger%28_,result%29-bbtt.md)
  Calculates the nearest integer to each element in a vector of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvrsqrtf(_:_:_:))*