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

**Source code**:

```xml
<plist>
<dict>
    <key>NSPrivacyTracking</key>
    <true/>
    <key>NSPrivacyTrackingDomains</key>
    <array>
        <string>mywebsite.example.com</string>
    </array>
</dict>
</plist>
```

**Property list**:

![A privacy manifest that contains the NSPrivacyTracking and NSPrivacyTrackingDomains keys. NSPrivacyTrackingDomains contains one tracking domain.](https://docs-assets.developer.apple.com/published/d859f1620a60329db1c7493fa34c14f0/tn3182-privacy_tracking_single_domain%402x.png)

Repeat step 5 for each additional tracking domain your app or third-party SDK contacts. The example below declares an additional tracking domain for `Sample`:

**Source code**:

```xml
<plist>
<dict>
    <key>NSPrivacyTracking</key>
    <true/>
    <key>NSPrivacyTrackingDomains</key>
    <array>
        <string>mywebsite.example.com</string>
        <string>tracking.subdomain.example.com</string>
    </array>
</dict>
</plist>
```

**Property list**:

![A privacy manifest that contains the NSPrivacyTracking and NSPrivacyTrackingDomains keys. NSPrivacyTrackingDomains contains two tracking domains.](https://docs-assets.developer.apple.com/published/15f0c626a8a9071cb16459e2def9c04d/tn3182-privacy_tracking_multiple_domains%402x.png)

#### Revision History

- **2024-12-17** First published.

## See Also

- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest)*