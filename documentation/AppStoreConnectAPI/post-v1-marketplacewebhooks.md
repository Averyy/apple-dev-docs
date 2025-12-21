# Add a marketplace webhook configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a new endpoint URL and secret for alternative distribution package notifications.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)

#### Discussion

Each developer account has a single marketplace webhooks `endpointUrl`, so if you operate mutliple marketplaces all notifications come to a single endpoint. The notification payload contains the `marketplaceAppId.`

##### Example Request and Response

## See Also

- [Read marketplace webhook information](get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Modify a marketplace webhook configuration](patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.
- [Delete a marketplace webhook configuration](delete-v1-marketplacewebhooks-_id_.md)
  Delete a specific marketplace notifcation endpoint URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-marketplacewebhooks)*