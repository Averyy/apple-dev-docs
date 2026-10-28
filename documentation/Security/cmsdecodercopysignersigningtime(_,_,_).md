# CMSDecoderCopySignerSigningTime(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the signing time of a CMS message, if present.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMSDecoderCopySignerSigningTime(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ signingTime: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

```c
OSStatus CMSDecoderCopySignerSigningTime(CMSDecoderRef cmsDecoder, size_t signerIndex, CFAbsoluteTime *signingTime);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). Typically, this function returns [`errSecParam`](./errsecparam.md) if the CMS message was not signed or if `signerIndex` is out of bounds.

## Discussion

The timestamp is an unauthenticated time, although it is part of the signed attributes of the message.

You must call [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) before you call this function.

## Parameters

- `cmsDecoder`: A CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) function to determine the total number of signers for a message.
- `signingTime`: The address of an absolute time value where the result should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignersigningtime(_:_:_:))*