# Trust

**Framework**: Security  
**Role**: API Collection

Evaluate trust based on a given policy.

## Overview

Before using a certificate, you evaluate its trustworthiness for a particular purpose.

If you know that a certificate comes unaltered from its sender, you can be confident that its embedded public key does as well. You can also take at face value claims made by the certificate about when and for what purpose the public key may be used. You can securely engage in the operations described in [Using Keys for Encryption](./using-keys-for-encryption.md) and [Signing and Verifying](./signing-and-verifying.md) without prior arrangement between sender and receiver.

## Topics

### Essentials
- [Creating a Trust Object](./creating-a-trust-object.md)
  Construct a trust object from a certificate and a policy.
- [func SecTrustCreateWithCertificates(CFTypeRef, CFTypeRef?, UnsafeMutablePointer<SecTrust?>) -> OSStatus](./sectrustcreatewithcertificates%28_,_,_%29.md)
  Creates a trust management object based on certificates and policies.
- [class SecTrust](./sectrust.md)
  An object used to evaluate trust.
- [func SecTrustGetTypeID() -> CFTypeID](./sectrustgettypeid%28%29.md)
  Returns the unique identifier of the opaque type to which a trust object belongs.
### Trust Evaluation
- [Evaluating a Trust and Parsing the Result](./evaluating-a-trust-and-parsing-the-result.md)
  Learn what to expect when evaluating a trust object.
- [func SecTrustEvaluateWithError(SecTrust, UnsafeMutablePointer<CFError?>?) -> Bool](./sectrustevaluatewitherror%28_,_%29.md)
  Evaluates trust for the specified certificate and policies.
- [func SecTrustEvaluateAsyncWithError(SecTrust, dispatch_queue_t, SecTrustWithErrorCallback) -> OSStatus](./sectrustevaluateasyncwitherror%28_,_,_%29.md)
  Evaluates a trust object asynchronously on the specified dispatch queue.
- [typealias SecTrustWithErrorCallback](./sectrustwitherrorcallback.md)
  A block called with the results of an asynchronous trust evaluation.
### Trust Evaluation Result
- [Discovering Why a Trust Evaluation Failed](./discovering-why-a-trust-evaluation-failed.md)
  Determine whether you can recover from a failed trust evaluation.
