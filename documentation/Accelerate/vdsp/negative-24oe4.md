# negative(_:)

**Framework**: Accelerate  
**Kind**: method

Returns the negative value of each element in the supplied double-precision vector.

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
static func negative<U>(_ vector: U) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

```swift
    let values: [Double] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let negativeValues = vDSP.negative(values)
    
    // Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
    print(negativeValues)
```

## Parameters

- `vector`: The source vector.

## See Also

- [static func negative<U>(U) -> [Float]](vdsp/negative(_:)-8mo1p.md)
  Returns the negative value of each element in the supplied single-precision vector.
- [static func negative<U, V>(U, result: inout V)](vdsp/negative(_:result:)-92caw.md)
  Calculates the negative value of each element in the supplied single-precision vector.
- [static func negative<U, V>(U, result: inout V)](vdsp/negative(_:result:)-5bwqv.md)
  Calculates the negative value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/negative(_:)-24oe4)*