# cropped(to:)

**Framework**: Accelerate  
**Kind**: method

Returns a new pixel buffer that contains a copy of the data specified as a subregion of an existing pixel buffer.

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
func cropped(to rect: CGRect) -> vImage.PixelBuffer<Format>
```

#### Return Value

A pixel buffer that contains of a copy of the specified subregion.

#### Discussion

For example, the following code populates a pixel buffer from the center 3 x 3 pixels of a 5 x 5 planar buffer:

```swift
let src = vImage.PixelBuffer<vImage.Planar8> (
    pixelValues: [ 10, 11, 12, 13, 14,
                   20, 21, 22, 23, 24,
                   30, 31, 32, 33, 34,
                   40, 41, 42, 43, 44,
                   50, 51, 52, 53, 54 ],
    size: vImage.Size(width: 5,
                      height: 5))

let roi = CGRect(x: 1, y: 1,
                 width: 3, height: 3)

let dest = src.cropped(to: roi)

// Prints:
//  [ 21, 22, 23,
//    31, 32, 33,
//    41, 42, 43 ]
print(dest.array)
```

## Parameters

- `rect`: A rectangle that specifies the portion of the image to keep.

## See Also

- [func crop(at: CGPoint, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/crop(at:destination:).md)
  Crops the pixel buffer to a rectangle that’s defined by an origin and the destination buffer’s dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/cropped(to:))*