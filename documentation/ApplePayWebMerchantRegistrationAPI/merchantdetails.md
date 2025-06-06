# MerchantDetails

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: dictionary

Detailed information for a single registered merchant.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Declaration

```swift
object MerchantDetails
```

#### Discussion

To compare your merchant ID with the value that this request returns in the `encryptTo` string, create a SHA-256 hash of your merchant ID first. In the Terminal app, enter the following command, replacing `com.your.merchant.id` with your merchant ID:

```other
echo -n com.your.merchant.id | openssl dgst -sha256
```

The result is a hexidecimal value that you can compare with the value that this request returns in the `encryptTo` string.

## See Also

- [Get Merchant Details](get-merchant.md)
  Retrieve information about a registered merchant’s current state by using the merchant’s internal merchant identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/merchantdetails)*