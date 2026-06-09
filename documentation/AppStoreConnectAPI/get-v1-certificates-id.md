# Read and download certificate information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a certificate and download the certificate data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates/{id}`

## Parameters

- `fields[certificates]` ([string])
- `fields[passTypeIds]` ([string])
- `include` ([string])

## See Also

- [List and download certificates](get-v1-certificates.md)
  Find and list certificates and download their data.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates-_id_)*