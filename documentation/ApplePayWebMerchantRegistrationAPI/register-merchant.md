# Register Merchant

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Register a merchant and its corresponding set of fully qualified domains.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Mentions

- [Preparing merchant domains for verification](./preparing-merchant-domains-for-verification.md)

#### Discussion

Call this API to register a merchant and their domains. You can register domains in multiple requests. The API has a limit of 99 domain names per `partnerInternalMerchantIdentifier.`

Before making a [`Register Merchant`](./register-merchant.md) request, you must prepare each domain included in the request for verification. For more information on domain verification, see [Preparing merchant domains for verification](./preparing-merchant-domains-for-verification.md).

This request returns no response body for a successful 200 response. Apple Pay servers register the relationship between the e-commerce partner, the merchant, and the merchant’s domains.

> **Note**:  To access the sandbox environment, use `POST` `https://apple-pay-gateway-cert.apple.com/paymentservices/registerMerchant`.

## Endpoint

`POST https://apple-pay-gateway.apple.com/paymentservices/registerMerchant`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RegisterMerchantRequest`

The request body you use to register merchants.

## Responses

- `200` OK: Success.
- `400` Bad Request: The request is malformed or invalid.
- `401` Unauthorized: The e-commerce platform doesn’t have permission to call this API.
- `417` Expectation Failed: The e-commerce platform isn’t registered with Apple Developer.
- `500` Internal Server Error: An internal server error occurred.

## See Also

### Web Merchant Registration
- [Preparing merchant domains for verification](./preparing-merchant-domains-for-verification.md)
  Host a domain verification file on each domain before requesting registration.
- [object RegisterMerchantRequest](./registermerchantrequest.md)
  The request body you use to register merchants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/register-merchant)*