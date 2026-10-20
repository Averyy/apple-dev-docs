# CMSDecoderSetSearchKeychain(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies the keychains to search for intermediate certificates to be used in verifying a signed message’s signer certificates.

**Availability**:
- macOS 10.5+ - Deprecated in 10.13 (renamed: SecKeychainSetSearchList(_:))

## Declaration

```swift
func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: CFTypeRef) -> OSStatus
```

```c
OSStatus CMSDecoderSetSearchKeychain(CMSDecoderRef cmsDecoder, CFTypeRef keychainOrArray);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

If you don’t call this function, the decoder uses the default keychain search list to search for intermediate certificates.

If you do call this function, you must call it before you call the `CMSDecoderCopySignerStatus` function.

## Parameters

- `cmsDecoder`: The CMSDecoder reference returned by the `CMSDecoderCreate` function.
- `keychainOrArray`: Either a single keychain to search, specified as a keychain object (type `SecKeychainRef`), or a set of keychains specified as a `CFArray` of keychain objects. If you specify an empty `CFArrayRef`, no keychains are searched for intermediate certificates.

## See Also

### Related Documentation
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodersetsearchkeychain(_:_:))*