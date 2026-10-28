# init(exactWidth:height:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a size with dimensions specified as integer values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init?<T>(exactWidth: T, height: T) where T : BinaryInteger
```

## Discussion

The height and width must be greater than `0` and exactly representable as an `Int` value.

## Parameters

- `exactWidth`: The width.
- `height`: The height.

## See Also

### Initializers
- [init(cvPixelBuffer: CVPixelBuffer)](./init%28cvpixelbuffer%29.md)
  Creates a size with dimensions specified by a Core Video pixel buffer.
- [init?<T>(exactWidth: T, height: T)](./init%28exactwidth,height%29-9nwk0.md)
  Creates a size with dimensions specified as floating-point values.
- [init?(exactly: CGSize)](./init%28exactly%29.md)
  Creates a size with dimensions specified as a Core Graphics size value.
- [init(width: Int, height: Int)](./init%28width,height%29-fzcb.md)
  Creates a size with dimensions specified as integer values.
- [init(width: vImagePixelCount, height: vImagePixelCount)](./init%28width,height%29-8ly3k.md)
  Creates a size with dimensions specified as unsigned integer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/size/init(exactwidth:height:)-4ygbk)*