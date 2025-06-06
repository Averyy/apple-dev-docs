# TN3180: Reverting to App Store Server Notifications V1

**Framework**: Technotes

Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.

#### Overview

When you enable your server to receive App Store Server Notifications, you configure your settings in App Store Connect. You select the version of App Store Server Notifications you want to receive, and provide your server URL, as described in [`Enter server URLs for App Store Server Notifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/enter-server-urls-for-app-store-server-notifications).

> **Note**: The [`App Store Server Notifications V1`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint and version 1 notifications are deprecated. Implement the [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications instead.

The [`App Store Server Notifications V1`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint and version 1 notifications are deprecated. Implement the [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications instead.

In the unusual case that you need to revert from version 2 to version 1 of App Store Server Notifications, use the [`Modify an App`](https://developer.apple.com/documentation/AppStoreConnectAPI/PATCH-v1-apps-_id_) endpoint.

#### Create the App Modification Request

The Modify an App endpoint updates app information including the URL and version you use for App Store Notifications. To use this endpoint, create a object that includes the `id`, `type`, and `attributes` properties detailed in [`AppUpdateRequest.Data`](https://developer.apple.com/documentation/AppStoreConnectAPI/AppUpdateRequest/Data-data.dictionary).

To revert to version 1 of App Store Server Notifications, add the following attributes to the request body of the endpoint:

| Attribute | Value |
| --- | --- |
| `subscriptionStatusUrl` | Your server’s [`App Store Server Notifications V1`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint URL. |
| `subscriptionStatusUrlVersion` | `V1` to indicate you’re using version 1 of App Store Server Notifications. |

The following code shows an example of a modification request that changes only the app’s App Store Server Notifications URL and version:

To change your server’s URL for receiving App Store Server Notifications in the sandbox environment, add the following attributes to the request body of the endpoint:

| Attribute | Value |
| --- | --- |
| `subscriptionStatusUrlForSandbox` | Your server’s [`App Store Server Notifications V1`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V1) endpoint URL for the sandbox environment. |
| `subscriptionStatusUrlVersionForSandbox` | `V1` to indicate you’re using version 1 of App Store Server Notifications in the sandbox environment. |

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3180-reverting-app-store-server-notifications-v1)*