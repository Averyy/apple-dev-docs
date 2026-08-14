# Processing alternative app marketplace notifications

**Framework**: MarketplaceKit

Manage the addition and removal of apps available on your alternative marketplace.

#### Overview

When an alternative distribution app completes Notarization, App Store Connect makes the app available for download in the form of an *alternative distribution package* (ADP). The developer of the app can download the ADP manually, or enable notifications in App Store Connect to send the app information automatically to an alternative app marketplace that distributes the app.

To receive notifications, the marketplace developer implements an endpoint, or webhook, on their marketplace server back end, and defines the webhook URL in App Store Connect.

App Store Connect includes information in notifications about newly available app versions, and the identifiers of one or more versions of an app to be removed.

#### Meet the Criteria for Notifications

When a new app version passes notarization for an app that installs from your marketplace, App Store Connect requires the following conditions before notifying your webhook:

- You and the app developer sign the respective Developer Program License Agreement; notifications cease if either signed license agreement expires.
- The marketplace app completes Notarization and is `Ready for Distribution` in App Store Connect; notifications cease for any other state. Note that `Ready for Distribution` doesn’t determine when you can publish the download link on your website. You can test notifications before making the download link public.
- A relationship exists between you and the app developer in App Store Connect. See [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace).
- The developer enables notifications in App Store Connect for the apps that distribute on your alternative marketplace.

> ❗ **Important**: App Store Connect doesn’t send notifications for your marketplace app itself. When your app or app update passes Notarization, you need to download its associated alternative distribution package from App Store Connect manually. For more information, see [`Distributing your app from your website`](distributing-your-app-from-your-website.md).

#### Set Up Your Notification Webhook

A *notification webhook* is an endpoint that you create on your marketplace server, which receives HTTP POST requests from App Store Connect. The POST requests describe important events about your app or the apps that your marketplace distributes.

To invoke your webhook, App Store Connect needs to know your server’s webhook endpoint URL. To set up your webhook endpoint the first time, provide the URL to the [`Add a Marketplace Webhook Configuration`](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-marketplacewebhooks) endpoint:

```None
POST https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks
```

Any time you reconfigure your web server, use the [`Modify a Marketplace Webhook Configuration`](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-marketplacewebhooks-_id_) endpoint to update App Store Connect.

