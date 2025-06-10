# absolute(_:)

**Framework**: Accelerate  
**Kind**: method

Returns the absolute value of each element in the supplied double-precision vector.

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
static func absolute<U>(_ vector: U) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

For example, the following code calculates the absolute values of the elements of an array:

```swift
    let values: [Double] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let absoluteValues = vDSP.absolute(values)
    
    // Prints "[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]".
    print(absoluteValues)
```

## Parameters

- `vector`: The source vector.

## See Also

- [static func absolute<U>(U) -> [Float]](vdsp/absolute(_:)-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-4pigo.md)
  Calculates the absolute value of each element in the supplied single-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/absolute(_:)-9c3ge)*