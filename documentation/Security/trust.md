# Trust

**Framework**: Security

Evaluate trust based on a given policy.

#### Overview

Before using a certificate, you evaluate its trustworthiness for a particular purpose.

If you know that a certificate comes unaltered from its sender, you can be confident that its embedded public key does as well. You can also take at face value claims made by the certificate about when and for what purpose the public key may be used. You can securely engage in the operations described in [`Using Keys for Encryption`](using-keys-for-encryption.md) and [`Signing and Verifying`](signing-and-verifying.md) without prior arrangement between sender and receiver.

## Topics

### Essentials
- [Creating a Trust Object](creating-a-trust-object.md)
  Construct a trust object from a certificate and a policy.
- [func SecTrustCreateWithCertificates(CFTypeRef, CFTypeRef?, UnsafeMutablePointer<SecTrust?>) -> OSStatus](sectrustcreatewithcertificates(_:_:_:).md)
  Creates a trust management object based on certificates and policies.
- [class SecTrust](sectrust.md)
  An object used to evaluate trust.
- [func SecTrustGetTypeID() -> CFTypeID](sectrustgettypeid().md)
  Returns the unique identifier of the opaque type to which a trust object belongs.
### Trust Evaluation
- [Evaluating a Trust and Parsing the Result](evaluating-a-trust-and-parsing-the-result.md)
  Learn what to expect when evaluating a trust object.
- [func SecTrustEvaluateWithError(SecTrust, UnsafeMutablePointer<CFError?>?) -> Bool](sectrustevaluatewitherror(_:_:).md)
  Evaluates trust for the specified certificate and policies.
- [func SecTrustEvaluateAsyncWithError(SecTrust, dispatch_queue_t, SecTrustWithErrorCallback) -> OSStatus](sectrustevaluateasyncwitherror(_:_:_:).md)
  Evaluates a trust object asynchronously on the specified dispatch queue.
- [typealias SecTrustWithErrorCallback](sectrustwitherrorcallback.md)
  A block called with the results of an asynchronous trust evaluation.
### Trust Evaluation Result
- [Discovering Why a Trust Evaluation Failed](discovering-why-a-trust-evaluation-failed.md)
  Determine whether you can recover from a failed trust evaluation.
