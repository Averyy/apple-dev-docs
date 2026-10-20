# GetVppAssetRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request for an asset.

**Availability**:
- VPP License Management 1.0+

## Declaration

```
object GetVppAssetRequest
```

## Properties

- `includeLicenseCounts` (boolean): If `true`, returns the total number of licenses, the number of assigned licenses, and the number of unassigned licenses in the response for each asset.
- `pricingParam` (string): The quality of a product in the iTunes Store. If a pricing parameter is specified, only records with that parameter are included in the results. Possible values are:

  - `STDQ`: Standard quality
  - `PLUS`: High quality
- `sToken` (string) *(required)*: The authentication token. For more information, see [Authenticate with the web service](./managing-apps-and-books-through-web-services-legacy.md#Authenticate-with-the-web-service).

## See Also

### Request and Response
- [object GetVppAssetResponse](./getvppassetresponse.md)
  The response with the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvppassetrequest)*