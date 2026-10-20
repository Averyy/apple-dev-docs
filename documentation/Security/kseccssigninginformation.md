# kSecCSSigningInformation

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

Cryptographic signing information.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSSigningInformation: UInt32 { get }
```

```c
kSecCSSigningInformation
```

#### Discussion

The certificate chain and Cryptographic Message Syntax (CMS) data (if any). For ad-hoc signed code, there are no certificates and the CMS data is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccssigninginformation)*