- [func SecTrustGetTrustResult(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](sectrustgettrustresult(_:_:).md)
  Returns the result code from the most recent trust evaluation.
- [enum SecTrustResultType](sectrustresulttype.md)
  Trust evaluation result codes.
- [func SecTrustCopyResult(SecTrust) -> CFDictionary?](sectrustcopyresult(_:).md)
  Returns a dictionary containing information about an evaluated trust.
- [Trust Result Dictionary Keys](trust-result-dictionary-keys.md)
  Recognize the keys that appear in a dictionary containing information about an evaluated certification chain.
### Trust Components
- [func SecTrustCopyPublicKey(SecTrust) -> SecKey?](sectrustcopypublickey(_:).md)
  Returns the public key for a leaf certificate after it has been evaluated.
- [func SecTrustGetCertificateCount(SecTrust) -> CFIndex](sectrustgetcertificatecount(_:).md)
  Returns the number of certificates in an evaluated certificate chain.
- [func SecTrustGetCertificateAtIndex(SecTrust, CFIndex) -> SecCertificate?](sectrustgetcertificateatindex(_:_:).md)
  Returns a specific certificate from the certificate chain used to evaluate trust.
- [func SecTrustGetVerifyTime(SecTrust) -> CFAbsoluteTime](sectrustgetverifytime(_:).md)
  Gets the absolute time against which the certificates in a trust management object are verified.
- [func SecTrustCopyAnchorCertificates(UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustcopyanchorcertificates(_:).md)
  Retrieves the anchor (root) certificates stored by macOS.
- [func SecTrustCopyCustomAnchorCertificates(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustcopycustomanchorcertificates(_:_:).md)
  Retrieves the custom anchor certificates, if any, used by a given trust.
- [func SecTrustCopyExceptions(SecTrust) -> CFData?](sectrustcopyexceptions(_:).md)
  Returns an opaque cookie containing exceptions to trust policies that will allow future evaluations of the current certificate to succeed.
- [func SecTrustCopyPolicies(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustcopypolicies(_:_:).md)
  Retrieves the policies used by a given trust management object.
- [func SecTrustCopyProperties(SecTrust) -> CFArray?](sectrustcopyproperties(_:).md)
  Returns an array containing the properties of a trust object.
### Advanced Trust Configuation
- [Configuring a Trust](configuring-a-trust.md)
  Work around a recoverable trust failure.
- [func SecTrustSetVerifyDate(SecTrust, CFDate) -> OSStatus](sectrustsetverifydate(_:_:).md)
  Sets the date and time against which the certificates in a trust management object are verified.
- [func SecTrustSetAnchorCertificates(SecTrust, CFArray?) -> OSStatus](sectrustsetanchorcertificates(_:_:).md)
  Sets the anchor certificates used when evaluating a trust management object.
- [func SecTrustSetAnchorCertificatesOnly(SecTrust, Bool) -> OSStatus](sectrustsetanchorcertificatesonly(_:_:).md)
  Reenables trusting built-in anchor certificates.
- [func SecTrustSetExceptions(SecTrust, CFData?) -> Bool](sectrustsetexceptions(_:_:).md)
  Sets a list of exceptions that should be ignored when the certificate is evaluated.
- [func SecTrustSetPolicies(SecTrust, CFTypeRef) -> OSStatus](sectrustsetpolicies(_:_:).md)
  Sets the policies to use in an evaluation.
- [func SecTrustSetOptions(SecTrust, SecTrustOptionFlags) -> OSStatus](sectrustsetoptions(_:_:).md)
  Sets option flags for customizing evaluation of a trust object.
- [struct SecTrustOptionFlags](sectrustoptionflags.md)
  The option flags used to condition a trust evaluation.
- [func SecTrustGetNetworkFetchAllowed(SecTrust, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](sectrustgetnetworkfetchallowed(_:_:).md)
  Indicates whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [func SecTrustSetNetworkFetchAllowed(SecTrust, Bool) -> OSStatus](sectrustsetnetworkfetchallowed(_:_:).md)
  Specifies whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [func SecTrustSetOCSPResponse(SecTrust, CFTypeRef?) -> OSStatus](sectrustsetocspresponse(_:_:).md)
  Attaches Online Certificate Status Protocol (OSCP) response data to a trust object.
- [func SecTrustSetSignedCertificateTimestamps(SecTrust, CFArray?) -> OSStatus](sectrustsetsignedcertificatetimestamps(_:_:).md)
  Attaches signed certificate timestamp data to a trust object.
### Trust Settings
- [func SecTrustSettingsCopyCertificates(SecTrustSettingsDomain, UnsafeMutablePointer<CFArray?>?) -> OSStatus](sectrustsettingscopycertificates(_:_:).md)
  Obtains an array of all certificates that have trust settings in a specific trust settings domain.
- [func SecTrustSettingsCopyModificationDate(SecCertificate, SecTrustSettingsDomain, UnsafeMutablePointer<CFDate?>) -> OSStatus](sectrustsettingscopymodificationdate(_:_:_:).md)
  Obtains the date and time at which a certificate’s trust settings were last modified.
- [Usage Constraints Dictionary Keys](usage-constraints-dictionary-keys.md)
  Use these trust settings keys in a usage constraints dictionary.
- [func SecTrustSettingsCopyTrustSettings(SecCertificate, SecTrustSettingsDomain, UnsafeMutablePointer<CFArray?>) -> OSStatus](sectrustsettingscopytrustsettings(_:_:_:).md)
  Obtains the trust settings for a certificate.
- [func SecTrustSettingsCreateExternalRepresentation(SecTrustSettingsDomain, UnsafeMutablePointer<CFData?>) -> OSStatus](sectrustsettingscreateexternalrepresentation(_:_:).md)
  Obtains an external, portable representation of the specified domain’s trust settings.
- [func SecTrustSettingsImportExternalRepresentation(SecTrustSettingsDomain, CFData) -> OSStatus](sectrustsettingsimportexternalrepresentation(_:_:).md)
  Imports trust settings into a trust domain.
- [func SecTrustSettingsRemoveTrustSettings(SecCertificate, SecTrustSettingsDomain) -> OSStatus](sectrustsettingsremovetrustsettings(_:_:).md)
  Deletes the trust settings for a certificate.
- [func SecTrustSettingsSetTrustSettings(SecCertificate, SecTrustSettingsDomain, CFTypeRef?) -> OSStatus](sectrustsettingssettrustsettings(_:_:_:).md)
  Specifies trust settings for a certificate.
- [struct SecTrustSettingsKeyUsage](sectrustsettingskeyusage.md)
  Allowed uses for the encryption key in a certificate.
- [enum SecTrustSettingsResult](sectrustsettingsresult.md)
  Trust settings returned in usage constraints dictionaries.
- [enum SecTrustSettingsDomain](sectrustsettingsdomain.md)
  The trust settings domains.
### Legacy Symbols
- [func SecTrustEvaluate(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](sectrustevaluate(_:_:).md)
  Evaluates trust for the specified certificate and policies.
- [func SecTrustEvaluateAsync(SecTrust, dispatch_queue_t?, SecTrustCallback) -> OSStatus](sectrustevaluateasync(_:_:_:).md)
  Evaluates a trust object asynchronously on the specified dispatch queue.
- [typealias SecTrustCallback](sectrustcallback.md)
  A block called with the results of an asynchronous trust evaluation.
- [func SecTrustSetKeychains(SecTrust, CFTypeRef?) -> OSStatus](sectrustsetkeychains(_:_:).md)
  Sets the keychains searched for intermediate certificates when evaluating a trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/trust)*