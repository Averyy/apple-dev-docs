# token(for:)

**Framework**: StoreKit  
**Kind**: method

Requests an external purchase token of the specified type.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
static func token(for tokenType: String) async throws -> ExternalPurchaseCustomLink.Token?
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)

#### Return Value

Returns an external purchase token of the type you specify, or returns `nil` if there isn’t an active token of the specified type. This method throws an error if your app isn’t eligible to use this API.

#### Discussion

Use this method to request tokens when your app uses the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API. Request the `ACQUISITION` and `SERVICES` token types when your app launches and immediately associate the tokens with a customer account on your server. You can also call this method at any other time, such as before communicating or promoting offers. The method returns the token, of each type, until it expires.

> 💡 **Tip**: Request a token before every potential transaction to ensure you have a current token.

##### Read and Report Tokens

Decode the token to read its contents, including its expiration date. For more information, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md). For a code example that shows requesting tokens, see [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md).

Report tokens and all transactions associated with the tokens from your server, using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

## Parameters

- `tokenType`: A string that indicates the token type. Valid string values are:  , 

## See Also

- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token(for:))*