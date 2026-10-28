# pointwiseMax(_:_:)

**Framework**: Swift  
**Kind**: func  
**Role**: Function

The lanewise maximum of two vectors.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func pointwiseMax<T>(_ a: T, _ b: T) -> T where T : SIMD, T.Scalar : Comparable
```

## Discussion

Each element of the result is the minimum of the corresponding elements of the inputs.

## See Also

### Supporting Functions
- [func all<Storage>(SIMDMask<Storage>) -> Bool](./all%28_%29.md)
  True if every lane of mask is true.
- [func any<Storage>(SIMDMask<Storage>) -> Bool](./any%28_%29.md)
  True if any lane of mask is true.
- [func pointwiseMax<T>(T, T) -> T](./pointwisemax%28_,_%29-29hn2.md)
  The lanewise maximum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](./pointwisemin%28_,_%29-39txi.md)
  The lanewise minimum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](./pointwisemin%28_,_%29-8v95p.md)
  The lanewise minimum of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/pointwisemax(_:_:)-2k6er)*