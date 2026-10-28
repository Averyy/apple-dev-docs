# CMSEncoderUpdateContent(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Feeds content bytes into the encoder.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderUpdateContent(_ cmsEncoder: CMSEncoder, _ content: UnsafeRawPointer, _ contentLen: Int) -> OSStatus
```

```c
OSStatus CMSEncoderUpdateContent(CMSEncoderRef cmsEncoder, const void *content, size_t contentLen);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

You use this function to add the content that is to be signed or encrypted. If the message is only a container for certificates added with the [`CMSEncoderAddSupportingCerts(_:_:)`](./cmsencoderaddsupportingcerts%28_,_%29.md) function and has no other content, do not call this function. This function can be called multiple times.

After you are finished adding content, call the `CMSEncoderCopyEncodedContent` function to complete the message creation process.

None of the setter functions ([`CMSEncoderSetHasDetachedContent(_:_:)`](./cmsencodersethasdetachedcontent%28_,_%29.md), [`CMSEncoderSetEncapsulatedContentType`](./cmsencodersetencapsulatedcontenttype.md), or [`CMSEncoderSetCertificateChainMode(_:_:)`](./cmsencodersetcertificatechainmode%28_,_%29.md)) can be called after this function has been called.

## Parameters

- `cmsEncoder`: The CMSEncoder reference returned by the `CMSEncoderCreate` function.
- `content`: The content that you want to add to the message. The content must conform to the type set with the [`CMSEncoderSetEncapsulatedContentType`](./cmsencodersetencapsulatedcontenttype.md) function (or type `id-data` if that function has not been called).
- `contentLen`: The length of the content being added, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencoderupdatecontent(_:_:_:))*