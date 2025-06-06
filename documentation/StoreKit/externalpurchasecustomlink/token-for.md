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

#### Return Value

Returns an external purchase token of the type you specify, or returns `nil` if there isn’t an active token of the specified type. This method throws an error if your app isn’t eligible to use this API.

#### Discussion

Use this method if your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key.

Request both token types when your app launches and immediately associate the tokens with a customer account on your server. You can also call this method at any other time, such as before offering external purchases. The method returns the same token, of each type, until it expires.

Decode the token to read its contents, including the expiration date. For more information, see [`Receiving and decoding external purchase tokens`](receiving-and-decoding-external-purchase-tokens.md). For a code example that shows requesting the tokens, see [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md).

Report tokens and all transactions associated with the tokens from your server, using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

## Parameters

- `tokenType`: A string that indicates the token type. Valid string values are:  , 

## See Also

- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  An external purchase token for use with custom links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token(for:))*