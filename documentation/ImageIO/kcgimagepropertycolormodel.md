# kCGImagePropertyColorModel

**Framework**: Image I/O  
**Kind**: var

The color model of the image, such as RGB, CMYK, grayscale, or Lab.

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
let kCGImagePropertyColorModel: CFString
```

#### Discussion

The value of this key is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString). Typically, the value corresponds to the [`kCGImagePropertyColorModelRGB`](kcgimagepropertycolormodelrgb.md), [`kCGImagePropertyColorModelCMYK`](kcgimagepropertycolormodelcmyk.md), [`kCGImagePropertyColorModelGray`](kcgimagepropertycolormodelgray.md), or [`kCGImagePropertyColorModelLab`](kcgimagepropertycolormodellab.md) constant.

A color model describes how color values are represented mathematically. A color space is a color model combined with a definition of how to interpret values within the model.

## See Also

- [let kCGImagePropertyHasAlpha: CFString](kcgimagepropertyhasalpha.md)
  A Boolean value that indicates whether the image has an alpha channel.
- [let kCGImagePropertyNamedColorSpace: CFString](kcgimagepropertynamedcolorspace.md)
  The name of the image’s color space.
- [let kCGImagePropertyProfileName: CFString](kcgimagepropertyprofilename.md)
  The name of the optional International Color Consortium (ICC) profile embedded in the image, if known.
- [let kCGImagePropertyColorModelRGB: CFString](kcgimagepropertycolormodelrgb.md)
  A Red Green Blue (RGB) color model.
- [let kCGImagePropertyColorModelCMYK: CFString](kcgimagepropertycolormodelcmyk.md)
  A Cyan Magenta Yellow Black (CMYK) color model.
- [let kCGImagePropertyColorModelGray: CFString](kcgimagepropertycolormodelgray.md)
  A grayscale color model.
- [let kCGImagePropertyColorModelLab: CFString](kcgimagepropertycolormodellab.md)
  A Lab color model, where color values contain the amount of light and the amounts of four human-perceivable colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodel)*