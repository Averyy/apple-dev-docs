# TN3182: Adding privacy tracking keys to your privacy manifest

**Framework**: Technotes

Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

#### Overview

When you build an app or third-party SDK that contacts domains engaged in tracking, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):

1. Add the `NSPrivacyTracking` key and set its value to `true`.
2. Add the `NSPrivacyTrackingDomains` key and set its value to a list of tracking domains.

For more information about these keys and the privacy manifest, see [`Privacy manifest files`](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files).

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

![A privacy manifest that contains the NSPrivacyTracking and NSPrivacyTrackingDomains keys. NSPrivacyTrackingDomains contains one tracking domain.](/images/com.apple.technotes/tn3182-privacy_tracking_single_domain@2x.png)

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

![A privacy manifest that contains the NSPrivacyTracking and NSPrivacyTrackingDomains keys. NSPrivacyTrackingDomains contains two tracking domains.](/images/com.apple.technotes/tn3182-privacy_tracking_multiple_domains@2x.png)

#### Revision History

- **2024-12-17** First published.

## See Also

- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest)*