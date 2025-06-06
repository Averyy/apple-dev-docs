# Alternative Distribution Keys

**Framework**: App Store Connect API

Create and manage keys for an alternative app distribution.

#### Overview

As an alternative marketplace developer you create keys and JSON web tokens (JWTs) to authenticate and connect your marketplace to the apps distributed on your marketplace.

The alternative distribution key you upload to App Store Connect is a public key. Your alternative distribution key is assocaited with all alternative distribution apps in your account. You can optionally assocaite a key with a single althernative disitribution app by adding a relationship in the payload when calling [`Add an alternative distribution key`](post-v1-alternativedistributionkeys.md). To learn more about creating this key, see [`Creating keys and establishing alternative marketplace connections`](creating-keys-and-establishing-alternative-marketplace-connections.md).

The alternative distribution key `ID`, which you can find in the response body of the endpoint described in  [`Read an app’s alternative distribution key`](get-v1-apps-_id_-alternativedistributionkey.md) is also a part of creating the JWT for [`Supplying an install verification token`](https://developer.apple.com/documentation/appdistribution/supplying-an-install-verification-token).

When using web distribution, you need to create an alternative distribution key, the private half of the key pair is used for install verification.  To learn more about creating keys for web distribution, see [`Creating and configuring keys for web distribution`](creating-and-configuring-keys-for-web-distribution.md). For more information, see [`Supplying an install verification token`](https://developer.apple.com/documentation/appdistribution/supplying-an-install-verification-token).

## Topics

### Creating and reading keys
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
- [Remove an alternative distribution key](delete-v1-alternativedistributionkeys-_id_.md)
  Remove an alternative distribution key from your account.
### Objects
- [object AlternativeDistributionKey](alternativedistributionkey.md)
  The data structure that represents an alternative distribution key resource.
- [object AlternativeDistributionKeyResponse](alternativedistributionkeyresponse.md)
  A response that contains a single alternative distribution key resource.
- [object AlternativeDistributionKeysResponse](alternativedistributionkeysresponse.md)
  A response that contains a list of alternative distribution keys.
- [object AlternativeDistributionKeyCreateRequest](alternativedistributionkeycreaterequest.md)
  The request body you use to create an alternative distribution key.

## See Also

- [Alternative Distribution Domains](alternative-distribution-domains.md)
  Create and read alternative distribution domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternative-distribution-keys)*