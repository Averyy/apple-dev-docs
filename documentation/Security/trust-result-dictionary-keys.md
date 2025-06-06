# Trust Result Dictionary Keys

**Framework**: Security

Recognize the keys that appear in a dictionary containing information about an evaluated certification chain.

#### Overview

These keys appear in the dictionary returned from a call to the [`SecTrustCopyResult(_:)`](sectrustcopyresult(_:).md) function and provide information about the evaluated trust.

## Topics

### Constants
- [let kSecTrustCertificateTransparency: CFString](ksectrustcertificatetransparency.md)
  A key whose value is a Boolean used to indicate Certificate Transparency.
- [let kSecTrustCertificateTransparencyWhiteList: CFString](ksectrustcertificatetransparencywhitelist.md)
  A key whose value is a Boolean used to indicate the chain satisfies Certificate Transparency by being on the allow list.
- [let kSecTrustEvaluationDate: CFString](ksectrustevaluationdate.md)
  A key whose value indicates the time that the trust evaluation took place.
- [let kSecTrustExtendedValidation: CFString](ksectrustextendedvalidation.md)
  A key whose value is a Boolean used to indicate Extended Validation.
- [let kSecTrustOrganizationName: CFString](ksectrustorganizationname.md)
  A key whose value is the organization name field of the subject of the leaf certificate.
- [let kSecTrustResultValue: CFString](ksectrustresultvalue.md)
  A key whose value represents the trust evaluation result.
- [let kSecTrustRevocationChecked: CFString](ksectrustrevocationchecked.md)
  A key whose value indicates the outcome of revocation checking during trust evaluation.
- [let kSecTrustRevocationValidUntilDate: CFString](ksectrustrevocationvaliduntildate.md)
  A key whose value indicates the earliest date at which revocation information becomes stale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/trust-result-dictionary-keys)*