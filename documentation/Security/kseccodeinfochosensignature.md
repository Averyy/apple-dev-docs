# kSecCodeInfoChosenSignature

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoChosenSignature: CFString
```

```c
extern CFStringRef const kSecCodeInfoChosenSignature;
```

## Discussion

Key in the dictionary returned by SecCodeCopySigningInformation. The value is a CFNumber containing the 1-based index of the signature slot that was selected for validation and information retrieval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfochosensignature)*