- [func SecTrustGetTrustResult(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](./sectrustgettrustresult%28_,_%29.md)
  Returns the result code from the most recent trust evaluation.
- [enum SecTrustResultType](./sectrustresulttype.md)
  Trust evaluation result codes.
- [func SecTrustCopyResult(SecTrust) -> CFDictionary?](./sectrustcopyresult%28_%29.md)
  Returns a dictionary containing information about an evaluated trust.
- [Trust Result Dictionary Keys](./trust-result-dictionary-keys.md)
  Recognize the keys that appear in a dictionary containing information about an evaluated certification chain.
### Trust Components
- [func SecTrustCopyPublicKey(SecTrust) -> SecKey?](./sectrustcopypublickey%28_%29.md)
  Returns the public key for a leaf certificate after it has been evaluated.
- [func SecTrustGetCertificateCount(SecTrust) -> CFIndex](./sectrustgetcertificatecount%28_%29.md)
  Returns the number of certificates in an evaluated certificate chain.
- [func SecTrustGetCertificateAtIndex(SecTrust, CFIndex) -> SecCertificate?](./sectrustgetcertificateatindex%28_,_%29.md)
  Returns a specific certificate from the certificate chain used to evaluate trust.
- [func SecTrustGetVerifyTime(SecTrust) -> CFAbsoluteTime](./sectrustgetverifytime%28_%29.md)
  Gets the absolute time against which the certificates in a trust management object are verified.
- [func SecTrustCopyAnchorCertificates(UnsafeMutablePointer<CFArray?>) -> OSStatus](./sectrustcopyanchorcertificates%28_%29.md)
  Retrieves the anchor (root) certificates stored by macOS.
- [func SecTrustCopyCustomAnchorCertificates(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sectrustcopycustomanchorcertificates%28_,_%29.md)
  Retrieves the custom anchor certificates, if any, used by a given trust.
- [func SecTrustCopyExceptions(SecTrust) -> CFData?](./sectrustcopyexceptions%28_%29.md)
  Returns an opaque cookie containing exceptions to trust policies that will allow future evaluations of the current certificate to succeed.
- [func SecTrustCopyPolicies(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sectrustcopypolicies%28_,_%29.md)
  Retrieves the policies used by a given trust management object.
- [func SecTrustCopyProperties(SecTrust) -> CFArray?](./sectrustcopyproperties%28_%29.md)
  Returns an array containing the properties of a trust object.
### Advanced Trust Configuation
- [Configuring a Trust](./configuring-a-trust.md)
  Work around a recoverable trust failure.
- [func SecTrustSetVerifyDate(SecTrust, CFDate) -> OSStatus](./sectrustsetverifydate%28_,_%29.md)
  Sets the date and time against which the certificates in a trust management object are verified.
- [func SecTrustSetAnchorCertificates(SecTrust, CFArray?) -> OSStatus](./sectrustsetanchorcertificates%28_,_%29.md)
  Sets the anchor certificates used when evaluating a trust management object.
- [func SecTrustSetAnchorCertificatesOnly(SecTrust, Bool) -> OSStatus](./sectrustsetanchorcertificatesonly%28_,_%29.md)
  Reenables trusting built-in anchor certificates.
- [func SecTrustSetExceptions(SecTrust, CFData?) -> Bool](./sectrustsetexceptions%28_,_%29.md)
  Sets a list of exceptions that should be ignored when the certificate is evaluated.
- [func SecTrustSetPolicies(SecTrust, CFTypeRef) -> OSStatus](./sectrustsetpolicies%28_,_%29.md)
  Sets the policies to use in an evaluation.
- [func SecTrustSetOptions(SecTrust, SecTrustOptionFlags) -> OSStatus](./sectrustsetoptions%28_,_%29.md)
  Sets option flags for customizing evaluation of a trust object.
- [struct SecTrustOptionFlags](./sectrustoptionflags.md)
  The option flags used to condition a trust evaluation.
- [func SecTrustGetNetworkFetchAllowed(SecTrust, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./sectrustgetnetworkfetchallowed%28_,_%29.md)
  Indicates whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [func SecTrustSetNetworkFetchAllowed(SecTrust, Bool) -> OSStatus](./sectrustsetnetworkfetchallowed%28_,_%29.md)
  Specifies whether a trust evaluation is permitted to fetch missing intermediate certificates from the network.
- [func SecTrustSetOCSPResponse(SecTrust, CFTypeRef?) -> OSStatus](./sectrustsetocspresponse%28_,_%29.md)
  Attaches Online Certificate Status Protocol (OSCP) response data to a trust object.
- [func SecTrustSetSignedCertificateTimestamps(SecTrust, CFArray?) -> OSStatus](./sectrustsetsignedcertificatetimestamps%28_,_%29.md)
  Attaches signed certificate timestamp data to a trust object.
### Trust Settings
- [func SecTrustSettingsCopyCertificates(SecTrustSettingsDomain, UnsafeMutablePointer<CFArray?>?) -> OSStatus](./sectrustsettingscopycertificates%28_,_%29.md)
  Obtains an array of all certificates that have trust settings in a specific trust settings domain.
- [func SecTrustSettingsCopyModificationDate(SecCertificate, SecTrustSettingsDomain, UnsafeMutablePointer<CFDate?>) -> OSStatus](./sectrustsettingscopymodificationdate%28_,_,_%29.md)
  Obtains the date and time at which a certificate’s trust settings were last modified.
- [Usage Constraints Dictionary Keys](./usage-constraints-dictionary-keys.md)
  Use these trust settings keys in a usage constraints dictionary.
- [func SecTrustSettingsCopyTrustSettings(SecCertificate, SecTrustSettingsDomain, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sectrustsettingscopytrustsettings%28_,_,_%29.md)
  Obtains the trust settings for a certificate.
- [func SecTrustSettingsCreateExternalRepresentation(SecTrustSettingsDomain, UnsafeMutablePointer<CFData?>) -> OSStatus](./sectrustsettingscreateexternalrepresentation%28_,_%29.md)
  Obtains an external, portable representation of the specified domain’s trust settings.
- [func SecTrustSettingsImportExternalRepresentation(SecTrustSettingsDomain, CFData) -> OSStatus](./sectrustsettingsimportexternalrepresentation%28_,_%29.md)
  Imports trust settings into a trust domain.
- [func SecTrustSettingsRemoveTrustSettings(SecCertificate, SecTrustSettingsDomain) -> OSStatus](./sectrustsettingsremovetrustsettings%28_,_%29.md)
  Deletes the trust settings for a certificate.
- [func SecTrustSettingsSetTrustSettings(SecCertificate, SecTrustSettingsDomain, CFTypeRef?) -> OSStatus](./sectrustsettingssettrustsettings%28_,_,_%29.md)
  Specifies trust settings for a certificate.
- [struct SecTrustSettingsKeyUsage](./sectrustsettingskeyusage.md)
  Allowed uses for the encryption key in a certificate.
- [enum SecTrustSettingsResult](./sectrustsettingsresult.md)
  Trust settings returned in usage constraints dictionaries.
- [enum SecTrustSettingsDomain](./sectrustsettingsdomain.md)
  The trust settings domains.
- [kSecTrustSettingsDefaultRootCertSetting](./ksectrustsettingsdefaultrootcertsetting.md)
  A value indicating the default root certificate trust settings when used as a certificate object in a trust settings API function.
### Legacy Symbols
- [func SecTrustEvaluate(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](./sectrustevaluate%28_,_%29.md)
  Evaluates trust for the specified certificate and policies.
- [func SecTrustEvaluateAsync(SecTrust, dispatch_queue_t?, SecTrustCallback) -> OSStatus](./sectrustevaluateasync%28_,_,_%29.md)
  Evaluates a trust object asynchronously on the specified dispatch queue.
- [typealias SecTrustCallback](./sectrustcallback.md)
  A block called with the results of an asynchronous trust evaluation.
- [func SecTrustSetKeychains(SecTrust, CFTypeRef?) -> OSStatus](./sectrustsetkeychains%28_,_%29.md)
  Sets the keychains searched for intermediate certificates when evaluating a trust management object.
- [SecTrustUserSetting](./sectrustusersetting.md)
  Represents user-specified trust settings.
- [SecTrustSetParameters](./sectrustsetparameters.md)
  Sets the action and action data for a trust management object.
- [SecTrustGetCssmResult](./sectrustgetcssmresult.md)
  Retrieves the CSSM trust result.
- [SecTrustGetCssmResultCode](./sectrustgetcssmresultcode.md)
  Retrieves the CSSM result code from the most recent trust evaluation for a trust management object.
- [SecTrustGetTPHandle](./sectrustgettphandle.md)
  Retrieves the trust policy handle.
- [SecTrustGetResult](./sectrustgetresult.md)
  Retrieves details on the outcome of a call to the function `SecTrustEvaluate`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/trust)*