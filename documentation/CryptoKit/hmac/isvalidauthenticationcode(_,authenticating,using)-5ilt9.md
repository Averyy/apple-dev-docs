# isValidAuthenticationCode(_:authenticating:using:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.

**Availability**:
- iOS 13.2+
- iPadOS 13.2+
- Mac Catalyst 13.2+
- macOS 10.15+
- tvOS 13.2+
- visionOS 1.0+
- watchOS 6.1+

## Declaration

```swift
static func isValidAuthenticationCode<C, D>(_ authenticationCode: C, authenticating authenticatedData: D, using key: SymmetricKey) -> Bool where C : ContiguousBytes, D : DataProtocol
```

## Return Value

A Boolean value that’s `true` if the message authentication code is valid for the specified block of data.

## Parameters

- `authenticationCode`: The authentication code to compare.
- `authenticatedData`: The block of data to compare.
- `key`: The symmetric key for the authentication code.

## See Also

### Checking an authentication code
- [static func isValidAuthenticationCode<D>(HMAC<H>.MAC, authenticating: D, using: SymmetricKey) -> Bool](./isvalidauthenticationcode%28_,authenticating,using%29-8ezmw.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.
- [static func isValidAuthenticationCode(HMAC<H>.MAC, authenticating: UnsafeRawBufferPointer, using: SymmetricKey) -> Bool](./isvalidauthenticationcode%28_,authenticating,using%29-5jbc8.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-5ilt9)*