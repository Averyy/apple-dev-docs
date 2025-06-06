# Invalidate a Merchant Token

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Invalidate a merchant token associated with your merchant identifier, making it invalid for future transaction authorizations.

**Availability**:
- App Store Connect API 1.0.10+

#### Discussion

When you call this endpoint, Apple Pay server unlinks — invalidates — the merchant token, and the token is no longer valid for future transaction authorizations. Call this endpoint in the following cases:

- Someone cancels a recurring transaction on your website or in your app that uses this merchant token
- Someone changes the payment method for a recurring transactions, for example, they stop using Apple Pay for the transaction

## Request Body

The request body you use to specify the merchant token that Apple Pay should invalidate.

## See Also

- [object MerchantTokenUnlinkRequest](merchanttokenunlinkrequest.md)
  The request body you use to invalidate a merchant token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/unlinking-merchanttoken)*