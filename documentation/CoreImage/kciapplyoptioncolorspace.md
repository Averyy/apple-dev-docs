# kCIApplyOptionColorSpace

**Framework**: Core Image  
**Kind**: var

The color space of the produced image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kCIApplyOptionColorSpace: String
```

#### Discussion

The associated value must be an RGB [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) object. If not specified, the output of the kernel is in the working color space of the Core Image context used to render the image.

## See Also

- [let kCIApplyOptionExtent: String](kciapplyoptionextent.md)
  The extent of the image.
- [let kCIApplyOptionDefinition: String](kciapplyoptiondefinition.md)
  The domain of definition (DOD) of the produced image.
- [let kCIApplyOptionUserInfo: String](kciapplyoptionuserinfo.md)
  Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace)*