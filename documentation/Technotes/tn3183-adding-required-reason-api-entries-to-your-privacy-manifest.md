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

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest)*