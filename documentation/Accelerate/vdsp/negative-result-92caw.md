# negative(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the negative value of each element in the supplied single-precision vector.

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
static func negative<U, V>(_ vector: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

```swift
    let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let negativeValues = [Float](unsafeUninitializedCapacity: values.count) {
        buffer, initializedCount in
        
        vDSP.negative(values, result: &buffer)
        
        initializedCount = values.count
    }
    
    // Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
    print(negativeValues)
```

## Parameters

- `vector`: The source vector.
- `result`: On output, the negative values of the elements in the source vector.

## See Also

- [static func negative<U>(U) -> [Float]](vdsp/negative(_:)-8mo1p.md)
  Returns the negative value of each element in the supplied single-precision vector.
- [static func negative<U>(U) -> [Double]](vdsp/negative(_:)-24oe4.md)
  Returns the negative value of each element in the supplied double-precision vector.
- [static func negative<U, V>(U, result: inout V)](vdsp/negative(_:result:)-5bwqv.md)
  Calculates the negative value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/negative(_:result:)-92caw)*