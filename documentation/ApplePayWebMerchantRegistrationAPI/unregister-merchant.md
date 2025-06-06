# Unregister Merchant

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: httpRequest

Unregister one or more domains associated with a previously registered merchant.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

#### Discussion

Only request to unregister merchants for domains you previously registered using the [`Register Merchant`](register-merchant.md) API.

If you pass a subset of the merchant’s registered domains, Apple Pay server unregisters only those domains and the merchant remains active. If you unregister a merchant’s last-remaining registered domain, Apple Pay servers delete the merchant’s registration.

> **Note**:  To access the sandbox environment, use `POST https://apple-pay-gateway-cert.apple.com/paymentservices/unregisterMerchant`.

 To access the sandbox environment, use `POST https://apple-pay-gateway-cert.apple.com/paymentservices/unregisterMerchant`.

## Request Body

The request body for unregistering merchants.

## See Also

- [object UnregisterMerchantRequest](unregistermerchantrequest.md)
  The request body you use to unregister one or more merchant domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregister-merchant)*