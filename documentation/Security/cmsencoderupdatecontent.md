# CMSEncoderUpdateContent(_:_:_:)

**Framework**: Security  
**Kind**: func

Feeds content bytes into the encoder.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafeRawPointer, _ contentLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

You use this function to add the content that is to be signed or encrypted. If the message is only a container for certificates added with the [`CMSEncoderAddSupportingCerts(_:_:)`](cmsencoderaddsupportingcerts(_:_:).md) function and has no other content, do not call this function. This function can be called multiple times.

After you are finished adding content, call the `CMSEncoderCopyEncodedContent` function to complete the message creation process.

None of the setter functions ([`CMSEncoderSetHasDetachedContent(_:_:)`](cmsencodersethasdetachedcontent(_:_:).md), [`CMSEncoderSetEncapsulatedContentType`](cmsencodersetencapsulatedcontenttype.md), or [`CMSEncoderSetCertificateChainMode(_:_:)`](cmsencodersetcertificatechainmode(_:_:).md)) can be called after this function has been called.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the   function.
- `content`: The content that you want to add to the message. The content must conform to the type set with the   function (or type   if that function has not been called).
- `contentLen`: The length of the content being added, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderupdatecontent(_:_:_:))*