# List alternative distribution keys

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the alternative distribution key for your account.

**Availability**:
- App Store Connect API 3.4.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys
```

**Response**:

```json
{
  "data": [
    {
      "type": "alternativeDistributionKeys",
      "id": "050614c7-6d00-4db1-98e6-5869c8281f30",
      "attributes": {
        "publicKey": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEskEtS7l4Bl4321ZcP0V7H7rHnmnc\nHAiUWSFK/Hz4bzhd1ZyPYRwRv6zeuH+CiVmFrggScHVrBO0UUz+gRN73kQ==\n-----END PUBLIC KEY-----"
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/050614c7-6d00-1234-98e6-5869c8281f30"
      }
    },
    {
      "type": "alternativeDistributionKeys",
      "id": "739970a0-9c7e-4fd1-be2c-f13204c728b7",
      "attributes": {
        "publicKey": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEZfD+k4321CZCu2tEx0SMsyhInL2G4lRBlF1ZDNnKBV7MPHFlDIQd92S2h37w46qrqVEivpSSWnFKVks+ZBeE5w==\n-----END PUBLIC KEY-----"
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/739970a0-9c7e-2222-be2c-f13204c728b7"
      }
    },
    {
      "type": "alternativeDistributionKeys",
      "id": "ac79daa8-f11c-4c38-b244-4c7a464dbf82",
      "attributes": {
        "publicKey": "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE38Gko2k5454321/+bSb/rMd2BRU0\nRZoHKRMm214cqeickeWFVpOQMHXOvOuhS+i3pX7fiVGvMthanQP2KIwiZQ==\n-----END PUBLIC KEY-----"
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/ac79daa8-f11c-ffff-b244-4c7a464dbf82"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys"
  },
  "meta": {
    "paging": {
      "total": 3,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys`

## Parameters

- `exists[app]` (boolean)
- `fields[alternativeDistributionKeys]` ([string])
- `limit` (integer)

## See Also

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
  Manage keys you use to sign JSON web tokens and connect marketplaces with apps.
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
  Manage keys you use to sign JSON web tokens (JWTs).
- [Add an alternative distribution key](post-v1-alternativedistributionkeys.md)
  Add an alternative distribution key for your alternative marketplace app or web distribution.
- [Read alternative distribution key information](get-v1-alternativedistributionkeys-_id_.md)
  Read the public key information for a specific alternative distribution key.
- [GET /v1/apps/{id}/relationships/alternativeDistributionKey](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Read an app’s alternative distribution key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.
- [Remove an alternative distribution key](delete-v1-alternativedistributionkeys-_id_.md)
  Remove an alternative distribution key from your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionkeys)*