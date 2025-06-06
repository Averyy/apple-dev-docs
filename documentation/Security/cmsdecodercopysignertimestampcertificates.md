# CMSDecoderCopySignerTimestampCertificates(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns an array containing the certificates from a timestamp response.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMSDecoderCopySignerTimestampCertificates(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ certificateRefs: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Typically, this function returns [`errSecParam`](errsecparam.md) if the CMS message was not signed or `signerIndex` is out of bounds, and returns [`errSecItemNotFound`](errsecitemnotfound.md) if no certificates were found.

#### Discussion

The signature must contain an authenticated timestamp provided by a time stamping authority. Elements of the returned array are of type `SecCertificateRef`. The caller is responsible for releasing the returned array by calling `CFRelease`.

You must call [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) before you call this function.

## Parameters

- `cmsDecoder`: A CMSDecoder reference returned by the   function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the   function to determine the total number of signers for a message.
- `certificateRefs`: The address of a Core Foundation array reference where the resulting array should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignertimestampcertificates(_:_:_:))*