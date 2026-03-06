# Add an alternative distribution key

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add an alternative distribution key for your alternative marketplace app or web distribution.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)

#### Discussion

You can use a single alternative distribution key for all alternative distribution apps on your account. You can optionally use an app specific alternative distribution key, by adding a relationship to a specific app in the JSON payload used with this endpoint.

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys
{
  "data": {
    "type": "alternativeDistributionKeys",
    "id": null,
    "attributes": {
      "publicKey": "-----BEGIN PUBLIC KEY-----MFkwEwYHKoZIzj0CAQYIKoZIzj0DA7021gAEFQUkD1YB67wg3e0VD/2c3N3Wf92nuQqDgFZuYG/NcYLwT3Zdw77s6//8XSI2NYv7WNgUONxMj+j65Qijq4/fhw==-----END PUBLIC KEY-----"
    }
  }
}
```

**Response**:

```json
{
  “data” : {
    “type” : “alternativeDistributionKeys”,
    “id” : “52c5cb04-1163-65ar-36aa-a3433cd6a4f6”,
    “attributes” : {
      “publicKey” : “-----BEGIN PUBLIC KEY-----MFkwEwYHKoZIzj0CAQYIKoZIzj0DA7021gAEFQUkD1YB67wg3e0VD/2c3N3Wf92nuQqDgFZuYG/NcYLwT3Zdw77s6//8XSI2NYv7WNgUONxMj+j65Qijq4/fhw==-----END PUBLIC KEY-----”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/52c5cb04-1163-4a30-ad4f-a3433cd6a4f6”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/apps/6476788026/alternativeDistributionKeys”
  }
}

```

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys
{
  "data": {
    "type": "alternativeDistributionKeys",
    "id": null,
    "attributes": {
      "publicKey": "-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFQUkD1YB67wg3e0VD/2c3N3Wf92n
uQqDgFZuYG/NcYLwT3Zdw77s6//8XSI2NYv7WNgUONxMj+j65Qijq4/fhw==
-----END PUBLIC KEY-----"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6476788026"
        }
      }
    }
  }
}
```

**Response**:

```json
{
  "data" : {
    "type" : "alternativeDistributionKeys",
    "id" : "52c5cb04-1163-4a30-ad4f-a3433cd6a4f6",
    "attributes" : {
      "publicKey" : "-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEFQUkD1YB67wg3e0VD/2c3N3Wf92n
uQqDgFZuYG/NcYLwT3Zdw77s6//8XSI2NYv7WNgUONxMj+j65Qijq4/fhw==
-----END PUBLIC KEY-----"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys/52c5cb04-1163-4a30-ad4f-a3433cd6a4f6"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/6476788026/alternativeDistributionKeys"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionKeys`

## See Also

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
  Manage keys you use to sign JSON web tokens and connect marketplaces with apps.
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
  Manage keys you use to sign JSON web tokens (JWTs).
- [List alternative distribution keys](get-v1-alternativedistributionkeys.md)
  List the alternative distribution key for your account.
- [Read alternative distribution key information](get-v1-alternativedistributionkeys-_id_.md)
  Read the public key information for a specific alternative distribution key.
- [GET /v1/apps/{id}/relationships/alternativeDistributionKey](get-v1-apps-_id_-relationships-alternativedistributionkey.md)
- [Read an app’s alternative distribution key](get-v1-apps-_id_-alternativedistributionkey.md)
  Get the alternative distribution keys for a specific app.
- [Remove an alternative distribution key](delete-v1-alternativedistributionkeys-_id_.md)
  Remove an alternative distribution key from your account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-alternativedistributionkeys)*