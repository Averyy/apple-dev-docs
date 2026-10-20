# negative(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the negative value of each element in the supplied single-precision vector.

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
static func negative<U>(_ vector: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

```swift
    let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let negativeValues = vDSP.negative(values)
    
    // Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
    print(negativeValues)
```

## Parameters

- `vector`: The source vector.

## See Also

### Vector negation functions
- [static func negative<U>(U) -> [Double]](./negative%28_%29-24oe4.md)
  Returns the negative value of each element in the supplied double-precision vector.
- [static func negative<U, V>(U, result: inout V)](./negative%28_,result%29-92caw.md)
  Calculates the negative value of each element in the supplied single-precision vector.
- [static func negative<U, V>(U, result: inout V)](./negative%28_,result%29-5bwqv.md)
  Calculates the negative value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/negative(_:)-8mo1p)*