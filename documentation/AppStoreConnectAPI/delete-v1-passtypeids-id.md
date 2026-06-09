# Delete a passtypeid

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

- [List passtypeid ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.
- [List pass type ids](get-v1-passtypeids.md)
  Find and list pass type IDs that are registered to your team.
- [Read passtypeid information](get-v1-passtypeids-_id_.md)
  Get information about a specific pass type ID.
- [List all certificates for a passtypeid](get-v1-passtypeids-_id_-certificates.md)
  List all certificates for a specific pass type ID.
- [List certificate ids for a passtypeid](get-v1-passtypeids-_id_-relationships-certificates.md)
  List all certificate IDs for a specific pass type ID.
- [Modify a passtypeid](patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a passtypeid](post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-passtypeids-_id_)*