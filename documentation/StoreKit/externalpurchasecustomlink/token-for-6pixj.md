# token(for:)

**Framework**: StoreKit  
**Kind**: method

Returns an external purchase token of the specified token type.

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
static func token(for tokenType: ExternalPurchaseCustomLink.TokenType) async throws -> ExternalPurchaseCustomLink.Token?
```

#### Return Value

Returns an [`ExternalPurchaseCustomLink.Token`](externalpurchasecustomlink/token.md) of the type you specify, or returns `nil` if there isn’t an active token of the specified type. This method throws a [`StoreKitError`](storekiterror.md) if your app isn’t eligible to use this API.

#### Discussion

Use this method to request tokens when your app uses the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API.

The token types you request depend on the region in which your app offers external purchases:

- For external purchases in the European Union (EU), request the `ACQUISITION` and `SERVICES` token types when your app launches, and immediately associate the tokens with a customer account on your server. You can also call this method at any other time, such as before communicating or promoting offers. The method returns a token of either token type until it expires.
- For external purchases in Brazil and Japan, request the [`withinApp`](externalpurchasecustomlink/tokentype/withinapp.md) or [`outOfApp`](externalpurchasecustomlink/tokentype/outofapp.md) token types. Request an [`withinApp`](externalpurchasecustomlink/tokentype/withinapp.md) token type for workflows that use an alternative payment provider inside the app. Request a [`outOfApp`](externalpurchasecustomlink/tokentype/outofapp.md) token type for workflows in which customers can complete transactions on a website, outside of the app. For more information, see [`Payment options on the App Store in Brazil`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-brazil) and [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan), respectively.

The [`withinApp`](externalpurchasecustomlink/tokentype/withinapp.md) and [`outOfApp`](externalpurchasecustomlink/tokentype/outofapp.md) token types for Japan and Brazil are available in iOS 27.2 and later.

> 💡 **Tip**: Request tokens before every potential transaction to ensure you have current tokens.

##### Read and Report Tokens

Decode the token to read its contents, including its expiration date. For more information, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md). For a code example that shows requesting tokens, see [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md).

Report tokens and all transactions associated with the tokens from your server, using the [`External Purchase Server API`](https://developer.apple.com/documentation/externalpurchaseserverapi).

## Parameters

- `tokenType`: The type of token to request.

## See Also

- [ExternalPurchaseCustomLink.TokenType](externalpurchasecustomlink/tokentype.md)
  Values that represent the external purchase token types.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token(for:)-6pixj)*