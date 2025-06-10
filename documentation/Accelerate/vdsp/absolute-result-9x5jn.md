# absolute(_:result:)

**Framework**: Accelerate  
**Kind**: method

Calculates the absolute value of each element in the supplied single-precision complex vector.

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
static func absolute<V>(_ vector: DSPSplitComplex, result: inout V) where V : AccelerateMutableBuffer, V.Element == Float
```

#### Discussion

This function returns the square roots of the sum of the squares of the real and imaginary parts of each complex element.

For example, the following code calculates the absolute values of four complex numbers:

```swift
    let n = 4
    
    let reals = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = reals.initialize(from: [-3, -6, 5, 9])
    
    let imaginaries = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = imaginaries.initialize(from: [4, -8, -12, 12])
    
    let values = DSPSplitComplex(realp: reals.baseAddress!,
                            imagp: imaginaries.baseAddress!)
    

    let absoluteValues = [Float](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP.absolute(values, result: &buffer)
        
        initializedCount = n
    }
    
    // Prints "[5.0, 10.0, 13.0, 15.0]".
    print(absoluteValues)
```

## Parameters

- `vector`: The source vector.
- `result`: On output, the absolute values of the elements in the source vector.

## See Also

- [static func absolute<V>(DSPDoubleSplitComplex, result: inout V)](vdsp/absolute(_:result:)-1wu9x.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/absolute(_:result:)-9x5jn)*