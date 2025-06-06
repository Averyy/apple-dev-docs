# Policies

**Framework**: Security

Obtain policies for establishing trust.

#### Overview

For a certificate that is deemed intact and valid (because the chain of signatures is unbroken back to a trusted root certificate), you evaluate it against a set of rules known as a . The policy indicates how particular fields or extensions of a certificate affect whether it should be trusted for a particular use. For example, the policy may state that a certificate must not be expired or must be marked as valid for encryption, code signing, or some other specific purpose.

Usually you use a standard, predefined policy, such as the basic X509 policy or the SSL policy. You can also create custom policies with the certificate, key, and trust services API.

## Topics

### Standard Policies
- [func SecPolicyCreateBasicX509() -> SecPolicy](secpolicycreatebasicx509().md)
  Returns a policy object for the default X.509 policy.
- [func SecPolicyCreateSSL(Bool, CFString?) -> SecPolicy](secpolicycreatessl(_:_:).md)
  Returns a policy object for evaluating SSL certificate chains.
- [func SecPolicyCreateRevocation(CFOptionFlags) -> SecPolicy?](secpolicycreaterevocation(_:).md)
  Returns a policy object for checking revocation of certificates.
- [Revocation Policy Constants](revocation-policy-constants.md)
  Use these flags to create a revocation policy object.
- [class SecPolicy](secpolicy.md)
  An object that represents a trust policy.
- [func SecPolicyGetTypeID() -> CFTypeID](secpolicygettypeid().md)
  Returns the unique identifier of the opaque type to which a policy object belongs.
### Advanced Policy Management
- [func SecPolicyCreateWithProperties(CFTypeRef, CFDictionary?) -> SecPolicy?](secpolicycreatewithproperties(_:_:).md)
  Returns a policy object based on an object identifier for the policy type.
- [func SecPolicyCopyProperties(SecPolicy) -> CFDictionary?](secpolicycopyproperties(_:).md)
  Returns a dictionary containing a policy’s properties.
- [Security Policy Keys](security-policy-keys.md)
  Use these dictionary keys to get and set policy properties.
- [Standard Policies for Specific Certificate Types](standard-policies-for-specific-certificate-types.md)
  Use special OIDs to cause a certificate to be evaluated based on security policies specific to a given type of certificate.
### Legacy Symbols
- [class SecPolicySearch](secpolicysearch.md)
  An object that contains information about a policy search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/policies)*