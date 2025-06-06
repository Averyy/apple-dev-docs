# Revocation Policy Constants

**Framework**: Security

Use these flags to create a revocation policy object.

#### Overview

Use these flags with a call to the [`SecPolicyCreateRevocation(_:)`](secpolicycreaterevocation(_:).md) function to characterize the constructed policy.

## Topics

### Constants
- [var kSecRevocationCRLMethod: CFOptionFlags](ksecrevocationcrlmethod.md)
  Perform revocation checking using the CRL (Certification Revocation List) method.
- [var kSecRevocationNetworkAccessDisabled: CFOptionFlags](ksecrevocationnetworkaccessdisabled.md)
  Consult only locally cached replies; do not use network access.
- [var kSecRevocationOCSPMethod: CFOptionFlags](ksecrevocationocspmethod.md)
  Perform revocation     checking using OCSP (Online Certificate Status Protocol).
- [var kSecRevocationPreferCRL: CFOptionFlags](ksecrevocationprefercrl.md)
  Prefer CRL revocation checking over OCSP; by default, OCSP is preferred.
- [var kSecRevocationRequirePositiveResponse: CFOptionFlags](ksecrevocationrequirepositiveresponse.md)
  Require a positive response to pass the policy.
- [var kSecRevocationUseAnyAvailableMethod: CFOptionFlags](ksecrevocationuseanyavailablemethod.md)
  Perform either OCSP or CRL checking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/revocation-policy-constants)*