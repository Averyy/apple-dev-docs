# Remove an alternative distribution key

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove an alternative distribution key from your account.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/52c5cb04-1163-4a30-ad4f-a3433cd6a4f6
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `alternativeDistributionKey` resource ID from the [`Read an app’s alternative distribution key`](get-v1-apps-_id_-alternativedistributionkey.md) response.

## See Also

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
  Manage keys you use to sign JSON web tokens and connect marketplaces with apps.
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
  Manage keys you use to sign JSON web tokens (JWTs).
- [Add an alternative distribution key](post-v1-alternativedistributionkeys.md)
  Add an alternative distribution key for your alternative marketplace app or web distribution.
- [List alternative distribution keys](get-v1-alternativedistributionkeys.md)
  List the alternative distribution key for your account.
- [Read alternative distribution key information](get-v1-alternativedistributionkeys-_id_.md)
  Read the public key information for a specific alternative distribution key.
- [GET /v1/apps/{id}/relationships/alternativeDistributionKey](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Read an app’s alternative distribution key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-alternativedistributionkeys-_id_)*