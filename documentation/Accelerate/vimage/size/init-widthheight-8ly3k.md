# init(width:height:)

**Framework**: Accelerate  
**Kind**: init

Creates a size with dimensions specified as unsigned integer values.

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
init(width: vImagePixelCount, height: vImagePixelCount)
```

#### Discussion

The height and width must be greater than `0`

## Parameters

- `width`: The width.
- `height`: The height.

## See Also

- [init(cvPixelBuffer: CVPixelBuffer)](vimage/size/init(cvpixelbuffer:).md)
  Creates a size with dimensions specified by a Core Video pixel buffer.
- [init?<T>(exactWidth: T, height: T)](vimage/size/init(exactwidth:height:)-9nwk0.md)
  Creates a size with dimensions specified as floating-point values.
- [init?<T>(exactWidth: T, height: T)](vimage/size/init(exactwidth:height:)-4ygbk.md)
  Creates a size with dimensions specified as integer values.
- [init?(exactly: CGSize)](vimage/size/init(exactly:).md)
  Creates a size with dimensions specified as a Core Graphics size value.
- [init(width: Int, height: Int)](vimage/size/init(width:height:)-fzcb.md)
  Creates a size with dimensions specified as integer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/size/init(width:height:)-8ly3k)*