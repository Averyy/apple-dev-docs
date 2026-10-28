# kCGImagePropertyHeight

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

The height of the image, in the image’s coordinate space.

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
let kCGImagePropertyHeight: CFString
```

```c
extern CFStringRef const kCGImagePropertyHeight;
```

## Discussion

The value of this property is a [`CFNumber`](../CoreFoundation/cfnumber.md).

## See Also

### Image Size
- [let kCGImagePropertyWidth: CFString](./kcgimagepropertywidth.md)
  The width of the image, in the image’s coordinate space.
- [let kCGImagePropertyBytesPerRow: CFString](./kcgimagepropertybytesperrow.md)
  The total number of bytes in each row of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyheight)*