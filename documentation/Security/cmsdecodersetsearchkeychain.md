# CMSDecoderSetSearchKeychain(_:_:)

**Framework**: Security  
**Kind**: func

Specifies the keychains to search for intermediate certificates to be used in verifying a signed message’s signer certificates.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: CFTypeRef) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If you don’t call this function, the decoder uses the default keychain search list to search for intermediate certificates.

If you do call this function, you must call it before you call the `CMSDecoderCopySignerStatus` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the   function.
- `keychainOrArray`: Either a single keychain to search, specified as a keychain object (type  ), or a set of keychains specified as a   of keychain objects. If you specify an empty  , no keychains are searched for intermediate certificates.

## See Also

- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](cmsdecodercreate(_:).md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodersetsearchkeychain(_:_:))*