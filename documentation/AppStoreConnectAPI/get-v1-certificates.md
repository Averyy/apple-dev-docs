# List and download certificates

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list certificates and download their data.

**Availability**:
- App Store Connect API 1.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/certificates`

## Parameters

- `fields[certificates]` ([string])
- `filter[id]` ([string])
- `filter[serialNumber]` ([string])
- `limit` (integer)
- `sort` ([string])
- `filter[certificateType]` ([string])
- `filter[displayName]` ([string])
- `fields[passTypeIds]` ([string])
- `include` ([string])

## See Also

- [Read and download certificate information](get-v1-certificates-_id_.md)
  Get information about a certificate and download the certificate data.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-certificates)*