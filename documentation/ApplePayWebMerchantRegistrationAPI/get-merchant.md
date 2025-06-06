# Get Merchant Details

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: httpRequest

Retrieve information about a registered merchant’s current state by using the merchant’s internal merchant identifier.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

#### Discussion

Get information about a merchant you previously registered. You provide the merchant’s unique identifier (`partnerInternalMerchantIdentifier`). A succesful response contains a [`MerchantDetails`](merchantdetails.md) object in the response body.

## See Also

- [object MerchantDetails](merchantdetails.md)
  Detailed information for a single registered merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/get-merchant)*