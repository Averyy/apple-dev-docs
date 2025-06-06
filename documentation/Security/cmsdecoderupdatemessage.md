# CMSDecoderUpdateMessage(_:_:_:)

**Framework**: Security  
**Kind**: func

Feeds raw bytes of the message to be decoded into the decoder.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderUpdateMessage(_ cmsDecoder: CMSDecoder, _ msgBytes: UnsafeRawPointer, _ msgBytesLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). Returns [`errSecUnknownFormat`](errsecunknownformat.md) upon detection of an improperly formatted CMS message.

#### Discussion

This function can be called multiple times. Call the `CMSDecoderFinalizeMessage` function when you have no more data to decode.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `msgBytes`: A pointer to the data to be decoded.
- `msgBytesLen`: The length of the data, in bytes.

## See Also

- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecoderupdatemessage(_:_:_:))*