# TN3184: Adding data collection details to your privacy manifest

**Framework**: Technotes

Declare the data your app or third-party SDK collects in a privacy manifest.

#### Overview

When you build an app or third-party SDK that collects any data type, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):

1. Add the `NSPrivacyCollectedDataTypes` key.
2. For each data type your app or third-party SDK collects, add a dictionary as a value for the `NSPrivacyCollectedDataTypes` key. The dictionary includes the data type, the data linked to the user and tracking status, and a list of reasons for collecting this data type. For more information, see [`Add a collected data type and reasons dictionary`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-and-reasons-dictionary.md).

For more information about the privacy manifest and these keys, see [`Privacy manifest files`](https://developer.apple.com/documentation/BundleResources/privacy-manifest-files) and [`Describing data use in privacy manifests`](https://developer.apple.com/documentation/BundleResources/describing-data-use-in-privacy-manifests).

This document describes how to add the `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, and `NSPrivacyCollectedDataTypePurposes` keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

> **Note**:  Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

#### Add a Collected Data Type Key

The `NSPrivacyCollectedDataType` key uses the following format:

```xml
<key>NSPrivacyCollectedDataType</key>
<string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>
```

The `NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE` string specifies the type of data your app or third-party SDK collects. For possible values, see “Report the categories of data your app or third-party SDK collects“ in [`Describing data use in privacy manifests`](https://developer.apple.com/documentation/BundleResources/describing-data-use-in-privacy-manifests).

To add the `NSPrivacyCollectedDataType` key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Click the Add button (+) beside the dictionary to add a new item.
4. In the pop-up menu, choose `NSPrivacyCollectedDataType`.
5. In the Type column, confirm that the value is `String`.
6. Select a data type from the pop-up menu in the Value column. For possible values, see “Report the categories of data your app or third-party SDK collects“ in [`Describing data use in privacy manifests`](https://developer.apple.com/documentation/BundleResources/describing-data-use-in-privacy-manifests).
7. Confirm that the value exactly matches the type of data your app or third-party SDK collects.

#### Add a Collected Data Type Linked Key

The `NSPrivacyCollectedDataTypeLinked` key uses the following format:

```xml
<key>NSPrivacyCollectedDataTypeLinked</key>
<!-- Use <true/> if your app or third-party SDK links this data type to the user’s identity; otherwise,
     use <false/>. -->
<true/>
```

To add the `NSPrivacyCollectedDataTypeLinked` key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Click the Add button (+) beside the dictionary to add a new item.
4. In the pop-up menu, choose `NSPrivacyCollectedDataTypeLinked`.
5. In the Type column, confirm that the value is `Boolean`.
6. Select `YES` from the pop-up menu in the Value column if your app or third-party SDK links this data type to the user’s identity; otherwise, select `NO`.

#### Add a Collected Data Type Tracking Key

The `NSPrivacyCollectedDataTypeTracking` key uses the following format:

```xml
<key>NSPrivacyCollectedDataTypeTracking</key>
<!-- Use <true/> if your app or third-party SDK uses this data type to track; otherwise, use <false/>. -->
<true/>
```

To add the `NSPrivacyCollectedDataTypeTracking` key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Click the Add button (+) beside the dictionary to add a new item.
4. In the pop-up menu, choose `NSPrivacyCollectedDataTypeTracking`.
5. In the Type column, confirm that the value is `Boolean`.
6. Select `YES` from the pop-up menu in the Value column if your app or third-party SDK uses this data type to track; otherwise, select `NO`.

#### Add a Collected Data Type Purposes Key

The `NSPrivacyCollectedDataTypePurposes` key uses the following format:

```xml
<key>NSPrivacyCollectedDataTypePurposes</key>
<array>
    <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
    ...
</array>
```

Each `NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE` string in the array identifies a reason why your app or third-party SDK collects a data type. For possible values, see “Report the reasons your app or third-party SDK collects data” in [`Describing data use in privacy manifests`](https://developer.apple.com/documentation/BundleResources/describing-data-use-in-privacy-manifests).

To add the `NSPrivacyCollectedDataTypePurposes` key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.
2. Click the disclosure triangle to the left of the dictionary to reveal it.
3. Confirm the dictionary contains a `NSPrivacyCollectedDataType` key with a value as described in [`Add a collected data type key`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-key.md).
4. Click the Add button (+) beside the dictionary to add a new item.
5. In the pop-up menu, choose `NSPrivacyCollectedDataTypePurposes`.
6. In the Type column, confirm that the value is `Array`.
7. Click the disclosure triangle to the left of `NSPrivacyCollectedDataTypePurposes` to reveal it.
8. Click the Add button (+) beside `NSPrivacyCollectedDataTypePurposes` to add a reason.
9. Choose a reason from the pop-up menu in the Value column. For possible values, see “Report the reasons your app or third-party SDK collects data” in [`Describing data use in privacy manifests`](https://developer.apple.com/documentation/BundleResources/describing-data-use-in-privacy-manifests).

Repeat the last two steps for each reason your app or third-party SDK collects this data type.

#### Add a Collected Data Type and Reasons Dictionary

A privacy collected data type and reasons dictionary includes a data type, a data linked to the user status, a tracking status, and a list of reasons for collecting this data type. The dictionary contains exactly four keys: `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, and `NSPrivacyCollectedDataTypePurposes`. It uses the following format:

```xml
<dict>
    <!-- Add a privacy collected data type key. -->
    <key>NSPrivacyCollectedDataType</key>
    <string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>

    <!-- Add a privacy collected data type linked key. -->
    <key>NSPrivacyCollectedDataTypeLinked</key>
    <false/>

    <!-- Add a privacy collected data type tracking key. -->
    <key>NSPrivacyCollectedDataTypeTracking</key>
    <false/>

    <!-- Add a privacy collected data type purposes key. -->
    <key>NSPrivacyCollectedDataTypePurposes</key>
    <array>
        <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
        ...
    </array>
</dict>
```

To add a privacy collected data type and reasons dictionary to the `NSPrivacyCollectedDataTypes` key in your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator in Xcode.
2. Find the `NSPrivacyCollectedDataTypes` key in the property list editor.
3. Click the disclosure triangle to the left of `NSPrivacyCollectedDataTypes` to reveal it.
4. Click the Add button (+) beside `NSPrivacyCollectedDataTypes` to insert a new item.
5. Confirm the value is `Dictionary` in the Type column.
6. Click the disclosure triangle to the left of the dictionary to reveal it.
7. To add the `NSPrivacyCollectedDataType` key to the dictionary, see [`Add a collected data type key`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-key.md).
8. To add the `NSPrivacyCollectedDataTypeLinked` key to the dictionary, see [`Add a collected data type linked key`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-linked-key.md).
9. To add the `NSPrivacyCollectedDataTypeTracking` key to the dictionary, see [`Add a collected data type tracking key`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-tracking-key.md).
10. To add the `NSPrivacyCollectedDataTypePurposes` key to the dictionary, see [`Add a collected data type purposes key`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-purposes-key.md).

#### Add the Collected Data Types Key

The `NSPrivacyCollectedDataTypes` key is an array of privacy collected data type and reasons dictionaries. For more information, see [`Add a collected data type and reasons dictionary`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-and-reasons-dictionary.md). The key uses the following format:

```xml
<key>NSPrivacyCollectedDataTypes</key>
<array>
    <dict>
        <!-- Add a privacy collected data type key. -->
        <key>NSPrivacyCollectedDataType</key>
        <string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>

        <!-- Add a privacy collected data type linked key. -->
        <key>NSPrivacyCollectedDataTypeLinked</key>
        <false/>

        <!-- Add a privacy collected data type tracking key. -->
        <key>NSPrivacyCollectedDataTypeTracking</key>
        <false/>

        <!-- Add a privacy collected data type purposes key. -->
        <key>NSPrivacyCollectedDataTypePurposes</key>
        <array>
            <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
            ...
        </array>
    </dict>
    ...
</array>
```

To add the `NSPrivacyCollectedDataTypes` key to your privacy manifest:

1. Select `PrivacyInfo.xcprivacy` in the Project navigator.
2. Click the Add button (+) beside the `App Privacy Configuration` key in the property list editor.
3. In the pop-up menu that appears, choose `NSPrivacyCollectedDataTypes`.
4. Confirm the value is `Array` in the Type column.
5. To add a privacy collected data type and reasons dictionary, see [`Add a collected data type and reasons dictionary`](tn3184-adding-data-collection-details-to-your-privacy-manifest#Add-a-collected-data-type-and-reasons-dictionary.md).

The following example declares the contacts information collected from the user in an app named `Sample`:

Repeat step 5 for each additional data type your app or third-party SDK collects. In the following example, `Sample` additionally collects user ID information from the user:

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

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3184-adding-data-collection-details-to-your-privacy-manifest)*