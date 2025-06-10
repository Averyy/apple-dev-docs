# copy(_:to:count:)

**Framework**: Accelerate  
**Kind**: method

Copies a complex single-precision vector.

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
static func copy(_ source: DSPSplitComplex, to destination: inout DSPSplitComplex, count: Int)
```

#### Discussion

The following code copies the complex elements in the source to the destination:

```swift
    let realSrc = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    _ = realSrc.initialize(from: [0, 2, 4, 6])
    
    let imagSrc = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    _ = imagSrc.initialize(from: [1, 3, 5, 7])
    
    let source = DSPSplitComplex(realp: realSrc.baseAddress!,
                                 imagp: imagSrc.baseAddress!)
    
    let realDst = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    let imagDst = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)

    var destination = DSPSplitComplex(realp: realDst.baseAddress!,
                                 imagp: imagDst.baseAddress!)
    
    vDSP.copy(source, to: &destination, count: 4)
    
    print(Array(realDst)) // Prints "[0.0, 2.0, 4.0, 6.0]".
    print(Array(imagDst)) // Prints "[1.0, 3.0, 5.0, 7.0]".
```

## Parameters

- `source`: The source complex vector.
- `destination`: The destination complex vector.
- `count`: The number of complex elements in the source and destination vectors.

## See Also

- [static func copy(DSPDoubleSplitComplex, to: inout DSPDoubleSplitComplex, count: Int)](vdsp/copy(_:to:count:)-7zpro.md)
  Copies a complex double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/copy(_:to:count:)-96jr5)*