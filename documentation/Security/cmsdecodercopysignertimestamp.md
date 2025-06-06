# CMSDecoderCopySignerTimestamp(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns the timestamp of a signer of a CMS message, if present.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Typically, this function returns [`errSecParam`](errsecparam.md) if the CMS message was not signed or if `signerIndex` is out of bounds.

#### Discussion

This timestamp is an authenticated timestamp provided by a time stamping authority.

You must call [`CMSDecoderFinalizeMessage(_:)`](cmsdecoderfinalizemessage(_:).md) before you call this function.

## Parameters

- `cmsDecoder`: A CMSDecoder reference returned by the   function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the   function to determine the total number of signers for a message.
- `timestamp`: The address of an absolute time value where the result should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignertimestamp(_:_:_:))*