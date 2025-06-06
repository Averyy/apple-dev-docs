# CMSEncoderCopyEncodedContent(_:_:)

**Framework**: Security  
**Kind**: func

Finishes encoding the message and obtains the encoded result.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCopyEncodedContent(_ cmsEncoder: CMSEncoder, _ encodedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This is the last function in the sequence of encoding functions you call when creating a signed or encrypted message. In many cases, you can call the `CMSEncode` function alone instead of using the sequence of encoding functions.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `encodedContentOut`: On return, points to the encoded message. You must use the   function to free this reference when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopyencodedcontent(_:_:))*