# taperedMerge(_:_:result:)

**Framework**: Accelerate  
**Kind**: method

Computes the result of a tapered merge between two single-precision vectors.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func taperedMerge<T, U, V>(_ vectorA: T, _ vectorB: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

#### Discussion

The following code performs a tapered merge between two vectors that represent sine waves at different frequencies:

```swift
let count = 1024

let vectorA: [Float] = (0 ..< count).map {
    return sin(Float($0) * 0.4)
}

let vectorB: [Float] = (0 ..< count).map {
    return sin(Float($0) * 0.025)
}

let tapered = [Float](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP.taperedMerge(vectorA, vectorB,
                      result: &buffer)
    
    initializedCount = count
}
```

The following image shows the result of the tapered merge in `tapered`.

![Graphic showing the tapered merge from a high-frequency sine wave to a low-frequency sine wave.](https://docs-assets.developer.apple.com/published/8f7231a827070d459218346b0ddbcfc7/media-3681543%402x.png)

## Parameters

- `vectorA`: The first vector to merge.
- `vectorB`: The second vector to merge.
- `result`: The destination vector that receives the result.

## See Also

- [static func taperedMerge<T, U>(T, U) -> [Float]](vdsp/taperedmerge(_:_:)-5dhoj.md)
  Returns the result of a tapered merge between two single-precision vectors.
- [static func taperedMerge<T, U>(T, U) -> [Double]](vdsp/taperedmerge(_:_:)-9s9j5.md)
  Returns the result of a tapered merge between two double-precision vectors.
- [static func taperedMerge<T, U, V>(T, U, result: inout V)](vdsp/taperedmerge(_:_:result:)-9361o.md)
  Computes the result of a tapered merge between two double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/taperedmerge(_:_:result:)-74fuy)*