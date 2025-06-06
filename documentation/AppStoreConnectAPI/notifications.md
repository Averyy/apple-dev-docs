# Notifications

**Framework**: Appstoreconnectapi

Add and read information for alternative distribution package notifications.

#### Overview

Alternative marketplaces can use the marketplace webhooks API [`Add a marketplace webhook configuration`](post-v1-marketplacewebhooks.md) endpoint to set up an `endpointURL,` where the marketplace receives notifications about changes to apps that it distributes.

The most typical notifications are:

- A new app version is available.
- A specific app version needs to be removed.
- All versions of an app need to be removed.

To learn more about configuring a webhook URL using the API, see [`Add a marketplace webhook configuration`](post-v1-marketplacewebhooks.md).

To learn more about server-side processing of marketplace webhook notifications, see [`Processing alternative app marketplace notifications`](https://developer.apple.com/documentation/appdistribution/processing-alternative-marketplace-notifications).

> **Note**:  To receive notifications for an app, the developer of an app distributed on an alternative marketplace must enable it in App Store Connect, to learn more see [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace). If a developer doesn’t opt-in to notifications, they must provide that alternative distribution ID to the marketplace so the marketplace can ingest the alternative distribution package. To learn more about server-side processing of marketplace webhooks, see [`Processing alternative app marketplace notifications`](https://developer.apple.com/documentation/appdistribution/processing-alternative-marketplace-notifications).

## Topics

### Managing Webhook Endpoint URLs
- [Read marketplace webhook information](get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Add a marketplace webhook configuration](post-v1-marketplacewebhooks.md)
  Add a new endpoint URL and secret for alternative distribution package notifications.
- [Modify a marketplace webhook configuration](patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.
- [Delete a marketplace webhook configuration](delete-v1-marketplacewebhooks-_id_.md)
  Delete a specific marketplace notifcation endpoint URL.
### Objects
- [object MarketplaceWebhook](marketplacewebhook.md)
  The data structure that represents a marketplace webhook resource.
- [object MarketplaceWebhookCreateRequest](marketplacewebhookcreaterequest.md)
  The request body you use to create a marketplace webhook url.
- [object MarketplaceWebhookResponse](marketplacewebhookresponse.md)
  A response that contains a single marketplace webhook resource.
- [object MarketplaceWebhooksResponse](marketplacewebhooksresponse.md)
  A response that contains a list of a marketplace webhook resources.
- [object MarketplaceWebhookUpdateRequest](marketplacewebhookupdaterequest.md)
  The request body you use to update a marketplace webhook url.

## See Also

- [Alternative Distribution Packages](alternative-distribution-packages.md)
  Create and read distribution packages for an alternative app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/notifications)*