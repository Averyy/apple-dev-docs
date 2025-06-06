# kCGPDFXInfo

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
let kCGPDFXInfo: CFString
```

#### Discussion

A human-readable text string containing additional information or comments about the intended target device or production condition. This key is required if the value of [`kCGPDFXOutputConditionIdentifier`](kcgpdfxoutputconditionidentifier.md) does not specify a standard production condition. It is optional otherwise. If present, the value of this key must be a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) object.

## See Also

- [let kCGPDFXOutputIntentSubtype: CFString](kcgpdfxoutputintentsubtype.md)
  The output intent subtype. This key is required.
- [let kCGPDFXOutputConditionIdentifier: CFString](kcgpdfxoutputconditionidentifier.md)
- [let kCGPDFXOutputCondition: CFString](kcgpdfxoutputcondition.md)
  A text string identifying the intended output device or production condition in a human-readable form.
- [let kCGPDFXRegistryName: CFString](kcgpdfxregistryname.md)
- [let kCGPDFXDestinationOutputProfile: CFString](kcgpdfxdestinationoutputprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfxinfo)*