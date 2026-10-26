# vvnextafter(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the next machine-representable value for each element in an array of double-precision values.

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
func vvnextafter(_: UnsafeMutablePointer<Double>, _: UnsafePointer<Double>, _: UnsafePointer<Double>, _: UnsafePointer<Int32>)
```

```c
void vvnextafter(double *, const double *, const double *, const int *);
```

#### Discussion

##### Parameters:

- **parameter 1**: The output array, *z*.
- **parameter 2**: The input array, *y*.
- **parameter 3**: The direction array, *x*.
- **parameter 4**: The number of elements in the arrays.

Not all values can be represented as a floating-point value of a given precision. This function sets a value in `z[i]` that is either minimally larger than the value in `y[i]` (if `x[i]` is larger than `y[i]`) or minimally smaller than the value in `y[i]` (if `x[i]` is smaller than `y[i]`).

The following code shows an example of using this function:

**Swift**:

```swift
var from: [Double] = [1, 2, 3]
var to: [Double] = [2, 2, 2]
var y = [Double](repeating: 0, count: from.count)
var n = Int32(from.count)

// Calculate the next representable value after each element in `from` toward the corresponding element in `to`.
vvnextafter(&y, &from, &to, &n)

// Prints "[1.0000000000000002, 2.0, 2.9999999999999996]".
print(y)
```

**Objective-C**:

```objc
double from[3] = {1, 2, 3};
double to[3] = {2, 2, 2};
double y[3];
int n = 3;

// Calculate the next representable value after each element in `from` toward the corresponding element in `to`.
vvnextafter(y, from, to, &n);

// Prints "[1, 2, 3]".
printf("[%g, %g, %g]\n", y[0], y[1], y[2]);
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
- [vvceil](./vvceil%28_,_,_%29.md)
  Calculates the ceiling of each element in an array of double-precision values.
- [vvceilf](./vvceilf%28_,_,_%29.md)
  Calculates the ceiling of each element in an array of single-precision values.
- [vvfloor](./vvfloor%28_,_,_%29.md)
  Calculates the floor of each element in an array of double-precision values.
- [vvfloorf](./vvfloorf%28_,_,_%29.md)
  Calculates the floor of each element in an array of single-precision values.
- [vvcopysign](./vvcopysign%28_,_,_,_%29.md)
  Copies an array, setting the sign of each element based on a second array of double-precision values.
- [vvcopysignf](./vvcopysignf%28_,_,_,_%29.md)
  Copies an array, setting the sign of each element based on a second array of single-precision values.
- [vvdiv](./vvdiv%28_,_,_,_%29.md)
  Divides each element in an array by the corresponding value in a second array of double-precision values.
- [vvdivf](./vvdivf%28_,_,_,_%29.md)
  Divides each element in an array by the corresponding value in a second array of single-precision values.
- [vvfabs](./vvfabs%28_,_,_%29.md)
  Calculates the absolute value for each element in an array of double-precision values.
- [vvfabsf](./vvfabsf%28_,_,_%29.md)
  Calculates the absolute value for each element in an array of single-precision values.
- [vvfmod](./vvfmod%28_,_,_,_%29.md)
  Calculates the modulus after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [vvfmodf](./vvfmodf%28_,_,_,_%29.md)
  Calculates the modulus after dividing each element in an array by the corresponding element in a second array of single-precision values.
- [vvremainder](./vvremainder%28_,_,_,_%29.md)
  Calculates the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [vvremainderf](./vvremainderf%28_,_,_,_%29.md)
  Calculates the remainder after dividing each element in an array by the corresponding element in a second array of single-precision values.
- [vvint](./vvint%28_,_,_%29.md)
  Calculates the integer truncation for each element in an array of double-precision values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvnextafter(_:_:_:_:))*