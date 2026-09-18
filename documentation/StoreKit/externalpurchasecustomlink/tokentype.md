# ExternalPurchaseCustomLink.TokenType

**Framework**: StoreKit  
**Kind**: struct

Values that represent the external purchase token types.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
struct TokenType
```

#### Discussion

Provide a token type value when you call [`token(for:)`](externalpurchasecustomlink/token(for:)-6pixj.md).

## Topics

### Token types
- [static let withinApp: ExternalPurchaseCustomLink.TokenType](externalpurchasecustomlink/tokentype/withinapp.md)
  A token type for workflows that use an alternative payment provider inside the app.
- [static let outOfApp: ExternalPurchaseCustomLink.TokenType](externalpurchasecustomlink/tokentype/outofapp.md)
  A token type for workflows in which customers complete transactions outside of the app.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static func token(for: ExternalPurchaseCustomLink.TokenType) async throws -> ExternalPurchaseCustomLink.Token?](externalpurchasecustomlink/token(for:)-6pixj.md)
  Returns an external purchase token of the specified token type.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/tokentype)*