# isValidAuthenticationCode(_:authenticating:using:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func isValidAuthenticationCode(_ mac: HMAC<H>.MAC, authenticating bufferPointer: UnsafeRawBufferPointer, using key: SymmetricKey) -> Bool
```

#### Return Value

A Boolean value that’s `true` if the message authentication code is valid for the data within the specified buffer.

## Parameters

- `mac`: The authentication code to compare.
- `bufferPointer`: A pointer to the block of data to compare.
- `key`: The symmetric key for the authentication code.

## See Also

### Checking an authentication code
- [static func isValidAuthenticationCode<D>(HMAC<H>.MAC, authenticating: D, using: SymmetricKey) -> Bool](./isvalidauthenticationcode%28_,authenticating,using%29-8ezmw.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.
- [static func isValidAuthenticationCode<C, D>(C, authenticating: D, using: SymmetricKey) -> Bool](./isvalidauthenticationcode%28_,authenticating,using%29-5ilt9.md)
  Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-5jbc8)*