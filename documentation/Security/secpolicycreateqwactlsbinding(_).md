# SecPolicyCreateQWACTLSBinding(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecPolicyCreateQWACTLSBinding(_ hostname: CFString) -> SecPolicy?
```

```c
SecPolicyRefSecPolicyCreateQWACTLSBinding(CFStringRef hostname);
```

## Return Value

A policy object. The caller is responsible for calling CFRelease on this when it is no longer needed.

## Discussion

Returns a policy object for verifying an EU 2-QWAC certificate (a QWAC issued for TLS certificate binding).

Builds on the Basic X.509 policy: it checks validity, that the leaf is issued for TLS certificate binding (the id-kp-tls-binding EKU and the qualified certificate statements of ETSI TS 119 411-5), and that the chain terminates at a QWAC-constrained EU Trusted List anchor. It validates the certificate profile only; the binding to the TLS certificate is performed by SecTrustCreateAndVerifyQWACTLSBinding (see <Security/SecQWACTLSBinding.h>).

## Parameters

- `hostname`: The policy will require the specified hostname to match the SAN list in the leaf certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicycreateqwactlsbinding(_:))*