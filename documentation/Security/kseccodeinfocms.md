# kSecCodeInfoCMS

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is the CMS cryptographic object that secures the code signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoCMS: CFString
```

```c
extern CFStringRef const kSecCodeInfoCMS;
```

## Discussion

The value is a [`CFData`](../CoreFoundation/cfdata.md) object. Empty for ad-hoc signed code.

Specify the [`kSecCSSigningInformation`](./kseccssigninginformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfocms)*