# pixelBuffer

**Framework**: Core ML  
**Kind**: property

A reference to the multiarray’s underlying pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## See Also

- [subscript(Int) -> NSNumber](mlmultiarray/subscript(_:)-2hh91.md)
  Accesses the multiarray by using a linear offset.
- [subscript([NSNumber]) -> NSNumber](mlmultiarray/subscript(_:)-3d9el.md)
  Accesses the multiarray by using a number array that has an element for each dimension.
- [var dataPointer: UnsafeMutableRawPointer](mlmultiarray/datapointer.md)
  A pointer to the multiarray’s underlying memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/pixelbuffer)*