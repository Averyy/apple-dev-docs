# TN3182: Adding privacy tracking keys to your privacy manifest

**Framework**: Technotes

Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

#### Overview

When you build an app or third-party SDK that contacts domains engaged in tracking, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):

1. Add the `NSPrivacyTracking` key and set its value to `true`.
2. Add the `NSPrivacyTrackingDomains` key and set its value to a list of tracking domains.

For more information about these keys and the privacy manifest, see [`Privacy manifest files`](https://developer.apple.com/documentation/BundleResources/privacy-manifest-files).

This document describes how to add the `NSPrivacyTracking` and `NSPrivacyTrackingDomains` keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

> **Note**: Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

#### Add the Privacy Tracking Key

The `NSPrivacyTracking` key uses the following format:

```xml
<key>NSPrivacyTracking</key>
<!-- Use <true/> if your app or third-party SDK contacts domains engaged in tracking; otherwise use 
    <false/>. -->
<true/>
```

To add the `NSPrivacyTracking` key to your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Click the Add button (+) beside the `App Privacy Configuration` key in the property list editor.
3. In the pop-up menu that appears, choose `NSPrivacyTracking`.
4. Confirm the value is `Boolean` in the Type column.
5. Select `YES` from the pop-up menu in the Value column.

#### Add a Tracking Domain to the Privacy Tracking Domains Key

Set the value of the `NSPrivacyTrackingDomains` key to a list of tracking domains in your privacy manifest. For more information about tracking domains, see “Configure a tracking domain” in [`TN3181: Debugging an invalid privacy manifest`](tn3181-debugging-invalid-privacy-manifest.md).

To add a tracking domain to the `NSPrivacyTrackingDomains` key in your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Find the `NSPrivacyTrackingDomains` key in the property list editor.
3. Confirm the value is `Array` in the Type column.
4. Click the disclosure triangle to the left of `NSPrivacyTrackingDomains` to reveal it.
5. Click the Add button (+) beside `NSPrivacyTrackingDomains` to insert a tracking domain such as `mywebsite.example.com`.

#### Add the Privacy Tracking Domains Key

The `NSPrivacyTrackingDomains` key uses the following format:

```xml
<key>NSPrivacyTrackingDomains</key>
<array>
    <string>mywebsite.example.com</string>
    ...
</array>
```

Each string value in the array identifies an internet domain your app or third-party SDK connects to that engages in tracking. For more information, see [`Add a tracking domain to the privacy tracking domains key`](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest#Add-a-tracking-domain-to-the-privacy-tracking-domains-key.md).

To add the `NSPrivacyTrackingDomains` key to your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Click the Add button (+) beside the `App Privacy Configuration` key in the property list editor.
3. In the pop-up menu that appears, choose `NSPrivacyTrackingDomains`.
4. Confirm the value is `Array` in the Type column.
5. To add a tracking domain to the array, see [`Add a tracking domain to the privacy tracking domains key`](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest#Add-a-tracking-domain-to-the-privacy-tracking-domains-key.md).

The following example declares one tracking domain for an app called `Sample`:

Repeat step 5 for each additional tracking domain your app or third-party SDK contacts. The example below declares an additional tracking domain for `Sample`:

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
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest)*