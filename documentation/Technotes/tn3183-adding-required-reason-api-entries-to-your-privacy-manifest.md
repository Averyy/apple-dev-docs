# TN3183: Adding required reason API entries to your privacy manifest

**Framework**: Technotes

Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.

#### Overview

When you build an app or third-party SDK that uses any required reason API, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):

1. Add the `NSPrivacyAccessedAPITypes` key and set its value to the dictionary.
2. For each required reason API your app or third-party SDK uses, add a dictionary as a value for the `NSPrivacyAccessedAPITypes` key. The dictionary includes the category of the reason API and a list of reasons for using this API. For more information, see [`Add an accessed API type and reasons dictionary`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Add-an-accessed-API-type-and-reasons-dictionary.md).

See [`Privacy manifest files`](https://developer.apple.com/documentation/BundleResources/privacy-manifest-files) and [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api) for more information about the privacy manifest and these keys.

This document describes how to add the `NSPrivacyAccessedAPIType`, `NSPrivacyAccessedAPITypeReasons`, and `NSPrivacyAccessedAPITypes` keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

> **Note**: Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

#### Select an Accessed Api Category

A privacy accessed API category identifies the category of required reason APIs your app or third-party SDK uses. Set the value of the `NSPrivacyAccessedAPIType` key to a privacy accessed API category. For more information, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

The possible values of a privacy accessed API category are:

- `NSPrivacyAccessedAPICategoryActiveKeyboards`
- `NSPrivacyAccessedAPICategoryDiskSpace`
- `NSPrivacyAccessedAPICategoryFileTimestamp`
- `NSPrivacyAccessedAPICategorySystemBootTime`
- `NSPrivacyAccessedAPICategoryUserDefaults`

#### Add an Accessed Api Type Key

The `NSPrivacyAccessedAPIType` key uses the following format:

```xml
<key>NSPrivacyAccessedAPIType</key>
<string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>
```

The `NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE` string represents a privacy accessed API category. For more information, see [`Select an accessed API category`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Select-an-accessed-API-category.md).

To add the `NSPrivacyAccessedAPIType` key to a privacy accessed API type and reasons dictionary:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Click the Add button (+) beside the dictionary to add a new item.
4. In the pop-up menu that appears, choose `NSPrivacyAccessedAPIType`.
5. Confirm the value is `String` in the Type column.
6. Select a privacy accessed API category from the pop-up menu in the Value column. For possible values, see [`Select an accessed API category`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Select-an-accessed-API-category.md).
7. Confirm that the value exactly matches the category of required reason API that your app or third-party SDK uses.

#### Add an Accessed Api Type Reasons Key

The `NSPrivacyAccessedAPITypeReasons` key uses the following format:

```xml
<key>NSPrivacyAccessedAPITypeReasons</key>
<array>
    <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
    ...
</array>
```

Each `NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE` string in the array identifies a reason why your app or third-party SDK uses a required reason API. All the values in the array are associated with a `NSPrivacyAccessedAPIType` key you provide when you create a privacy accessed API type and reasons dictionary.

To add the `NSPrivacyAccessedAPITypeReasons` key to a privacy accessed API type and reasons dictionary:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Confirm the dictionary contains a `NSPrivacyAccessedAPIType` key with a value as described in [`Select an accessed API category`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Select-an-accessed-API-category.md).
4. Click the Add button (+) beside the dictionary to add a new item.
5. In the pop-up menu that appears, choose `NSPrivacyAccessedAPITypeReasons`.
6. Confirm the value is `Array` in the Type column.
7. Click the disclosure triangle to the left of `NSPrivacyAccessedAPITypeReasons` to reveal it.
8. Click the Add button (+) beside `NSPrivacyAccessedAPITypeReasons` to add a reason.
9. Choose a reason from the pop-up menu in the Value column. For possible values, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).
10. Confirm that the value exactly matches a reason for the `NSPrivacyAccessedAPIType` key you use in step 3.

#### Add an Accessed Api Type and Reasons Dictionary

A privacy accessed API type and reasons dictionary includes a category of required reason APIs and a list of related reasons. The dictionary contains exactly two keys: `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons`. It uses the following format:

```xml
<dict>
    <!— Add an accessed API type key. -->
    <key>NSPrivacyAccessedAPIType</key>
    <string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>

    <!— Add an accessed API type reasons key. -->
    <key>NSPrivacyAccessedAPITypeReasons</key>
    <array>
        <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
        ...
    </array>
</dict>
```

To add a privacy accessed API type and reasons dictionary to the `NSPrivacyAccessedAPITypes` key in your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Find the `NSPrivacyAccessedAPITypes` key in the property list editor.
3. Click the disclosure triangle to the left of `NSPrivacyAccessedAPITypes` to reveal it.
4. Click the Add button (+) beside `NSPrivacyAccessedAPITypes` to insert a new item.
5. Confirm the value is `Dictionary` in the Type column.
6. To add the `NSPrivacyAccessedAPIType` key to the dictionary, see [`Add an accessed API type key`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Add-an-accessed-API-type-key.md).
7. To add the `NSPrivacyAccessedAPITypeReasons` key to the dictionary, see [`Add an accessed API type reasons key`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Add-an-accessed-API-type-reasons-key.md).

#### Add the Accessed Api Types Key

The `NSPrivacyAccessedAPITypes` key is an array of privacy accessed API type and reasons dictionaries. For more information, see [`Add an accessed API type and reasons dictionary`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Add-an-accessed-API-type-and-reasons-dictionary.md). The key uses the following format:

```xml
<key>NSPrivacyAccessedAPITypes</key>
<array>
    <dict>
        <key>NSPrivacyAccessedAPIType</key>
        <string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>
        <key>NSPrivacyAccessedAPITypeReasons</key>
        <array>
            <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
            ...
        </array>
    </dict>
    ...
</array>
```

To add the `NSPrivacyAccessedAPITypes` key to your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Click the Add button (+) beside the `App Privacy Configuration` key in the property list editor.
3. In the pop-up menu that appears, choose `NSPrivacyAccessedAPITypes`.
4. Confirm the value is `Array` in the Type column.
5. To add a privacy accessed API type and reasons dictionary to the array, see [`Add an accessed API type and reasons dictionary`](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest#Add-an-accessed-API-type-and-reasons-dictionary.md).

The following example declares disk space required reason API usage in an app named `Sample`:

Repeat step 5 for each additional required reason API your app or third-party SDK uses. The example below additionally declares user defaults required reason API usage in `Sample`:

#### Revision History

-  First published.

## See Also

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
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest)*