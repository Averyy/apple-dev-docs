# issuerIdentifiers

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Required**: Yes

A list of X.509 authority key identifiers your app accepts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var issuerIdentifiers: [Data] { get set }
```

#### Discussion

An empty list means any document signer certificate is acceptable.

> ⚠️ **Warning**: You can’t have more than 1,000 issuer identifiers, and the size of each identifier can’t exceed 64 bytes. If you don’t meet these conditions, your app terminates.

## See Also

- [var elements: [PKIdentityElement]](pkidentitydocumentdescriptor/elements.md)
  A list of identity elements to request.
- [class PKIdentityElement](pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor/issueridentifiers)*