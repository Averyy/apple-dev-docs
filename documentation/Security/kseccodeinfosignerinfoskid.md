# kSecCodeInfoSignerInfoSKID

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoSignerInfoSKID: CFString
```

```c
extern CFStringRef const kSecCodeInfoSignerInfoSKID;
```

## Discussion

Key in the dictionary returned by SecCodeCopySigningInformation. The value is a CFData containing the Subject Key Identifier (SKID) of the leaf signing certificate. Useful for looking up detached certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfosignerinfoskid)*