For more information about managing webhook endpoint configuration for your marketplace, see [`Notifications`](https://developer.apple.com/documentation/appstoreconnectapi/notifications).

#### Set Up Notification Authentication

Secure your webhook by verifying that a request to your endpoint comes from App Store Connect. The security protocol for webhooks is Hash-based Message Authentication Code (HMAC), which requires that you:

- Share a secret phrase with the request sender (App Store Connect).
- Verify that each POST to your endpoint has the HMAC header and validate it with your secret.

When you register your webhook URL with App Store Connect, define the secret phrase using the `secret` key in [`MarketplaceWebhookCreateRequest.Data.Attributes`](https://developer.apple.com/documentation/appstoreconnectapi/marketplacewebhookcreaterequest/data-data.dictionary/attributes-data.dictionary). Choose a `String` value for `secret` that’s difficult to guess.

App Store Connect creates a hash signature using the secret and includes in each POST. The signature resides in the payload header as `x-apple-signature`.

Verify the signature by implementing code in your webhook endpoint that:

- Creates a hash from the payload body using your secret token.
- Compares the hash to the one App Store Connect sends in the header to ensure they match.

For example, applying `HMAC-SHA256` to the `secret` “This is my secret” and payload body “Hello, World!” produces the hash:

```None
7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

This result verifies a POST is authentic — the sender knows the secret — if the payload contains the header:

```None
x-apple-signature:hmacsha256=7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

Use an implementation of HMAC `hex digest` to generate the hash. For more information, see [`GitHub’s Validating webhook deliveries`](https://developer.apple.comhttps://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries).

#### Receive a Notification and Determine the Type

When App Store Connect sends a notification to your webhook, it does so in the form of an HTTP POST. When you receive a notification, check its type to process it accordingly. The action you perform depends on the notification type, which is among the following:

| Notification type | Description |
| --- | --- |
| `AlternativeDistributionPackageVersionAvailable` | An alternative distribution package for a newly approved app version. |
| `AppVersionUnavailable` | A request to remove the alternative distribution package for a specific app version. |
| `AppUnavailable` | A request to remove all alternative distribution packages for an app. |

Each type has a specific data set, or *schema*, composed of `attributes` that drive the different action you take.

In rare circumstances, your webhook may receive a duplicate notification. Your webhook can filter out duplicate notifications by discarding them. Specifically, if you receive a notification of type `AlternativeDistributionPackageVersionAvailable` that describes a package that your webhook already ingested, discard it. Similarly, if you receive a notification of type `AppVersionsUnavailable` or `AppUnavailable` for an app or version that’s already unavailable, discard it.

#### Process an Available App Version

When the type is `AlternativeDistributionPackageVersionAvailable`, the `attributes` include the alternative distribution package ID, version ID and version number. Use this information to add the new app or versions of an app. An example notification follows:

```json
{
  "data": {
    "type": "AlternativeDistributionPackageVersionAvailable",
    "version": 1,
    "id": "543c3939-2db6-4fbc-9672-fb0ec5687624",
    "timestamp": "2023-11-27T10:40:37.246-08:00",
    "attributes": {
      "marketplaceAppId": "3839839",
      "appId": "1111",
      "alternativeDistributionPackageId": "f826eb7a-fa2b-420f-a780-356106195663",
      "alternativeDistributionPackageVersionId": "6B29FC40-CA47-1067-B31D-00DD010662DA",
      "alternativeDistributionPackageVersionNum": "1",
      "eventTimestamp": "2023-11-27T18:40:32.143-00:00"
    }
  }
}
```

To learn more about ingesting apps and app versions, see [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md).

#### Process a Request to Remove Specific App Versions

When the notification type is `AppVersionsUnavailable`, App Store Connect requests that you remove the identified app versions from your alternative marketplace. The `attributes` include a list of alternative distribution package IDs to remove. An example notification follows:

```json
{
  "data": {
    "type": "AppVersionsUnavailable",
    "version": 1,
    "id": "543c3939-2db6-4fbc-9672-fb0ec5687624",
    "timestamp": "2023-11-27T10:40:37.246-08:00",
    "attributes": {
      "marketplaceAppId": "3839839",
      "appId": "1111",
      "alternativeDistributionPackageIds": [
        "f826eb7a-fa2b-420f-a780-356106195663"
      ],
      "eventTimestamp": "2023-11-27T18:40:32.143-00:00"
    }
  }
}
```

#### Process a Request to Remove All Versions of an App

The `AppUnavailable` type is similar to `AppVersionsUnavailable`, except that App Store Connect requests that you remove all versions for the identified app. As such, the `attributes` contain only the app to remove. An example notification follows:

```json
{
  "data": {
    "type": "AppUnavailable",
    "version": 1,
    "id": "543c3939-2db6-4fbc-9672-fb0ec5687624",
    "timestamp": "2023-11-27T10:40:37.246-08:00",
    "attributes": {
      "marketplaceAppId": "3839839",
      "appId": "1111",
      "eventTimestamp": "2023-11-27T18:40:32.143-00:00"
    }
  }
}
```

## See Also

- [Ingesting an alternative distribution package](ingesting-an-alternative-distribution-package.md)
  Process an available app version from App Store Connect and store it for download from your server.
- [Installing your app from your website](installing-your-app-from-your-website.md)
  Manage the installation of an app that you develop and distribute through your website.
- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
  Manage the installation of apps that developers distribute from your marketplace app.
- [Supplying an install verification token](supplying-an-install-verification-token.md)
  Support the installation of alternative distribution apps by creating signed JSON web tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/processing-alternative-marketplace-notifications)*