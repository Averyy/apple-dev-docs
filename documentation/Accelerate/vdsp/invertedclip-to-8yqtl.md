# invertedClip(_:to:)

**Framework**: Accelerate  
**Kind**: method

Returns a double-precision vector that’s inverted-clipped to the specified range.

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
static func invertedClip<U>(_ vector: U, to bounds: ClosedRange<Double>) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

## See Also

- [static func clip<U>(U, to: ClosedRange<Double>) -> [Double]](vdsp/clip(_:to:)-8jsic.md)
  Returns the elements of a double-precision vector clipped to the specified range.
- [static func clip<U>(U, to: ClosedRange<Float>) -> [Float]](vdsp/clip(_:to:)-20gz4.md)
  Returns the elements of a single-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Double>, result: inout V)](vdsp/clip(_:to:result:)-3lbii.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Float>, result: inout V)](vdsp/clip(_:to:result:)-84zw9.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Float>) -> [Float]](vdsp/invertedclip(_:to:)-4pkxw.md)
  Returns a single-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Double>, result: inout V)](vdsp/invertedclip(_:to:result:)-5ioal.md)
  Calculates a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Float>, result: inout V)](vdsp/invertedclip(_:to:result:)-3q12m.md)
  Calculates a single-precision vector that’s inverted-clipped to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/invertedclip(_:to:)-8yqtl)*