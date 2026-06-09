# List passtypeid ids for a certificate

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all PassTypeID Ids for a specific certificate.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates/{id}/passTypeId`

## Parameters

- `fields[certificates]` ([string])
- `fields[passTypeIds]` ([string])
- `include` ([string])
- `limit[certificates]` (integer)

## See Also

- [List and download certificates](get-v1-certificates.md)
  Find and list certificates and download their data.
- [Read and download certificate information](get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates-_id_-passtypeid)*