# kCGImagePropertyHasAlpha

**Framework**: Image I/O  
**Kind**: var  
**Role**: Global Variable

A Boolean value that indicates whether the image has an alpha channel.

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
let kCGImagePropertyHasAlpha: CFString
```

```c
extern CFStringRef const kCGImagePropertyHasAlpha;
```

#### Discussion

The value of this key is a [`CFBoolean`](../CoreFoundation/cfboolean.md). The value is [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) when the image contains an alpha channel.

## See Also

### Color Information
- [let kCGImagePropertyNamedColorSpace: CFString](./kcgimagepropertynamedcolorspace.md)
  The name of the image’s color space.
- [let kCGImagePropertyProfileName: CFString](./kcgimagepropertyprofilename.md)
  The name of the optional International Color Consortium (ICC) profile embedded in the image, if known.
- [let kCGImagePropertyColorModel: CFString](./kcgimagepropertycolormodel.md)
  The color model of the image, such as RGB, CMYK, grayscale, or Lab.
- [let kCGImagePropertyColorModelRGB: CFString](./kcgimagepropertycolormodelrgb.md)
  A Red Green Blue (RGB) color model.
- [let kCGImagePropertyColorModelCMYK: CFString](./kcgimagepropertycolormodelcmyk.md)
  A Cyan Magenta Yellow Black (CMYK) color model.
- [let kCGImagePropertyColorModelGray: CFString](./kcgimagepropertycolormodelgray.md)
  A grayscale color model.
- [let kCGImagePropertyColorModelLab: CFString](./kcgimagepropertycolormodellab.md)
  A Lab color model, where color values contain the amount of light and the amounts of four human-perceivable colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/kcgimagepropertyhasalpha)*