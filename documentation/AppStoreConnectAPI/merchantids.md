# Merchant ID

**Framework**: Appstoreconnectapi

Manage your merchant ID for Apple Pay.

#### Overview

Apple Pay developers and merchants can use this resource to automate registering both merchant ID and merchant name for interacting with Apple Pay services, and rotate required certificates to keep the service active. To learn more about developing and configuring Apple Pay, see [`Configure Apple Pay`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay/).

To learn more about setting up your Apple developer account and implementing Apple Pay in your apps, see [`Managing merchant IDs and Payment Processing certificates`](managing-payment-processing-certificates.md) and [`Setting up Apple Pay`](https://developer.apple.comhttps://developer.apple.com/documentation/passkit/setting-up-apple-pay).

> **Note**: Apple Pay is not available for Enterprise teams.

## Topics

### Managing merchant IDs
- [Managing merchant IDs and Payment Processing certificates](managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [List merchant IDs](get-v1-merchantids.md)
  List all merchant Ids for your team.
- [Read details for a merchant ID](get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificates for a merchant ID](get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [Modify merchant IDs](patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a merchant ID](post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant ID](delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.
### Objects
- [object MerchantId](merchantid.md)
  The data structure that represents a merchant ID resource.
- [object MerchantIdResponse](merchantidresponse.md)
  A response that contains a single merchant ID resource.
- [object MerchantIdsResponse](merchantidsresponse.md)
  A response that contains a list of merchant ID resources.
- [object MerchantIdCreateRequest](merchantidcreaterequest.md)
  The request body you use to create a merchant ID.
- [object MerchantIdUpdateRequest](merchantidupdaterequest.md)
  The request body you use to update a merchant ID.

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/merchantids)*