# SecTrustCreateAndVerifyQWACTLSBinding(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
func SecTrustCreateAndVerifyQWACTLSBinding(_ bindingData: CFData, _ tlsTrust: SecTrust, _ error: UnsafeMutablePointer<CFError?>?) -> SecTrust?
```

```c
SecTrustRefSecTrustCreateAndVerifyQWACTLSBinding(CFDataRef bindingData, SecTrustRef tlsTrust, CFErrorRef*error);
```

## Return Value

On success, returns an evaluated trust object for the 2-QWAC chain taken from the binding’s x5c header parameter. The caller is responsible for calling CFRelease on a non-NULL return value when it is no longer needed. If validating the binding or the 2-QWAC certificate chain fails, returns NULL.

## Discussion

Validates a 2-QWAC TLS certificate binding against an established TLS connection, and returns an evaluated trust object for the 2-QWAC.

Verifies the JAdES signature over the binding using the public key of the 2-QWAC, evaluates the 2-QWAC chain with SecPolicyCreateQWACTLSBinding, and checks the binding values required by ETSI TS 119 411-5 Annex B, including that the TLS leaf certificate of tlsTrust appears in the signed list of bound certificates. The 2-QWAC is additive: it never affects TLS trust, and success requires both a valid TLS connection and a valid 2-QWAC.

A successful result describes the binding at the time of the call, and is not recorded on either trust object.

This call does not access the network. ETSI TS 119 411-5 Annex B requires the binding to carry the full 2-QWAC chain in its x5c header parameter, up to an issuer on the EU Trusted List, and those issuers are already in the trust store, so nothing needs to be fetched to build the chain. Network fetching is disabled on the 2-QWAC trust before it is evaluated: a binding whose x5c is incomplete is malformed and is rejected rather than completed from the network. Evaluation is therefore bounded, and does not follow URLs taken from attacker-supplied certificates.

## Parameters

- `bindingData`: The binding resource fetched from the server, a JWS Compact Serialization carrying a JAdES signature (ETSI TS 119 411-5 Annex B).
- `tlsTrust`: The already-evaluated trust object for the TLS connection the binding is claimed to bind to. The connection must have passed standard TLS trust evaluation on its own before calling this function.
- `error`: On failure, set to an error describing why the binding was rejected. Binding failures use kSecQWACTLSBindingErrorDomain with a SecQWACTLSBindingError code; invalid arguments are reported as errSecParam in kCFErrorDomainOSStatus. The caller is responsible for releasing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcreateandverifyqwactlsbinding(_:_:_:))*