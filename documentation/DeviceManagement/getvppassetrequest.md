# GetVppAssetRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for an asset.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetVppAssetRequest
```

## Properties

- `includeLicenseCounts` (boolean): If `true`, returns the total number of licenses, the number of assigned licenses, and the number of unassigned licenses in the response for each asset.
- `pricingParam` (string): The quality of a product in the iTunes Store. If a pricing parameter is specified, only records with that parameter are included in the results. Possible values are: - `STDQ`: Standard quality
- `PLUS`: High quality
- `sToken` (string) *(required)*: The authentication token. For more information, see [`Authentication`](managing-apps-and-books-through-web-services-legacy#Authentication.md).

## See Also

- [object GetVppAssetResponse](getvppassetresponse.md)
  The response with the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvppassetrequest)*