# open(inplace:using:nonce:tag:authenticating:)

**Framework**: Apple CryptoKit  
**Kind**: method

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
static func open(inplace message: inout MutableRawSpan, using key: SymmetricKey, nonce: RawSpan, tag: RawSpan, authenticating authenticatedData: RawSpan? = nil) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/open(inplace:using:nonce:tag:authenticating:))*