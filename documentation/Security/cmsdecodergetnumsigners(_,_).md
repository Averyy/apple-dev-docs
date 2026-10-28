# CMSDecoderGetNumSigners(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains the number of signers of a message.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderGetNumSigners(_ cmsDecoder: CMSDecoder, _ numSignersOut: UnsafeMutablePointer<Int>) -> OSStatus
```

```c
OSStatus CMSDecoderGetNumSigners(CMSDecoderRef cmsDecoder, size_t *numSignersOut);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

Call the `CMSDecoderCopySignerStatus` function to determine the status of a signature.

You cannot call this function until after you have called the `CMSDecoderFinalizeMessage` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `numSignersOut`: On return, the number of signers of the message. Zero indicates that the message was not signed.

## See Also

### Related Documentation
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodergetnumsigners(_:_:))*