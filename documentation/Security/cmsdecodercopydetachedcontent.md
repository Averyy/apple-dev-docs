# CMSDecoderCopyDetachedContent(_:_:)

**Framework**: Security  
**Kind**: func

Obtains the detached content specified with the `CMSDecoderSetDetachedContent` function.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderCopyDetachedContent(_ cmsDecoder: CMSDecoder, _ detachedContentOut: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `detachedContentOut`: On return, points to the data reference specified by an earlier call to the   function. Returns a NULL data reference if no detached content has been specified. You must use the   function to free this reference when you are finished using it.

## See Also

- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopydetachedcontent(_:_:))*