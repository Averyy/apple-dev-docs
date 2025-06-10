# init(exactly:)

**Framework**: Accelerate  
**Kind**: init

Creates a size with dimensions specified as a Core Graphics size value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init?(exactly size: CGSize)
```

#### Discussion

The height and width must be greater than `0` and exactly representable as an `Int` value.

## Parameters

- `size`: The size.

## See Also

- [init(cvPixelBuffer: CVPixelBuffer)](vimage/size/init(cvpixelbuffer:).md)
  Creates a size with dimensions specified by a Core Video pixel buffer.
- [init?<T>(exactWidth: T, height: T)](vimage/size/init(exactwidth:height:)-9nwk0.md)
  Creates a size with dimensions specified as floating-point values.
- [init?<T>(exactWidth: T, height: T)](vimage/size/init(exactwidth:height:)-4ygbk.md)
  Creates a size with dimensions specified as integer values.
- [init(width: Int, height: Int)](vimage/size/init(width:height:)-fzcb.md)
  Creates a size with dimensions specified as integer values.
- [init(width: vImagePixelCount, height: vImagePixelCount)](vimage/size/init(width:height:)-8ly3k.md)
  Creates a size with dimensions specified as unsigned integer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/size/init(exactly:))*