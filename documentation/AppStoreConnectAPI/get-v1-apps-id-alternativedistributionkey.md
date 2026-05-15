# Read an App’s Alternative Distribution Key

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the alternative distribution keys for a specific app.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6473805491/alternativeDistributionKey
```

**Response**:

```json
{
  “data” : {
    “type” : “alternativeDistributionKeys”,
    “id” : “52c5cb04-1163-4a30-ad4f-a3433cd6a4f6”,
    “attributes” : {
      “publicKey” : “-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE7rsxeCw+hrwRgStk0J2vYmnGQZha\ngSt0fm511aTjpDVsaIy9z7jmUKjJ1jgb8P5UKmQfmw0ovD+fNTSefjrw5A==\n-----END PUBLIC KEY-----\n”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/52c5cb04-1163-4a30-ad4f-a3433cd6a4f6”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/apps/6473805491/alternativeDistributionKey”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/alternativeDistributionKey`

## Parameters

- `fields[alternativeDistributionKeys]` ([string])

## See Also

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
  Manage keys you use to sign JSON web tokens and connect marketplaces with apps.
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
  Manage keys you use to sign JSON web tokens (JWTs).
- [Add an Alternative Distribution Key](post-v1-alternativedistributionkeys.md)
  Add an alternative distribution key for your alternative marketplace app or web distribution.
- [List Alternative Distribution Keys](get-v1-alternativedistributionkeys.md)
  List the alternative distribution key for your account.
- [Read Alternative Distribution Key Information](get-v1-alternativedistributionkeys-_id_.md)
  Read the public key information for a specific alternative distribution key.
- [GET /v1/apps/{id}/relationships/alternativeDistributionKey](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Remove an Alternative Distribution Key](delete-v1-alternativedistributionkeys-_id_.md)
  Remove an alternative distribution key from your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-alternativedistributionkey)*