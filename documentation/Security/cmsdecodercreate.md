# CMSDecoderCreate(_:)

**Framework**: Security  
**Kind**: func

Creates a CMSDecoder reference.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCreate(_ cmsDecoderOut: UnsafeMutablePointer<CMSDecoder?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This is the first function in a sequence of decoder functions that you call to get information from a CMS message. The other functions in the sequence require you to pass in the CMSDecoder reference returned by this function. The next function in the sequence is `CMSDecoderUpdateMessage`.

## Parameters

- `cmsDecoderOut`: On return, points to a CMSDecoder reference. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSDecoderUpdateMessage(CMSDecoder, UnsafeRawPointer, Int) -> OSStatus](cmsdecoderupdatemessage(_:_:_:).md)
  Feeds raw bytes of the message to be decoded into the decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercreate(_:))*