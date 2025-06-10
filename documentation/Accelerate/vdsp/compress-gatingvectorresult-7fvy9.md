# compress(_:gatingVector:result:)

**Framework**: Accelerate  
**Kind**: method

Compresses the specified single-precision vector using the nonzero values in a gating vector.

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
static func compress<T, U, V>(_ vector: T, gatingVector: U, result: inout V) where T : AccelerateBuffer, U : AccelerateBuffer, V : AccelerateMutableBuffer, T.Element == Float, U.Element == Float, V.Element == Float
```

#### Discussion

The following code shows an example of compressing the values in `source` using the nonzero values in `gatingVector`:

```swift
let source: [Float] = [1, 2,
                       3, 4,
                       5, 6,
                       7, 8]

let gatingVector: [Float] = [-1, 0,
                             1, 0,
                             0.001, 0,
                             10, 0]

let count = gatingVector.filter {
    !$0.isZero
}.count

let destination = [Float](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP.compress(source,
                  gatingVector: gatingVector,
                  result: &buffer)
    
    initializedCount = count
}

// Prints "[1.0, 3.0, 5.0, 7.0]".
print(destination)
}
```

## Parameters

- `vector`: The source vector that the function compresses.
- `gatingVector`: The gating vector.
- `result`: The destination vector that receives the result.

## See Also

- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Float]](vdsp/compress(_:gatingvector:nonzerogatingcount:)-3c7yk.md)
  Returns a compressed copy of the specified single-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U>(T, gatingVector: U, nonZeroGatingCount: Int?) -> [Double]](vdsp/compress(_:gatingvector:nonzerogatingcount:)-93v23.md)
  Returns a compressed copy of the specified double-precision vector using the nonzero values in a gating vector.
- [static func compress<T, U, V>(T, gatingVector: U, result: inout V)](vdsp/compress(_:gatingvector:result:)-2yse4.md)
  Compresses the specified double-precision vector using the nonzero values in a gating vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/compress(_:gatingvector:result:)-7fvy9)*