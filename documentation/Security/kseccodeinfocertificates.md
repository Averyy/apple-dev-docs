# kSecCodeInfoCertificates

**Framework**: Security  
**Kind**: var

A key whose value is an array of certificates representing the certificate chain of the signing certificate as seen by the system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoCertificates: CFString
```

#### Discussion

The value is a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) array of [`SecCertificate`](seccertificate.md) objects that the system uses to process the signature. Absent for ad-hoc signed code. May be partial or absent in the case of error.

Specify the [`kSecCSSigningInformation`](kseccssigninginformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfocertificates)*