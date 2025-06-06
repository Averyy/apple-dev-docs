# kSecCodeInfoTrust

**Framework**: Security  
**Kind**: var

A key whose value is the trust object the system uses to evaluate the validity of the code’s signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoTrust: CFString
```

#### Discussion

The value is a retained [`SecTrust`](sectrust.md) object. You may use [`SecTrust`](sectrust.md) functions (see [`Certificate, Key, and Trust Services`](certificate-key-and-trust-services.md) to extract detailed information, for example the reasons why certificate validation may have failed. Because this object may continue to be used for further evaluations of the code signature, if you make any changes to it, the behavior of the [`SecTrust`](sectrust.md) functions is undefined.

Specify the [`kSecCSSigningInformation`](kseccssigninginformation.md) flag when calling the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to get this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfotrust)*