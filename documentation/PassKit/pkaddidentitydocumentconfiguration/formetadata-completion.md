# forMetadata(_:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns the identity document configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
class func forMetadata(_ metadata: PKIdentityDocumentMetadata) async throws -> PKAddIdentityDocumentConfiguration
```

## Parameters

- `metadata`: The configurable metadata that defines the required information to add the corresponding pass to Wallet.
- `completion`: Returns the identity document configration.

## See Also

- [var metadata: PKIdentityDocumentMetadata](pkaddidentitydocumentconfiguration/metadata.md)
  A set of configurable metadata that defines the required information to add the corresponding pass to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddidentitydocumentconfiguration/formetadata(_:completion:))*