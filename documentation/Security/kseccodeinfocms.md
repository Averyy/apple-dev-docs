# kSecCodeInfoCMS

**Framework**: Security  
**Kind**: var

A key whose value is the CMS cryptographic object that secures the code signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoCMS: CFString
```

#### Discussion

The value is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object. Empty for ad-hoc signed code.

Specify the [`kSecCSSigningInformation`](kseccssigninginformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfocms)*