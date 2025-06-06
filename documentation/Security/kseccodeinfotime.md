# kSecCodeInfoTime

**Framework**: Security  
**Kind**: var

A key whose value is the signing date embedded in the code signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoTime: CFString
```

#### Discussion

The value is a [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate) object. Note that a signer is able to omit this date or pre-date it. Therefore, this is not necessarily the date the code was actually signed. However, you do know that this is the date the signer wanted you to see. Ad-hoc signatures never have secured signing dates.

Specify the [`kSecCSSigningInformation`](kseccssigninginformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfotime)*