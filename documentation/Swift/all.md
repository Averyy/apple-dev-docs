# all(_:)

**Framework**: Swift  
**Kind**: func

True if every lane of mask is true.

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
func all<Storage>(_ mask: SIMDMask<Storage>) -> Bool where Storage : SIMD, Storage.Scalar : FixedWidthInteger, Storage.Scalar : SignedInteger
```

## See Also

- [func any<Storage>(SIMDMask<Storage>) -> Bool](any(_:).md)
  True if any lane of mask is true.
- [func pointwiseMax<T>(T, T) -> T](pointwisemax(_:_:)-29hn2.md)
  The lanewise maximum of two vectors.
- [func pointwiseMax<T>(T, T) -> T](pointwisemax(_:_:)-2k6er.md)
  The lanewise maximum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](pointwisemin(_:_:)-39txi.md)
  The lanewise minimum of two vectors.
- [func pointwiseMin<T>(T, T) -> T](pointwisemin(_:_:)-8v95p.md)
  The lanewise minimum of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/all(_:))*