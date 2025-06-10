# Add an alternative distribution key

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add an alternative distribution key for your alternative marketplace app or web distribution.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Creating keys and establishing alternative marketplace connections](creating-keys-and-establishing-alternative-marketplace-connections.md)
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)

#### Discussion

You can use a single alternative distribution key for all alternative distribution apps on your account. You can optionally use an app specific alternative distribution key, by adding a relationship to a specific app in the JSON payload used with this endpoint.

##### Example Request and Response

##### Example Request and Response

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