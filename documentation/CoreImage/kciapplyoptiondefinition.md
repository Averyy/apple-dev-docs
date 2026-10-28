# kCIApplyOptionDefinition

**Framework**: Core Image  
**Kind**: var  
**Role**: Global Variable

The domain of definition (DOD) of the produced image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kCIApplyOptionDefinition: String
```

```c
extern NSString * const kCIApplyOptionDefinition;
```

## Discussion

The associated value is either a Core Image filter shape or a four-element array ([`NSArray`](../Foundation/nsarray.md)) that specifies a rectangle.

## See Also

### Constants
- [let kCIApplyOptionExtent: String](./kciapplyoptionextent.md)
  The extent of the image.
- [let kCIApplyOptionUserInfo: String](./kciapplyoptionuserinfo.md)
  Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [let kCIApplyOptionColorSpace: String](./kciapplyoptioncolorspace.md)
  The color space of the produced image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kciapplyoptiondefinition)*