# kSecCodeInfoEntitlements

**Framework**: Security  
**Kind**: var

A key whose value represents the embedded entitlement blob of the code, if any.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoEntitlements: CFString
```

#### Discussion

The value is a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object.

Specify the [`kSecCSRequirementInformation`](kseccsrequirementinformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoentitlements)*