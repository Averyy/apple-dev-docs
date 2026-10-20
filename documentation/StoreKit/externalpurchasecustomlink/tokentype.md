# ExternalPurchaseCustomLink.TokenType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Values that represent the external purchase token types.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct TokenType
```

#### Discussion

Provide a token type value when you call [`token(for:)`](./token%28for%29-6pixj.md).

## Topics

### Token types
- [static let withinApp: ExternalPurchaseCustomLink.TokenType](./tokentype/withinapp.md)
  A token type for workflows that use an alternative payment provider inside the app.
- [static let outOfApp: ExternalPurchaseCustomLink.TokenType](./tokentype/outofapp.md)
  A token type for workflows in which customers complete transactions outside of the app.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting external purchase tokens
- [static func token(for: ExternalPurchaseCustomLink.TokenType) async throws -> ExternalPurchaseCustomLink.Token?](./token%28for%29-6pixj.md)
  Returns an external purchase token of the specified token type.
- [ExternalPurchaseCustomLink.Token](./token.md)
  A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](../receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/tokentype)*