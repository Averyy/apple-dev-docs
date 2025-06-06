# kCGPDFXRegistryName

**Framework**: Core Graphics  
**Kind**: var

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
let kCGPDFXRegistryName: CFString
```

#### Discussion

A string identifying the registry in which the condition designated by [`kCGPDFXOutputConditionIdentifier`](kcgpdfxoutputconditionidentifier.md) is defined. This key is optional. If present, the value of this key must be a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) object. For best results, the string should be lossless in ASCII encoding.

## See Also

- [let kCGPDFXOutputIntentSubtype: CFString](kcgpdfxoutputintentsubtype.md)
  The output intent subtype. This key is required.
- [let kCGPDFXOutputConditionIdentifier: CFString](kcgpdfxoutputconditionidentifier.md)
- [let kCGPDFXOutputCondition: CFString](kcgpdfxoutputcondition.md)
  A text string identifying the intended output device or production condition in a human-readable form.
- [let kCGPDFXInfo: CFString](kcgpdfxinfo.md)
- [let kCGPDFXDestinationOutputProfile: CFString](kcgpdfxdestinationoutputprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfxregistryname)*