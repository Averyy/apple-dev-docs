# dataPointer

**Framework**: Core ML  
**Kind**: property

A pointer to the multiarray’s underlying memory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var dataPointer: UnsafeMutableRawPointer { get }
```

## See Also

- [subscript(Int) -> NSNumber](mlmultiarray/subscript(_:)-2hh91.md)
  Accesses the multiarray by using a linear offset.
- [subscript([NSNumber]) -> NSNumber](mlmultiarray/subscript(_:)-3d9el.md)
  Accesses the multiarray by using a number array that has an element for each dimension.
- [var pixelBuffer: CVPixelBuffer?](mlmultiarray/pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/datapointer)*