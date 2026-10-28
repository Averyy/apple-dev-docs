# CMSDecoderCopySignerStatus(_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the status of a CMS message’s signature.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ policyOrArray: CFTypeRef, _ evaluateSecTrust: Bool, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>?, _ secTrustOut: UnsafeMutablePointer<SecTrust?>?, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>?) -> OSStatus
```

```c
OSStatus CMSDecoderCopySignerStatus(CMSDecoderRef cmsDecoder, size_t signerIndex, CFTypeRef policyOrArray, Boolean evaluateSecTrust, CMSSignerStatus *signerStatusOut, SecTrustRef*secTrustOut, OSStatus *certVerifyResultCodeOut);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). A result of [`errSecSuccess`](./errsecsuccess.md) indicates only that the function completed successfully; it does not indicate that the signature is verified or the certificates are valid. See the `signerStatusOut` and `certVerifyResultCodeOut` parameters for the verification and certificate validation results.

## Discussion

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) function. Although the message has been fully decoded when the [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) function returns with no error, the signature can’t be validated or certificates verified until this function is called.

A CMS message can be signed by multiple signers; this function returns the status associated with one signer as specified by the `signerIndex` parameter.

If you both pass in [`false`](../Swift/false.md) for the `evaluateSecTrust` parameter and `NULL` for the `secTrustOut` parameter, no evaluation of the signer certificate can occur.

## Parameters

- `cmsDecoder`: The [`CMSDecoder`](./cmsdecoder.md) reference returned by the [`CMSDecoderCreate(_:)`](./cmsdecodercreate%28_%29.md) function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) function to determine the total number of signers for a message.
- `policyOrArray`: The trust policy or policies to be used to verify the signer’s certificate. You can specify either a single [`SecPolicy`](./secpolicy.md) instance or a [`CFArray`](../CoreFoundation/cfarray.md) of [`SecPolicy`](./secpolicy.md) instances. For more information about policy objects, see [Policies](./policies.md).
- `evaluateSecTrust`: Set to [`true`](../Swift/true.md) to cause the decoder to call the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function to evaluate the [`SecTrust`](./sectrust.md) instance created for the evaluation of the signer certificate. Set to [`false`](../Swift/false.md) if you intend to call the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function for the [`SecTrust`](./sectrust.md) instance returned by the `secTrustOut` parameter.
- `signerStatusOut`: If you specify [`true`](../Swift/true.md) for the `evaluateSecTrust` parameter, on return this parameter indicates the status of the signature. See [`CMSSignerStatus`](./cmssignerstatus.md) for possible results. Pass in `NULL` if you don’t want a value returned.
- `secTrustOut`: On return this parameter points to a [`SecTrust`](./sectrust.md) instance. If you specified [`true`](../Swift/true.md) for the `evaluateTrust` parameter, this is the trust instance that was used to verify the signer’s certificate. If you specified [`false`](../Swift/false.md) for the `evaluateTrust` parameter, you can call the [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) function to evaluate the [`SecTrust`](./sectrust.md) instance. Pass `NULL` if you do not want this instance returned. You must use the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free this reference when you are finished using it.
- `certVerifyResultCodeOut`: If you specify [`true`](../Swift/true.md) for the `evaluateSecTrust` parameter, on return this parameter indicates the result of the certificate verification.  Pass in `NULL` if you don’t want a value returned.

  Some of the most common results returned in this parameter include:

  - **`CSSMERR_TP_INVALID_ANCHOR_CERT`**: The certificate was verified through the certificate chain to a self-signed root certificate that was present in the message, but that root certificate is not a known, trusted root certificate.
  - **`CSSMERR_TP_NOT_TRUSTED`**: The certificate could not be verified back to a root certificate.
  - **`CSSMERR_TP_VERIFICATION_FAILURE`**: The root certificate failed verification.
  - **`CSSMERR_TP_VERIFY_ACTION_FAILED`**: Trust could not be established according to the specified trust policy.
  - **`CSSMERR_TP_INVALID_CERTIFICATE`**: The signer’s leaf certificate was not valid.
  - **`CSSMERR_TP_CERT_EXPIRED`**: A certificate in the chain was expired at the time of verification.
  - **`CSSMERR_TP_CERT_NOT_VALID_YET`**: A certificate in the chain was not yet valid at the time of verification.

## See Also

### Related Documentation
- [func SecTrustEvaluate(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](./sectrustevaluate%28_,_%29.md)
  Evaluates trust for the specified certificate and policies.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignerstatus(_:_:_:_:_:_:_:))*