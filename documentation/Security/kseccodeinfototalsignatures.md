# kSecCodeInfoTotalSignatures

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoTotalSignatures: CFString
```

```c
extern CFStringRef const kSecCodeInfoTotalSignatures;
```

## Discussion

Key in the dictionary returned by SecCodeCopySigningInformation. The value is a CFNumber giving the total number of signature slots present on the code object (ranging from 1 to kSecCSMaxSignatures).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfototalsignatures)*