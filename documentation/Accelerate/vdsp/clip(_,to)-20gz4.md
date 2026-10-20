# clip(_:to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Type Method

Returns the elements of a single-precision vector clipped to the specified range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
static func clip<U>(_ vector: U, to bounds: ClosedRange<Float>) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

### Clipping Operations
- [static func clip<U>(U, to: ClosedRange<Double>) -> [Double]](./clip%28_,to%29-8jsic.md)
  Returns the elements of a double-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./clip%28_,to,result%29-3lbii.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [static func clip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./clip%28_,to,result%29-84zw9.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Double>) -> [Double]](./invertedclip%28_,to%29-8yqtl.md)
  Returns a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U>(U, to: ClosedRange<Float>) -> [Float]](./invertedclip%28_,to%29-4pkxw.md)
  Returns a single-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Double>, result: inout V)](./invertedclip%28_,to,result%29-5ioal.md)
  Calculates a double-precision vector that’s inverted-clipped to the specified range.
- [static func invertedClip<U, V>(U, to: ClosedRange<Float>, result: inout V)](./invertedclip%28_,to,result%29-3q12m.md)
  Calculates a single-precision vector that’s inverted-clipped to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/clip(_:to:)-20gz4)*