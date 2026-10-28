# kCGPDFXOutputIntentSubtype

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

The output intent subtype. This key is required.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.4+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let kCGPDFXOutputIntentSubtype: CFString
```

```c
extern CFStringRef const kCGPDFXOutputIntentSubtype;
```

## Discussion

The value of this key must be a [`CFString`](../CoreFoundation/cfstring.md) object equal to `"GTS_PDFX"`; otherwise, the dictionary is ignored.

## See Also

### Output Intent Keys
- [let kCGPDFXOutputConditionIdentifier: CFString](./kcgpdfxoutputconditionidentifier.md)
- [let kCGPDFXOutputCondition: CFString](./kcgpdfxoutputcondition.md)
  A text string identifying the intended output device or production condition in a human-readable form.
- [let kCGPDFXRegistryName: CFString](./kcgpdfxregistryname.md)
- [let kCGPDFXInfo: CFString](./kcgpdfxinfo.md)
- [let kCGPDFXDestinationOutputProfile: CFString](./kcgpdfxdestinationoutputprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputintentsubtype)*