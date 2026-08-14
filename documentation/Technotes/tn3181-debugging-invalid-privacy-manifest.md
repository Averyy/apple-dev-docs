# TN3181: Debugging an invalid privacy manifest

**Framework**: Technotes

Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.

#### Overview

Starting November 12, 2024, apps you submit for review in App Store Connect must contain a valid privacy manifest file. If you upload an app to App Store Connect that contains invalid privacy manifest files, you’ll receive an email that includes the name and path of the invalid files in your app bundle. For example:

```None
ITMS-91056: Invalid privacy manifest - The PrivacyInfo.xcprivacy file from the following path
is invalid: "PrivacyInfo.xcprivacy". Keys and values in your app's privacy manifests must be
valid. For more details about privacy manifest files, visit: 
https://developer.apple.com/documentation/bundleresources/privacy_manifest_files.
```

An invalid privacy manifest is:

- A property list file that contains invalid keys or values.
- An improperly formatted property list file.

Review [`Privacy manifest files`](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) to learn about the keys you can include in a privacy manifest. This document lists possible reasons for invalid privacy tracking and accessed API values in your privacy manifest. Validate your privacy manifest to determine why your privacy manifest is malformed.

#### Configure a Tracking Domain

A tracking domain is a string that identifies an internet domain your app or third-party SDK connects to that engages in tracking. You set the value of the `NSPrivacyTrackingDomains` key to a list of tracking domains in your privacy manifest. The value of the string meets the following requirements:

- Includes the top-level domain or subdomain.
- Contains no path and query components.
- Contains no trailing slash.

#### Possible Reason for an Invalid Tracking Value

A value for the `NSPrivacyTracking` key is invalid if the value is any other type than a `Boolean`. In your privacy manifest, change the type of the key to `Boolean`.

#### Possible Reasons for an Invalid Tracking Domains Value

A value for the `NSPrivacyTrackingDomains` key is invalid if the value is any other type than an array of strings. In your privacy manifest, change the type of the key to `Array`, then add one or more tracking domains to the array. For more information, see [`Configure a tracking domain`](tn3181-debugging-invalid-privacy-manifest#Configure-a-tracking-domain.md).

You can create an invalid privacy manifest when you use both `NSPrivacyTrackingDomains` and `NSPrivacyTracking` keys as follows:

| Reason | Solution |
| --- | --- |
| The value of the `NSPrivacyTracking` key is `true` and the value of the `NSPrivacyTrackingDomains` key is an empty array of strings. | Fill the array with one or more tracking domains your app or third-party SDK connects to. |
| The value of the `NSPrivacyTracking` key is `true` and the value of the `NSPrivacyTrackingDomains` key is an array of strings, but some entries are improperly formatted. | Confirm you configure each tracking domain in the array as described in [`Configure a tracking domain`](tn3181-debugging-invalid-privacy-manifest#Configure-a-tracking-domain.md). |
| The value of the `NSPrivacyTracking` key is `false` and the `NSPrivacyTrackingDomains` key contains some entries. | Remove the `NSPrivacyTrackingDomains` key from your privacy manifest. |

> **Note**: If your app or third-party SDK doesn’t connect, or no longer connects to any tracking domains, remove both `NSPrivacyTrackingDomains` and `NSPrivacyTracking` keys from your privacy manifest. Alternatively, set the value of `NSPrivacyTracking` to `false` and remove `NSPrivacyTrackingDomains` from your privacy manifest.

#### Possible Reasons for an Invalid Accessed Api Type Value

The following table lists reasons why a value for the `NSPrivacyAccessedAPIType` key is invalid:

| Reason | Solution |
| --- | --- |
| The value is any other type than a string. | Change the type of the `NSPrivacyAccessedAPIType` key to `String` in your privacy manifest. |
| The value is an empty string, or a string whose value doesn’t match a category of required reason APIs. | Set the value of the `NSPrivacyAccessedAPIType` key to a string that exactly matches a category of required reason APIs your app uses. For possible values, see [`Describing use of required reason API`](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api). |

#### Possible Reasons for an Invalid Accessed Api Type Reasons Value

The following table lists reasons why a value for the `NSPrivacyAccessedAPITypeReasons` key is invalid:

| Reason | Solution |
| --- | --- |
| The value is any other type than an array of strings. | Change the type of the `NSPrivacyAccessedAPITypeReasons` key to `Array` in your privacy manifest. |
| The value is an empty array of strings. | In the dictionary that contains the `NSPrivacyAccessedAPITypeReasons` key, check the value of the `NSPrivacyAccessedAPIType` key. Add one or more reason strings to the array whose value exactly matches a value associated with `NSPrivacyAccessedAPIType`. |
| The value is an array of strings, but some entries don’t match the expected values for the `NSPrivacyAccessedAPIType` key you provide. | In the dictionary that contains the `NSPrivacyAccessedAPITypeReasons` key, check the value of the `NSPrivacyAccessedAPIType` key. Confirm each reason string in the array exactly matches a value associated with `NSPrivacyAccessedAPIType`. |

> **Note**: If your app or third-party SDK doesn’t use, or no longer uses a specific required reason API, remove its related dictionary from the `NSPrivacyAccessedAPITypes` key. If `NSPrivacyAccessedAPITypes` is empty, remove it from the privacy manifest.

#### Possible Reasons for an Invalid Accessed Api Types Value

The following table lists reasons why a value for the `NSPrivacyAccessedAPITypes` key is invalid:

| Reason | Solution |
| --- | --- |
| The value is any other type than an array of dictionaries. | Change the type of the `NSPrivacyAccessedAPITypes` key to `Array` in your privacy manifest. |
| The value is an empty array of dictionaries. | Create a dictionary that includes information about a required reason API your app or third-party SDK uses, then add the dictionary to the array. Repeat the process for all required reason APIs your app or third-party SDK uses. |
| The value is an array of dictionaries, but some of the dictionaries are invalid. | Confirm each dictionary in the array contains a `NSPrivacyAccessedAPIType` key and a `NSPrivacyAccessedAPITypeReasons` key, and both keys contain valid values. |

#### Validate Your Privacy Manifest File

You can use the `plutil` command to ensure your privacy manifest is a properly formatted plist file. To validate your privacy manifest, run `plutil` with the `-lint` option in Terminal:

```zsh
% plutil -lint /path/to/PrivacyInfo.xcprivacy
```

If the privacy manifest is a valid plist, the command prints a message similar to the following:

```zsh
% plutil -lint PrivacyInfo.xcprivacy
~/Documents/SampleApp/PrivacyInfo.xcprivacy: OK
```

If the privacy manifest is malformed, an error message appears in Terminal:

```zsh
% plutil -lint PrivacyInfo.xcprivacy
~/Documents/SampleApp/PrivacyInfo.xcprivacy: Encountered unexpected character 
`a` on line 8 while looking for close tag 
```

To fix the errors, open your privacy manifest in a text editor or Xcode to address them.

> **Note**: If your privacy manifest is a valid plist, check its keys and values. Your privacy manifest could still be invalid if its keys and values don’t match the values App Store Connect expects. For more information about the keys and values App Store Connect expects, see [`Privacy manifest files`](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files).

#### Revision History

- **2024-11-12** First published.

## See Also

- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3181-debugging-invalid-privacy-manifest)*