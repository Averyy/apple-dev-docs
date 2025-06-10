# absolute(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the absolute value of each element in the supplied single-precision vector.

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
static func absolute<U, V>(_ vector: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

#### Discussion

For example, the following code calculates the absolute values of the elements of an array:

```swift
    let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let absoluteValues = [Float](unsafeUninitializedCapacity: values.count) {
        buffer, initializedCount in
        
        vDSP.absolute(values, result: &buffer)
        
        initializedCount = values.count
    }
    
    // Prints "[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]".
    print(absoluteValues)
```

## Parameters

- `vector`: The source vector.
- `result`: On output, the absolute values of the elements in the source vector.

## See Also

- [static func absolute<U>(U) -> [Float]](vdsp/absolute(_:)-5ehc1.md)
  Returns the absolute value of each element in the supplied single-precision vector.
- [static func absolute<U>(U) -> [Double]](vdsp/absolute(_:)-9c3ge.md)
  Returns the absolute value of each element in the supplied double-precision vector.
- [static func absolute<U, V>(U, result: inout V)](vdsp/absolute(_:result:)-657bd.md)
  Calculates the absolute value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/absolute(_:result:)-4pigo)*