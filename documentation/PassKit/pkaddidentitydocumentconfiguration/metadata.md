# metadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A set of configurable metadata that defines the required information to add the corresponding pass to Wallet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
var metadata: PKIdentityDocumentMetadata { get }
```

## See Also

- [class func forMetadata(PKIdentityDocumentMetadata, completion: (PKAddIdentityDocumentConfiguration?, (any Error)?) -> Void)](pkaddidentitydocumentconfiguration/formetadata(_:completion:).md)
  Returns the identity document configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddidentitydocumentconfiguration/metadata)*