# kCGImagePropertyDepth

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

The number of bits in the color sample of a pixel.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGImagePropertyDepth: CFString
```

```c
extern CFStringRef const kCGImagePropertyDepth;
```

## Discussion

The value of this key is a [`CFNumber`](../CoreFoundation/cfnumber.md).

## See Also

### Pixel Information
- [let kCGImagePropertyPixelFormat: CFString](./kcgimagepropertypixelformat.md)
  The format of the image’s individual pixels.
- [let kCGImagePropertyPixelWidth: CFString](./kcgimagepropertypixelwidth.md)
  The number of pixels along the x-axis of the image.
- [let kCGImagePropertyPixelHeight: CFString](./kcgimagepropertypixelheight.md)
  The number of pixels along the y-axis of the image.
- [let kCGImagePropertyDPIHeight: CFString](./kcgimagepropertydpiheight.md)
  The resolution, in dots per inch, in the y dimension.
- [let kCGImagePropertyDPIWidth: CFString](./kcgimagepropertydpiwidth.md)
  The resolution, in dots per inch, in the x dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertydepth)*