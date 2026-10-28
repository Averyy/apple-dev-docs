# kCGPDFXOutputCondition

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

A text string identifying the intended output device or production condition in a human-readable form.

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
let kCGPDFXOutputCondition: CFString
```

```c
extern CFStringRef const kCGPDFXOutputCondition;
```

## Discussion

This key is optional. If present, the value of this key must be a [`CFString`](../CoreFoundation/cfstring.md) object.

## See Also

### Output Intent Keys
- [let kCGPDFXOutputIntentSubtype: CFString](./kcgpdfxoutputintentsubtype.md)
  The output intent subtype. This key is required.
- [let kCGPDFXOutputConditionIdentifier: CFString](./kcgpdfxoutputconditionidentifier.md)
- [let kCGPDFXRegistryName: CFString](./kcgpdfxregistryname.md)
- [let kCGPDFXInfo: CFString](./kcgpdfxinfo.md)
- [let kCGPDFXDestinationOutputProfile: CFString](./kcgpdfxdestinationoutputprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputcondition)*