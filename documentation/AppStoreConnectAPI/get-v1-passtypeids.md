# List Pass Type IDs

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list pass type IDs that are registered to your team.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/passTypeIds`

## Parameters

- `fields[certificates]` ([string])
- `fields[passTypeIds]` ([string])
- `filter[id]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[certificates]` (integer)
- `sort` ([string])

## See Also

- [List Passtypeid IDs for a Certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [GET /v1/certificates/{id}/relationships/passTypeId](get-v1-certificates-_id_-relationships-passtypeid.md)
- [Read Passtypeid Information](get-v1-passtypeids-_id_.md)
  Get information about a specific pass type ID.
- [List All Certificates for a Passtypeid](get-v1-passtypeids-_id_-certificates.md)
  List all certificates for a specific pass type ID.
- [GET /v1/passTypeIds/{id}/relationships/certificates](get-v1-passtypeids-_id_-relationships-certificates.md)
- [Modify a Passtypeid](patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a Passtypeid](post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [Delete a Passtypeid](delete-v1-passtypeids-_id_.md)
  Delete a pass type ID that is used for app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-passtypeids)*