# CMSDecoderCopySignerTimestamp(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the timestamp of a signer of a CMS message, if present.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMSDecoderCopySignerTimestamp(_ cmsDecoder: CMSDecoder, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

```c
OSStatus CMSDecoderCopySignerTimestamp(CMSDecoderRef cmsDecoder, size_t signerIndex, CFAbsoluteTime *timestamp);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). Typically, this function returns [`errSecParam`](./errsecparam.md) if the CMS message was not signed or if `signerIndex` is out of bounds.

## Discussion

This timestamp is an authenticated timestamp provided by a time stamping authority.

You must call [`CMSDecoderFinalizeMessage(_:)`](./cmsdecoderfinalizemessage%28_%29.md) before you call this function.

## Parameters

- `cmsDecoder`: A CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) function to determine the total number of signers for a message.
- `timestamp`: The address of an absolute time value where the result should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignertimestamp(_:_:_:))*