# CMSDecoderCopySignerStatus(_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Obtains the status of a CMS message’s signature.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopySignerStatus(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ policyOrArray: CFTypeRef, _ evaluateSecTrust: Bool, _ signerStatusOut: UnsafeMutablePointer<CMSSignerStatus>?, _ secTrustOut: UnsafeMutablePointer<SecTrust?>?, _ certVerifyResultCodeOut: UnsafeMutablePointer<OSStatus>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). A result of [`errSecSuccess`](errsecsuccess.md) indicates only that the function completed successfully; it does not indicate that the signature is verified or the certificates are valid. See the `signerStatusOut` and `certVerifyResultCodeOut` parameters for the verification and certificate validation results.

#### Discussion

You cannot call this function until after you have called the [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) function. Although the message has been fully decoded when the [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) function returns with no error, the signature can’t be validated or certificates verified until this function is called.

A CMS message can be signed by multiple signers; this function returns the status associated with one signer as specified by the `signerIndex` parameter.

If you both pass in [`false`](https://developer.apple.com/documentation/Swift/false) for the `evaluateSecTrust` parameter and `NULL` for the `secTrustOut` parameter, no evaluation of the signer certificate can occur.

## Parameters

- `cmsDecoder`: The   reference returned by the   function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the   function to determine the total number of signers for a message.
- `policyOrArray`: The trust policy or policies to be used to verify the signer’s certificate. You can specify either a single   instance or a   of   instances. For more information about policy objects, see  .
- `evaluateSecTrust`: Set to   to cause the decoder to call the   function to evaluate the   instance created for the evaluation of the signer certificate. Set to   if you intend to call the   function for the   instance returned by the   parameter.
- `signerStatusOut`: If you specify   for the   parameter, on return this parameter indicates the status of the signature. See   for possible results. Pass in   if you don’t want a value returned.
- `secTrustOut`: On return this parameter points to a   instance. If you specified   for the   parameter, this is the trust instance that was used to verify the signer’s certificate. If you specified   for the   parameter, you can call the   function to evaluate the   instance. Pass   if you do not want this instance returned. You must use the   function to free this reference when you are finished using it.
- `certVerifyResultCodeOut`: Some of the most common results returned in this parameter include:

## See Also

- [func SecTrustEvaluate(SecTrust, UnsafeMutablePointer<SecTrustResultType>) -> OSStatus](sectrustevaluate(_:_:).md)
  Evaluates trust for the specified certificate and policies.
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](cmsdecoderfinalizemessage(_:).md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignerstatus(_:_:_:_:_:_:_:))*