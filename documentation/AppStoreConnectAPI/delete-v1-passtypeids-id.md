# Delete a Passtypeid

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a pass type ID that is used for app distribution.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/passTypeIds/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [List Passtypeid IDs for a Certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [GET /v1/certificates/{id}/relationships/passTypeId](get-v1-certificates-_id_-relationships-passtypeid.md)
- [List Pass Type IDs](get-v1-passtypeids.md)
  Find and list pass type IDs that are registered to your team.
- [Read Passtypeid Information](get-v1-passtypeids-_id_.md)
  Get information about a specific pass type ID.
- [List All Certificates for a Passtypeid](get-v1-passtypeids-_id_-certificates.md)
  List all certificates for a specific pass type ID.
- [GET /v1/passTypeIds/{id}/relationships/certificates](get-v1-passtypeids-_id_-relationships-certificates.md)
- [Modify a Passtypeid](patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a Passtypeid](post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-passtypeids-_id_)*