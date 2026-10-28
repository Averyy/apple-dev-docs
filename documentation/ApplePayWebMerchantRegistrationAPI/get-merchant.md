# Get Merchant Details

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve information about a registered merchant’s current state by using the merchant’s internal merchant identifier.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Discussion

Get information about a merchant you previously registered. You provide the merchant’s unique identifier (`partnerInternalMerchantIdentifier`). A succesful response contains a [`MerchantDetails`](./merchantdetails.md) object in the response body.

## Endpoint

`GET https://apple-pay-gateway.apple.com/paymentservices/merchant/${partnerInternalMerchantIdentifier}`

## Parameters

### Path Parameters

- `partnerInternalMerchantIdentifier` (string) *(required)*: A unique identifier for the merchant that the e-commerce partner created and used in the [`Register Merchant`](./register-merchant.md) request.

  **Maximum Length**: `1024`; **Allowed Values**: `/a-zA-Z0-9~-_+&@$!|,.;/`

## Responses

- `200` OK (`MerchantDetails`, `application/json`): Success. The response contains an object with information for the registered merchant.
- `400` Bad Request: The request is malformed or invalid, or the merchant isn’t registered.
- `401` Unauthorized: The e-commerce platform doesn’t have permission to call this API.
- `417` Expectation Failed: The e-commerce platform isn’t registered with Apple Developer.
- `500` Internal Server Error: An internal server error occurred.

## See Also

### Web Merchant Details
- [object MerchantDetails](./merchantdetails.md)
  Detailed information for a single registered merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/get-merchant)*