# kSecTrustOrganizationName

**Framework**: Security  
**Kind**: var

A key whose value is the organization name field of the subject of the leaf certificate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecTrustOrganizationName: CFString
```

#### Discussion

The value is a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) that is meant to be displayed to the user as the validated name of the company or entity that owns the certificate, but only if the [`kSecTrustExtendedValidation`](ksectrustextendedvalidation.md) key is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustorganizationname)*